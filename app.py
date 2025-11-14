import os
import sys
import webbrowser
from threading import Timer
from flask import Flask, request, render_template, jsonify
from ask_ai import AIQueryTool

app = Flask(__name__)
ai_tool = AIQueryTool()

def open_browser():
    webbrowser.open('http://127.0.0.1:5000')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    responses = {
        'chatgpt': ai_tool.ask_chatgpt(question),
        'gemini': ai_tool.ask_gemini(question),
        'claude': ai_tool.ask_claude(question)
    }
    
    return jsonify(responses)

@app.route('/compare', methods=['POST'])
def compare():
    data = request.json
    comparison_question = (
        f"Analysera dessa tre AI-svar och svara på svenska.\n\n"
        f"VIKTIGT FORMAT:\n"
        f"- Första meningen: Ange ENBART vilket svar som är bäst (ChatGPT, Gemini eller Claude)\n"
        f"- Sedan minst en tom rad\n"
        f"- Sedan motivering i punktform eller löpande text\n"
        f"- Använd normal text, INTE versaler\n\n"
        f"ChatGPT svarade: {data['chatgpt']}\n\n"
        f"Gemini svarade: {data['gemini']}\n\n"
        f"Claude svarade: {data['claude']}"
    )

    analyses = {
        'ChatGPT': ai_tool.ask_chatgpt(comparison_question),
        'Gemini': ai_tool.ask_gemini(comparison_question),
        'Claude': ai_tool.ask_claude(comparison_question)
    }

    return jsonify(analyses)

if __name__ == '__main__':
    # Open browser automatically when the app starts
    Timer(1.5, open_browser).start()
    
    # Run the app
    app.run(debug=False)