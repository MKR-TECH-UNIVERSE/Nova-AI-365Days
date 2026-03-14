import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
from config import Config

class VoiceHandler:
    """Handle voice input/output using gTTS"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.language = Config.LANGUAGE  # 'hi-IN' for Hindi-English mix
    
    def speak(self, text):
        """
        Text ko speech mein convert karega (gTTS)
        Args: text (str) - Jo bolna hai
        """
        try:
            print(f"🤖 Nova: {text}")
            
            # gTTS se audio generate karo
            tts = gTTS(text=text, lang=self.language, slow=False)
            
            # Temporary file save karo
            temp_file = os.path.join(Config.BASE_DIR, "temp_voice.mp3")
            tts.save(temp_file)
            
            # Play the audio
            playsound(temp_file)
            
            # Delete temporary file
            os.remove(temp_file)
            
        except Exception as e:
            print(f"❌ Error in speak: {e}")
            # Fallback: Print kardo
            print(f"🤖 [TEXT-ONLY MODE]: {text}")
    
    def listen(self, timeout=5):
        """
        Mic se sunega aur text return karega
        Args: timeout (int) - Kitni der tak sunna hai
        Returns: query (str) - Jo user ne bola
        """
        try:
            with sr.Microphone() as source:
                print("🎤 Listening...")
                
                # Background noise adjust karo
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                # Suno
                audio = self.recognizer.listen(source, timeout=timeout)
                
            print("🎤 Processing...")
            
            # Google Speech Recognition se text nikalo
            query = self.recognizer.recognize_google(audio, language=self.language)
            
            print(f"🗣️ You said: {query}")
            return query.lower()
            
        except sr.WaitTimeoutError:
            print("⏰ Timeout: Kuch nahi suna")
            return ""
        except sr.UnknownValueError:
            print("❌ Samajh nahi aaya")
            return ""
        except sr.RequestError as e:
            print(f"❌ Internet error: {e}")
            return ""
        except Exception as e:
            print(f"❌ Error in listen: {e}")
            return ""
    
    def test_voice(self):
        """Test function - voice module check karne ke liye"""
        print("\n🧪 Testing Voice Module...\n")
        
        # Test 1: Speak
        self.speak("Hello! Main Nova hoon. Kaise ho aap?")
        
        # Test 2: Listen
        print("\n🎤 Ab aap bolo kuch...")
        query = self.listen(timeout=5)
        
        if query:
            self.speak(f"Aapne kaha: {query}")
            print(f"✅ Test successful! You said: {query}")
        else:
            print("⚠️  Kuch nahi suna, but module ready hai!")
        
        print("\n✅ Voice Module Ready!")

# Test ke liye
if __name__ == "__main__":
    voice = VoiceHandler()
    voice.test_voice()