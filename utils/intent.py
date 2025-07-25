from transformers import pipeline
import json

class IntentDetector:
    def __init__(self):
        # Use a multilingual model for better Hindi support
        self.classifier = pipeline(
            "text-classification",
            model="microsoft/DialoGPT-medium",
            return_all_scores=True
        )
        
        # Define intents - you can expand this
        self.intents = {
            "greeting": ["hello", "hi", "namaste", "namaskar"],
            "farewell": ["bye", "goodbye", "alvida", "alavida"],
            "question": ["what", "how", "when", "where", "kya", "kaise"],
            "help": ["help", "madad", "sahayata"],
            "weather": ["weather", "mausam", "temperature"]
        }
    
    def detect_intent(self, text):
        """Simple rule-based intent detection"""
        text_lower = text.lower()
        
        for intent, keywords in self.intents.items():
            if any(keyword in text_lower for keyword in keywords):
                return intent, 0.9  # High confidence for rule-based
        
        return "general", 0.5  # Default intent
