# CompareAI - Multi-AI Query Tool

Query ChatGPT, Claude and Gemini simultaneously and compare their responses side by side. Built to understand how different LLMs reason about the same question.

## What it does

Type a question. Get three answers. Compare them. The tool also uses AI to analyze which model gave the best response (yes, AI judging AI).

## Tech stack

- **Backend:** Python / Flask
- **APIs:** OpenAI, Anthropic (Claude), Google Generative AI (Gemini)
- **Frontend:** Vanilla JavaScript, responsive design
- Built-in retry logic and error handling per provider

## Setup

```bash
git clone https://github.com/Kullendorff/compareai.git
cd compareai
pip install -r requirements.txt
```

Create a `.env` file:
```
ANTHROPIC_API_KEY=your_key
OPENAI_API_KEY=your_key
GOOGLE_API_KEY=your_key
```

Run:
```bash
python app.py
```

Opens at `http://127.0.0.1:5000`

## Why I built this

I wanted to understand how different AI models handle the same prompt. Not benchmarks or leaderboards, but actual side-by-side comparison of reasoning patterns, tone and accuracy. Turns out they disagree more often than you'd expect.

## License

MIT
