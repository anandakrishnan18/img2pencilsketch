from flask import Flask, render_template, request, redirect, url_for
import os
import cv2
import random
import uuid

app = Flask(__name__)
integer = random.randint(691827, 963963)
name_id = uuid.uuid1()


@app.route('/', methods=['POST', "GET"])
def home():
    os.system('mkdir uploads1')
    if request.method == 'POST':
        file = request.files['filechooser']
        file.save(os.path.join('uploads1', file.filename))
        image = cv2.imread(os.path.join('uploads1', file.filename))
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        inverted_image = 255 - gray_image
        blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), 0)
        inverted_image_blur = 255 - blurred_image
        pencil_sketch = cv2.divide(gray_image, inverted_image_blur, scale=256.0)
        cv2.imwrite('static/image.png', pencil_sketch)
        return redirect(url_for('imagepage'))
    return render_template('index.html')


@app.route('/imagepage')
def imagepage():
    return render_template('image1.html', img='static/image.png')


if __name__ == '__main__':
    app.run(debug=True)

