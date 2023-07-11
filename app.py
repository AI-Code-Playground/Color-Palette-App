from flask import Flask, request, render_template
from colorthief import ColorThief
from PIL import Image
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    colors = None
    if request.method == 'POST':
        file = request.files['file']
        img = Image.open(file.stream)  # PIL image
        img.save("uploaded_image.jpg", "JPEG")  # Save the image
        color_thief = ColorThief("uploaded_image.jpg")
        # Get the color palette
        palette = color_thief.get_palette(color_count=6, quality=1)
        colors = [{'rgb': color, 'hex': '#{:02x}{:02x}{:02x}'.format(*color)} for color in palette]
    return render_template('upload.html', colors=colors)

if __name__ == '__main__':
    app.run(debug=True)
