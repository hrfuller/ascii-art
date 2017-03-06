from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash

from flask.json import jsonify as json
from PIL import Image

app = Flask(__name__)

# Our set of ASCII chars in increasing order of lightness to map greyscale
# pixel vals onto.
ascii_ramp = (
                "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxr"
                "jft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
            )
num_chars = len(ascii_ramp)

# maximum width or height (whichever is largest in input) for image scaling
ascii_art_size = 2**8  # seems like a nice number.
greyscale_precision = 2**8  # PIL 'L' mode greyscale is 8-bit precision.


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/artify', methods=['POST'])
def artify():
    if 'file' not in request.files:
        return ("Please attach an image file to the POST request", 400, [])
    try:
        im = Image.open(request.files['file'])
    except:
        return (
            "Was not able to parse file. Are you sure you uploaded an image?",
            400,
            []
        )

    # convert image to greyscale: 8-bit precision
    im = im.convert(mode='L')

    aspect_ratio = float(im.height) / im.width
    # new dimension (width, height)
    new_size = [ascii_art_size, ascii_art_size]
    # Make largest dimension of ASCII raster ascii_art_size,
    # and maintain original aspect ratio.
    if aspect_ratio >= 1:
        # scale down width to maintain original aspect ratio.
        new_size[0] = int(round(new_size[0] / aspect_ratio))
    else:
        # scale down height to maintain original aspect ratio.
        new_size[1] = int(round(new_size[1] * aspect_ratio))

    # resize the raster to the new size
    im = im.resize(new_size)
    ascii_art = ''
    width, height = im.size

    for y in xrange(height):
        for x in xrange(width):
            px = im.getpixel((x, y))
            best_char_idx = int(num_chars * (float(px)/greyscale_precision))
            ascii_art += ascii_ramp[best_char_idx]
        ascii_art += '\n'
    return json(art=ascii_art)
