from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form['text']
    lang = request.form.get('lang', 'hi')

    if not text.strip():
        return jsonify({'error': 'No text provided'}), 400

    tts = gTTS(text=text, lang=lang, slow=False)
    audio_buffer = io.BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)

    return send_file(
        audio_buffer,
        mimetype='audio/mp3',
        as_attachment=True,
        download_name='speech.mp3'
    )

@app.route('/self-clone', methods=['POST'])
def self_clone():
    return jsonify({
        'status': 'ok',
        'message': 'Self voice clone feature coming soon. Backend API abhi connect karna hai.'
    })

if __name__ == '__main__':
    app.run(debug=True)
