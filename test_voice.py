#!/usr/bin/env python3
"""
Day 2: Voice Module Test
"""

from core.voice import VoiceHandler

def main():
    print("=" * 50)
    print("🎤 DAY 2: VOICE MODULE TEST")
    print("=" * 50)
    
    # Voice handler create karo
    voice = VoiceHandler()
    
    print("\n🧪 TEST 1: Speak Function")
    print("-" * 50)
    voice.speak("Hello! Main Nova hoon. Aap kaise hain?")
    
    print("\n🧪 TEST 2: Listen Function")
    print("-" * 50)
    print("🎤 Mic mein bolo kuch (5 seconds)...")
    query = voice.listen(timeout=5)
    
    if query:
        print(f"✅ Success! Aapne kaha: {query}")
        voice.speak(f"Maine suna: {query}")
    else:
        print("⚠️  Kuch nahi suna, but module kaam kar raha hai!")
    
    print("\n" + "=" * 50)
    print("✅ VOICE MODULE READY!")
    print("=" * 50)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Test cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")