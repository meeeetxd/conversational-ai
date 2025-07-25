# 🤖 Vakta AI - Multilingual Conversational Assistant

A sophisticated multilingual conversational AI system that seamlessly integrates speech-to-text, natural language understanding, intelligent response generation, and text-to-speech capabilities. Built with Python and Streamlit, Vakta AI supports both English and Hindi languages.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.29+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **🎤 Speech Recognition**: High-quality speech-to-text using OpenAI Whisper
- **🌍 Multilingual Support**: Seamless conversation in English and Hindi
- **🧠 Intent Detection**: Intelligent understanding of user intentions
- **💬 AI Response Generation**: Context-aware responses using local Ollama or cloud LLMs
- **🔊 Text-to-Speech**: Natural voice synthesis using Google TTS
- **📱 Interactive Web Interface**: Beautiful and responsive Streamlit UI
- **⚡ Real-time Processing**: Fast audio recording and transcription

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit UI  │    │  Audio Input    │    │  Text Input     │
│   (app.py)      │    │  (Microphone)   │    │  (Keyboard)     │
└─────────┬───────┘    └─────────┬───────┘    └─────────┬───────┘
          │                      │                      │
          └──────────────────────┼──────────────────────┘
                                 │
                    ┌─────────────▼─────────────┐
                    │    Speech-to-Text         │
                    │    (utils/stt.py)         │
                    │    - Whisper Model        │
                    │    - Audio Recording      │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │    Intent Detection       │
                    │    (utils/intent.py)      │
                    │    - Rule-based System    │
                    │    - Multilingual         │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │   Response Generation     │
                    │   (utils/response.py)     │
                    │   - Ollama Local LLM      │
                    │   - Groq Cloud API        │
                    └─────────────┬─────────────┘
                                  │
                    ┌─────────────▼─────────────┐
                    │    Text-to-Speech         │
                    │    (utils/tts.py)         │
                    │    - Google TTS           │
                    │    - Audio Playback       │
                    └───────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Microphone for voice input
- Internet connection (for TTS and cloud LLM APIs)
- Optional: Ollama for local LLM inference

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/vakta-ai.git
   cd vakta-ai
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your API keys
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Quick Test

For a simple command-line test without Streamlit:
```bash
python convoAi.py
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
# Required for cloud LLM
GROQ_API_KEY=your_groq_api_key_here

# Optional configurations
DEFAULT_LANGUAGE=en
WHISPER_MODEL=medium
RECORDING_DURATION=5
```

### Local LLM Setup (Optional)

To use local Ollama instead of cloud APIs:

1. **Install Ollama**
   ```bash
   # Visit https://ollama.ai for installation instructions
   ```

2. **Pull a model**
   ```bash
   ollama pull mistral
   # or
   ollama pull llama3.2
   ```

3. **Start Ollama server**
   ```bash
   ollama serve
   ```

## 📖 Usage Guide

### Voice Interaction

1. Click "🎤 Start Recording (5 seconds)"
2. Speak your message clearly
3. Wait for transcription and AI response
4. Listen to the AI's voice response

### Text Interaction

1. Type your message in the text input field
2. Press Enter or click Send
3. View the AI response and intent detection
4. Optionally listen to the voice response

### Supported Commands

- **Greetings**: "Hello", "Hi", "नमस्ते", "नमस्कार"
- **Questions**: "What is...", "How to...", "क्या है...", "कैसे..."
- **Help**: "Help me", "मदद करो", "सहायता"
- **Farewells**: "Goodbye", "Bye", "अलविदा"
- **General conversation**: Any other text or speech

## 🛠️ Component Details

### Speech-to-Text (`utils/stt.py`)
- **Model**: OpenAI Whisper (medium)
- **Features**: Multilingual transcription, real-time recording
- **Audio**: 16kHz sample rate, 5-second recording duration

### Intent Detection (`utils/intent.py`)
- **Approach**: Rule-based keyword matching
- **Languages**: English and Hindi
- **Intents**: Greeting, farewell, question, help, weather, general

### Response Generation (`utils/response.py`)
- **Primary**: Local Ollama LLM (Mistral/Llama)
- **Fallback**: Groq cloud API (Llama 3.1)
- **Backup**: Predefined responses
- **Features**: Context-aware, multilingual responses

### Text-to-Speech (`utils/tts.py`)
- **Engine**: Google Text-to-Speech (gTTS)
- **Languages**: English (en), Hindi (hi)
- **Output**: MP3 audio files with automatic cleanup

## 🔍 Troubleshooting

### Common Issues

1. **FFmpeg not found**
   ```bash
   # Windows (Chocolatey)
   choco install ffmpeg
   
   # macOS (Homebrew)
   brew install ffmpeg
   
   # Ubuntu/Debian
   sudo apt install ffmpeg
   ```

2. **Microphone not working**
   - Check system permissions
   - Verify microphone access in browser
   - Test with other recording applications

3. **LLM API errors**
   - Verify API keys in `.env` file
   - Check internet connection
   - Ensure Ollama is running (if using local LLM)

4. **Module import errors**
   - Activate virtual environment
   - Reinstall requirements: `pip install -r requirements.txt`
   - Check Python version compatibility

### Performance Optimization

- Use smaller Whisper models (`base` instead of `medium`) for faster transcription
- Configure local Ollama for offline operation
- Adjust recording duration based on your needs
- Use GPU acceleration if available

## 📁 Project Structure

```
vakta-ai/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore file
├── README.md           # This file

├── utils/              # Core modules
│   ├── __init__.py
│   ├── stt.py          # Speech-to-Text
│   ├── intent.py       # Intent Detection
│   ├── response.py     # Response Generation
│   └── tts.py          # Text-to-Speech
│
└── venv/               # Virtual environment (not in git)
```

## 🚧 Development

### Adding New Intents

1. Edit `utils/intent.py`:
   ```python
   self.intents = {
       "your_intent": ["keyword1", "keyword2", "हिंदी_कीवर्ड"],
       # ... existing intents
   }
   ```

2. Add corresponding responses in `utils/response.py`:
   ```python
   self.fallback_responses = {
       "your_intent": {
           "en": "English response",
           "hi": "हिंदी उत्तर"
       },
       # ... existing responses
   }
   ```

### Extending Language Support

1. Add language detection in `utils/stt.py`
2. Update TTS language codes in `utils/tts.py`
3. Add fallback responses for new languages
4. Update intent keywords for new languages

### Custom LLM Integration

1. Modify `utils/response.py`
2. Add your LLM API client
3. Update the `generate_response` method
4. Configure API keys in `.env`

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and add tests
4. Commit your changes: `git commit -am 'Add feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenAI Whisper** - Robust speech recognition
- **Google TTS** - Natural text-to-speech synthesis
- **Streamlit** - Beautiful web interface framework
- **Ollama** - Local LLM inference platform
- **Groq** - Fast cloud LLM API
- **Transformers** - State-of-the-art NLP models

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/meeeetxd/conversational-ai/issues)
- **Discussions**: [GitHub Discussions](https://github.com/meeeetxd/conversational-ai/discussions)
- **Documentation**: This README and code comments

---

