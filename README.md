# 🤖 ARIA - AI Reasoning & Interactive Assistant

ARIA is a personal AI assistant powered by Google Gemini 1.5 Flash, featuring intelligent conversation and built-in calculator tools.

## ✨ Features

- 💬 **Natural Language Chat** - Have conversations with Google Gemini
- 🧮 **Smart Calculator** - Perform arithmetic calculations through natural language
- ⚡ **Fast Responses** - Powered by Gemini 1.5 Flash for quick interactions
- 🔧 **Extensible Tools** - Easy to add new tools and capabilities

## 🚀 Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vhakash/ARIA-personal-assistant-.git
   cd ARIA-personal-assistant-
   ```

2. **Set up your Google API key**:
   - Get a free API key from [Google AI Studio](https://aistudio.google.com/)
   - Create a `.env` file:
     ```
     GOOGLE_API_KEY=your_gemini_api_key_here
     ```

3. **Install dependencies**:
   ```bash
   uv sync
   ```

4. **Run ARIA**:
   ```bash
   uv run main.py
   ```

## 💬 Example Usage

```
🤖 Welcome to ARIA - AI Reasoning & Interactive Assistant!
Powered by Google Gemini 1.5 Flash with calculator tools.

You: What's 15 + 27?
Assistant: I'll calculate that for you! 15 + 27 = 42

You: Tell me a joke
Assistant: Why don't scientists trust atoms? Because they make up everything!

You: quit
```

## 🛠️ Tech Stack

- **Python 3.12+**
- **LangChain** - AI framework
- **Google Gemini 1.5 Flash** - Language model
- **LangGraph** - Agent execution
- **UV** - Package management

## 📝 License

MIT License - feel free to use and modify!

## 🤝 Contributing

Pull requests welcome! Feel free to add new tools and features.

---

*ARIA - Making AI assistance personal and powerful* ✨
