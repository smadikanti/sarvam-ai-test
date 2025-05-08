# Telugu Text-to-Speech Web Application

A simple web application and CLI tool that converts typed text to Telugu speech using the Sarvam AI API.

## Features

- Web interface for typing or pasting text
- Convert text to natural-sounding Telugu speech
- Audio playback directly in the browser
- Command-line interface for quick conversions
- Interactive CLI mode for multiple conversions

## Demo

![Telugu TTS Demo](demo.gif)

## Requirements

- Python 3.6+
- Sarvam AI API key (get one at [Sarvam AI Dashboard](https://dashboard.sarvam.ai))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/telugu-tts-app.git
cd telugu-tts-app
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root directory and add your Sarvam AI API key:
```
SARVAM_API_KEY=your_api_key_here
```

## Usage

### Web Interface

1. Start the web application:
```bash
python app.py
```

2. Open your web browser and navigate to http://127.0.0.1:5000

3. Type or paste text in the text area, then click "Convert to Speech"

4. The audio will be generated and played in the browser

### Command Line

#### Single Text Conversion

```bash
python cli_example.py "Your text here"
```

#### Interactive Mode

```bash
python cli_example.py
```

Then enter text at the prompt, and press Enter to convert to speech. Press Ctrl+C to exit.

## Customization

You can customize the speech parameters in both `app.py` and `cli_example.py`:

- `target_language_code`: Language code (default: "te-IN" for Telugu)
- `speaker`: Voice to use (options: "anushka", "karun", "meera", etc.)
- `pitch`: Adjust the pitch (-1 to 1)
- `pace`: Adjust the speaking speed (0.3 to 3)
- `loudness`: Adjust the volume (0.1 to 3)
- `speech_sample_rate`: Audio quality (8000, 16000, 22050, or 24000)

## How It Works

1. The application collects text input from the user
2. It sends the text to the Sarvam AI API for text-to-speech conversion
3. The API returns base64-encoded audio data
4. The application decodes the audio and plays it back

## Credits

This project uses the [Sarvam AI API](https://docs.sarvam.ai/) for text-to-speech conversion.

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. 