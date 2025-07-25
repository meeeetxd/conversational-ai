from gtts import gTTS
import tempfile
import os
import streamlit as st

class TextToSpeech:
    def __init__(self):
        pass
    
    def speak(self, text, language="en"):
        """Convert text to speech"""
        try:
            if language == "unknown":
                language = "en"

            if language in ["hi", "hindi"]:
                lang_code = "hi"
            else:
                lang_code = "en"
            
            # speech generation
            tts = gTTS(text=text, lang=lang_code, slow=False)
            
            #temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts.save(tmp_file.name)
                return tmp_file.name
                
        except Exception as e:
            st.error(f"TTS Error: {str(e)}")
            return None
