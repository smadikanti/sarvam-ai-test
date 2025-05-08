import os
import tempfile
from flask import Flask, render_template, request, send_file, jsonify
from sarvamai import SarvamAI
from dotenv import load_dotenv
import base64

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Initialize Sarvam AI client
client = SarvamAI(
    api_subscription_key=os.getenv("SARVAM_API_KEY"),
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthesize', methods=['POST'])
def synthesize():
    data = request.json
    text = data.get('text', '')
    voice = data.get('voice', 'anushka')
    pitch = data.get('pitch', 0)
    pace = data.get('pace', 1.0)
    
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Create a temporary file to store the audio
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.wav')
        temp_filename = temp_file.name
        temp_file.close()
        
        # Convert text to speech using Sarvam AI API
        response = client.text_to_speech.convert(
            inputs=[text],
            model="bulbul:v2",
            target_language_code="te-IN",  # Telugu language code
            speaker=voice,                 # Using the selected voice
            pitch=pitch,                   # Using the selected pitch
            pace=pace,                     # Using the selected pace
            loudness=1.0,
            speech_sample_rate=16000,
            enable_preprocessing=True
        )
        
        # Get the audio data and decode from base64
        audio_base64 = response.audios[0]
        audio_bytes = base64.b64decode(audio_base64)
        
        # Save the audio data to the temporary file
        with open(temp_filename, 'wb') as f:
            f.write(audio_bytes)
        
        return jsonify({"audio_url": f"/audio/{os.path.basename(temp_filename)}"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/audio/<filename>')
def get_audio(filename):
    temp_dir = tempfile.gettempdir()
    return send_file(os.path.join(temp_dir, filename), mimetype='audio/wav')

if __name__ == '__main__':
    # Ensure templates directory exists
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True) 