from openai import OpenAI
import google.generativeai as genai
from anthropic import Anthropic
import os
from typing import Dict
import time
import dotenv
from pathlib import Path

class AIQueryTool:
    """
    A tool for querying multiple AI models (ChatGPT, Gemini, and Claude) and comparing their responses.
    This class handles API authentication, rate limiting, and error recovery for each service.
    """

    def __init__(self):
        """
        Initialize the AI query tool by setting up API clients and loading necessary credentials.
        Implements automatic retries and error handling for API initialization.
        """
        # Try to load from .env file first
        env_path = Path('.') / '.env'
        if env_path.exists():
            dotenv.load_dotenv()
            
        # Try environment variables first, then fallback to api-keys.txt
        self.claude_key = os.getenv('ANTHROPIC_API_KEY')
        self.openai_key = os.getenv('OPENAI_API_KEY')
        # Support both GOOGLE_API_KEY and GEMINI_API_KEY for compatibility
        self.gemini_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')
        
        # If any keys are missing, try reading from api-keys.txt
        if not all([self.claude_key, self.openai_key, self.gemini_key]):
            try:
                with open('api-keys.txt', 'r') as f:
                    self.claude_key = f.readline().strip()
                    self.openai_key = f.readline().strip()
                    self.gemini_key = f.readline().strip()
            except FileNotFoundError:
                raise Exception("No API keys found. Please either:\n1. Create a .env file with your API keys, or\n2. Create api-keys.txt with your API keys on separate lines.")
            except Exception as e:
                raise Exception(f"Error reading API keys: {str(e)}")
                
        if not all([self.claude_key, self.openai_key, self.gemini_key]):
            raise Exception("Some API keys are missing. Please check your .env file or api-keys.txt.")

        # Initialize API clients with error handling
        try:
            # OpenAI (ChatGPT) initialization
            self.openai_client = OpenAI(api_key=self.openai_key)
            
            # Google (Gemini) initialization
            genai.configure(api_key=self.gemini_key)
            
            # Use the latest Gemini model
            self.gemini_model = genai.GenerativeModel('gemini-2.0-flash-exp')
            
            # Anthropic (Claude) initialization
            self.anthropic_client = Anthropic(api_key=self.claude_key)
        except Exception as e:
            raise Exception(f"Error initializing AI clients: {str(e)}")

    def ask_chatgpt(self, question: str, retries: int = 3) -> str:
        """
        Query ChatGPT using OpenAI's latest API.
        
        Args:
            question (str): The question to ask ChatGPT
            retries (int): Number of retry attempts for failed requests
            
        Returns:
            str: ChatGPT's response or error message
        """
        for attempt in range(retries):
            try:
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "Du är en hjälpsam AI-assistent. Ge tydliga och koncisa svar på svenska. Använd normal text, inte versaler."},
                        {"role": "user", "content": question}
                    ],
                    temperature=0.7,
                    max_tokens=1000
                )
                return response.choices[0].message.content

            except Exception as e:
                if attempt == retries - 1:  # Last attempt
                    return f"ChatGPT Error: {str(e)}"
                time.sleep(1)  # Wait before retrying
                
        return "ChatGPT Error: Maximum retries reached"

    def ask_gemini(self, question: str, retries: int = 3) -> str:
        """
        Query Gemini using Google's latest API.

        Args:
            question (str): The question to ask Gemini
            retries (int): Number of retry attempts for failed requests

        Returns:
            str: Gemini's response or error message
        """
        for attempt in range(retries):
            try:
                # Add instruction to respond in Swedish
                formatted_question = f"Svara på svenska med tydlig och normal text (inte versaler).\n\n{question}"
                response = self.gemini_model.generate_content(formatted_question)

                # Check if response was blocked by safety filters
                if response.prompt_feedback.block_reason:
                    return f"Gemini Response Blocked: {response.prompt_feedback.block_reason}"

                return response.text

            except Exception as e:
                if attempt == retries - 1:  # Last attempt
                    return f"Gemini Error: {str(e)}"
                time.sleep(1)  # Wait before retrying

        return "Gemini Error: Maximum retries reached"

    def ask_claude(self, question: str, retries: int = 3) -> str:
        """
        Query Claude using Anthropic's latest API.

        Args:
            question (str): The question to ask Claude
            retries (int): Number of retry attempts for failed requests

        Returns:
            str: Claude's response or error message
        """
        for attempt in range(retries):
            try:
                response = self.anthropic_client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=1000,
                    temperature=0.7,
                    system="Du är en hjälpsam AI-assistent. Ge tydliga och koncisa svar på svenska. Använd normal text, inte versaler eller överdriven formatering.",
                    messages=[
                        {"role": "user", "content": question}
                    ]
                )
                return response.content[0].text

            except Exception as e:
                if attempt == retries - 1:  # Last attempt
                    return f"Claude Error: {str(e)}"
                time.sleep(1)  # Wait before retrying

        return "Claude Error: Maximum retries reached"

    def query_all(self, question: str) -> Dict[str, str]:
        """
        Query all AI models in parallel and return their responses.
        
        Args:
            question (str): The question to ask all AIs
            
        Returns:
            Dict[str, str]: Dictionary containing each AI's response
        """
        try:
            # In a production environment, you might want to use asyncio or threading
            # to make these calls in parallel for better performance
            responses = {
                'chatgpt': self.ask_chatgpt(question),
                'gemini': self.ask_gemini(question),
                'claude': self.ask_claude(question)
            }
            return responses
            
        except Exception as e:
            return {
                'error': f"Error querying AIs: {str(e)}"
            }

# Example usage and testing of the tool
if __name__ == "__main__":
    try:
        # Initialize the AI query tool
        ai_tool = AIQueryTool()
        
        # Test question
        test_question = "What is the capital of France?"
        
        # Get responses from all AIs
        responses = ai_tool.query_all(test_question)
        
        # Print responses
        for ai, response in responses.items():
            print(f"\n{ai.upper()} RESPONSE:")
            print(response)
            print("-" * 50)
            
    except Exception as e:
        print(f"Error running test: {str(e)}")