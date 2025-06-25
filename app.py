from flask import Flask, request, send_file
from rembg import remove
from PIL import Image
import io
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/remove-bg', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return 'No file uploaded', 400

    # Open the uploaded image
    input_image = Image.open(request.files['image'])

    # Remove the background
    output_image = remove(input_image)

    # Save result in memory
    output_io = io.BytesIO()
    output_image.save(output_io, format='PNG')
    output_io.seek(0)

    # Return the image as response
    return send_file(output_io, mimetype='image/png')

if __name__ == '__main__':
    # Use the PORT environment variable required by Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
