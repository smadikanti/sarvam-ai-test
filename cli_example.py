#!/usr/bin/env python
import os
import sys
import argparse
import tempfile
import subprocess
import base64
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the API key
API_KEY = os.getenv("SARVAM_API_KEY")
if not API_KEY:
    print("Error: SARVAM_API_KEY not found in environment variables or .env file")
    print("Please set your API key by creating a .env file with:")
    print("SARVAM_API_KEY=your_api_key_here")
    sys.exit(1)

def text_to_speech(text, output_file=None):
    """Convert text to Telugu speech using Sarvam AI API"""
    try:
        # Initialize the Sarvam AI client
        client = SarvamAI(
            api_subscription_key=API_KEY,
        )
        
        # Convert text to speech
        response = client.text_to_speech.convert(
            inputs=[text],
            model="bulbul:v2",
            target_language_code="te-IN",  # Telugu language code
            speaker="anushka",
            pitch=0,
            pace=1.0,
            loudness=1.0,
            speech_sample_rate=16000,
            enable_preprocessing=True
        )
        
        # Get the audio data and decode from base64
        audio_base64 = response.audios[0]
        audio_bytes = base64.b64decode(audio_base64)
        
        # Use the provided output file or create a temporary one
        if not output_file:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
            output_file = temp_file.name
            temp_file.close()
        
        # Save the audio data to the file
        with open(output_file, 'wb') as f:
            f.write(audio_bytes)
        
        print(f"Speech saved to: {output_file}")
        
        # Try to play the audio (platform dependent)
        try:
            if sys.platform == 'darwin':  # macOS
                subprocess.call(['afplay', output_file])
            elif sys.platform == 'linux':
                subprocess.call(['aplay', output_file])
            elif sys.platform == 'win32':  # Windows
                subprocess.call(['start', output_file], shell=True)
        except Exception as e:
            print(f"Could not automatically play audio: {e}")
            print(f"Please manually open the file: {output_file}")
            
        return output_file
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def main():
    parser = argparse.ArgumentParser(description='Convert text to Telugu speech using Sarvam AI')
    parser.add_argument('text', nargs='?', help='Text to convert to speech')
    parser.add_argument('-o', '--output', help='Output audio file path (default: temporary file)')
    args = parser.parse_args()
    
    # If no text provided via arguments, enter interactive mode
    if not args.text:
        print("Enter text to convert to Telugu speech (Ctrl+C to exit):")
        try:
            while True:
                text = input("> ")
                if text.strip():
                    text_to_speech(text, args.output)
        except KeyboardInterrupt:
            print("\nExiting...")
    else:
        text_to_speech(args.text, args.output)

if __name__ == "__main__":
    main() 