import streamlit as st
import tempfile
import os
import time
import wave
from utils.stt import SpeechToText
from utils.intent import IntentDetector
from utils.response import ResponseGenerator
from utils.tts import TextToSpeech

@st.cache_resource
def load_models():
    return {
        'stt': SpeechToText(),
        'intent': IntentDetector(), 
        'response': ResponseGenerator(),
        'tts': TextToSpeech()
    }

def safe_file_cleanup(file_path, max_attempts=5, delay=0.1):
    """Safely delete file with retry mechanism for Windows"""
    for attempt in range(max_attempts):
        try:
            if os.path.exists(file_path):
                os.unlink(file_path)
            return True
        except PermissionError:
            time.sleep(delay)
            delay *= 2 
    return False

def create_wav_file(audio_data, sample_rate):
    """Create WAV file with proper context management"""
    tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    tmp_file.close()  
    
    try:
        with wave.open(tmp_file.name, 'wb') as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes((audio_data * 32767).astype('int16').tobytes())
        return tmp_file.name
    except Exception as e:
        safe_file_cleanup(tmp_file.name)
        raise e

def main():
    st.set_page_config(
        page_title="Multilingual Conversational AI",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 Multilingual Conversational AI Demo")
    st.subheader("Supports English and Hindi")
    
    models = load_models()

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Conversation")
        
        if st.button("Start Recording (5 seconds)", type="primary"):
            with st.spinner("Recording..."):
                try:
                    audio_data, sample_rate = models['stt'].record_audio()
                    tmp_audio_path = create_wav_file(audio_data, sample_rate)
                    
                    #transcribe
                    text, language = models['stt'].transcribe(tmp_audio_path)
                    
                    if text.strip():
                        st.success(f"**You said ({language}):** {text}")
                        #intent detection
                        intent, confidence = models['intent'].detect_intent(text)
                        
                        #generate response
                        response = models['response'].generate_response(text, intent, language)
                        
                        st.info(f"**AI Response:** {response}")
                        
                        #speech conversion
                        audio_file = models['tts'].speak(response, language)
                        if audio_file:
                            st.audio(audio_file, format="audio/mp3")
                            # Clean up TTS file
                            safe_file_cleanup(audio_file)
                    
                    # Clean up audio file with retry mechanism
                    if not safe_file_cleanup(tmp_audio_path):
                        st.warning("Could not clean up temporary file - this is normal on Windows")
                        
                except Exception as e:
                    st.error(f"Error during recording: {str(e)}")
        
        # Text input alternative
        st.subheader("Or type your message:")
        user_input = st.text_input("Enter your message in English or Hindi:")
        
        if user_input:
            try:
                intent, confidence = models['intent'].detect_intent(user_input)
                response = models['response'].generate_response(user_input, intent)
                
                st.write(f"**Intent detected:** {intent} (confidence: {confidence:.2f})")
                st.write(f"**AI Response:** {response}")
                
                # TTS for typed input
                audio_file = models['tts'].speak(response)
                if audio_file:
                    st.audio(audio_file, format="audio/mp3")
                    safe_file_cleanup(audio_file)
                    
            except Exception as e:
                st.error(f"Error processing text input: {str(e)}")
    
    with col2:
        st.header("System Info")
        st.write("**Supported Languages:**")
        st.write("- All") 
        
        st.write("**Features:**")
        st.write("- Speech-to-Text")
        st.write("- Intent Detection") 
        st.write("- AI Response Generation")
        st.write("- Text-to-Speech")
        
        # Add system status
        st.write("**System Status:**")
        if 'stt' in st.session_state:
            st.write("✅ Models Loaded")
        else:
            st.write("⏳ Loading Models...")

if __name__ == "__main__":
    main()
