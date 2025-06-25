from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    input_image = Image.open(request.files['image'])
    output_image = remove(input_image)

    output_io = io.BytesIO()
    output_image.save(output_io, format='PNG')
    output_io.seek(0)

    return send_file(output_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
