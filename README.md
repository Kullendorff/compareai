# AI Assistant - Multiple AI Query Tool

![AI Assistant Screenshot](https://via.placeholder.com/800x400?text=AI+Assistant+Screenshot)

## Overview

This tool allows you to query multiple AI services (ChatGPT, Claude, and Gemini) simultaneously and compare their responses. It provides a clean, user-friendly web interface that displays all responses side-by-side and even lets you compare which AI gave the best answer.

## Features

- **Multi-AI Querying**: Ask the same question to ChatGPT, Claude, and Gemini at once
- **Side-by-Side Comparison**: View all responses in a clean, organized interface
- **Response Analysis**: Compare which AI provided the best answer (using AI to analyze AI!)
- **Error Handling**: Built-in retries and error recovery for reliable operation
- **Responsive Design**: Works on desktop and mobile devices

## Installation

### Prerequisites

- Python 3.8 or higher
- API keys for OpenAI, Anthropic, and Google AI

### Setup Instructions

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/ai-assistant.git
   cd ai-assistant
   ```

2. Set up your API keys (two options):

   **Option 1**: Create a `.env` file in the project root:
   ```
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   GOOGLE_API_KEY=your_google_api_key_here
   ```
   
   **Option 2**: Create an `api-keys.txt` file with each key on a separate line:
   ```
   your_anthropic_api_key
   your_openai_api_key
   your_google_api_key
   ```

3. Install required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the application:
   ```
   python app.py
   ```
   
   Or use the included batch file on Windows:
   ```
   run_ai_assistant.bat
   ```

2. Your web browser should automatically open to `http://127.0.0.1:5000`

3. Enter your question in the input field and click "Ask AIs"

4. View the responses from each AI model

5. Click "Compare Responses" to get an analysis of which AI provided the best answer

## Technical Details

- Built with Flask for the backend
- Uses official APIs for each AI service:
  - OpenAI API for ChatGPT
  - Anthropic API for Claude
  - Google Generative AI API for Gemini
- Implements automatic retries and error handling
- Responsive frontend with vanilla JavaScript

## Future Improvements

- Add support for more AI models
- Implement streaming responses
- Add authentication for multi-user environments
- Create option to save question/response history
- Add conversation context/memory

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to OpenAI, Anthropic, and Google for providing API access to their AI models
- Built as a learning project to compare different AI capabilities