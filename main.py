#!/usr/bin/env python3
"""
🚀 NOVA AI - DAY 1
Fresh Start - Clean Code
"""

from config import Config

def main():
    print("=" * 50)
    print("🚀 NOVA AI - DAY 1/365")
    print("=" * 50)
    print(f"✅ Config loaded successfully")
    print(f"✅ Wake Word: {Config.WAKE_WORD}")
    print(f"✅ Voice: {Config.VOICE_NAME}")
    print(f"✅ Language: {Config.LANGUAGE}")
    print("=" * 50)
    print("🎉 Day 1 Setup Complete!")
    print("=" * 50)

if __name__ == "__main__":
    main()