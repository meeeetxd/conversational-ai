import requests
import json
# from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()

class ResponseGenerator:
    def __init__(self):
        self.ollama_url = "http://localhost:11434/api/generate"
       
        # Fallback responses if Ollama isn't available
        self.fallback_responses = {
            "greeting": {
                "en": "Hello! How can I help you today?",
                "hi": "नमस्ते! मैं आपकी कैसे सहायता कर सकता हूं?"
            },
            "farewell": {
                "en": "Goodbye! Have a great day!",
                "hi": "अलविदा! आपका दिन शुभ हो!"
            },
            "question": {
                "en": "That's an interesting question. Let me think about it.",
                "hi": "यह एक दिलचस्प सवाल है। मुझे इसके बारे में सोचने दें।"
            },
            "help": {
                "en": "I'm here to help! What do you need assistance with?",
                "hi": "मैं मदद के लिए यहाँ हूँ! आपको किस चीज़ में सहायता चाहिए?"
            }
        }
    
    def llm_response(self, text, language="en"):
        llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.5, max_tokens=250)
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful and friendly multilingual conversational AI assistant which responds to user queries and texts in a very simple and concise manner. 
            - Respond in short answers.
            - Do not use any markdown formatting or any special characters
            - Be conversational, helpful, and concise
            - Keep responses natural and engaging
            - For Hindi responses, use proper Devanagari script"""),
            ("user", text)
            ])
        
        chain = prompt | llm
        result = chain.invoke({"text": text})
        return result.content

    def generate_response(self, text, intent, language="en"):
        """Generate response using Ollama or fallback"""
        try:
            # Try Ollama first
            return self.llm_response(text, language)
        except:
            # Use fallback responses
            return self._get_fallback_response(intent, language)
   
    def _get_fallback_response(self, intent, language):
        return self.fallback_responses.get(intent, {}).get(language,
               "I understand you, but I'm not sure how to respond.")
    