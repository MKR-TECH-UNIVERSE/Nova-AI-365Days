import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """All settings in one place"""
    
    # API Keys (from .env file)
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')
    
    # Voice Settings
    WAKE_WORD = "nova"
    VOICE_NAME = "Rachel"
    LANGUAGE = "hi-IN"
    
    # Paths
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    MUSIC_FOLDER = os.path.join(os.path.expanduser('~'), 'Music')
    
    @staticmethod
    def setup():
        """Create necessary folders"""
        os.makedirs(os.path.join(Config.BASE_DIR, 'data'), exist_ok=True)
        os.makedirs(os.path.join(Config.BASE_DIR, 'assets'), exist_ok=True)
        print("✅ Folders created!")

# Auto setup
Config.setup()