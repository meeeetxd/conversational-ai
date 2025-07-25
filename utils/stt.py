import whisper
import sounddevice as sd
import numpy as np
import tempfile
import wave
import warnings

class SpeechToText:
    def __init__(self):
        # Suppress the FP16 warning          
        warnings.filterwarnings("ignore", message="FP16 is not supported on CPU")
        
        # Load Whisper model
        self.model = whisper.load_model("medium")
    
    def record_audio(self, duration=5, sample_rate=16000):     
        """Record audio from microphone"""
        print("Recording...")
        audio_data = sd.rec(int(duration * sample_rate), 
                           samplerate=sample_rate, 
                           channels=1, dtype=np.float32)
        sd.wait()
        print("Recording completed")
        return audio_data, sample_rate
    
    def transcribe(self, audio_file_path):
        """Transcribe audio to text"""
        try:
            result = self.model.transcribe(audio_file_path)
            return result["text"], result.get("language", "unknown")
        except Exception as e:
            print(f"Transcription error: {e}")
            return "", "unknown"
