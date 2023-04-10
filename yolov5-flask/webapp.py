"""
Simple app to upload an image via a web form 
and view the inference results on the image in the browser.
"""
import argparse
import base64
import io
import os
from PIL import Image
import datetime

import torch
from flask import Flask, render_template, request, redirect


import tensorflow as tf
import librosa
import numpy as np

os.environ['KMP_DUPLICATE_LIB_OK']='True'

def get_mfcc(wav_file_path):
  y, sr = librosa.load(wav_file_path)
  mfcc = np.array(librosa.feature.mfcc(y=y, sr=sr))
  return mfcc

def get_melspectrogram(wav_file_path):
  y, sr = librosa.load(wav_file_path)
  mel_spect = librosa.feature.melspectrogram(y=y, sr=sr)
  log_melspectrogram = np.array(librosa.power_to_db(mel_spect))
  return log_melspectrogram

def get_feature(file_path):
  # Extracting MFCC feature
  mfcc = get_mfcc(file_path)
  mfcc_mean = mfcc.mean(axis=1)
  mfcc_min = mfcc.min(axis=1)
  mfcc_max = mfcc.max(axis=1)
  mfcc_feature = np.concatenate( (mfcc_mean, mfcc_min, mfcc_max) )

  # Extracting Mel Spectrogram feature
  melspectrogram = get_melspectrogram(file_path)
  melspectrogram_mean = melspectrogram.mean(axis=1)
  melspectrogram_min = melspectrogram.min(axis=1)
  melspectrogram_max = melspectrogram.max(axis=1)
  melspectrogram_feature = np.concatenate( (melspectrogram_mean, melspectrogram_min, melspectrogram_max) )
  
  feature = np.concatenate( (melspectrogram_feature, mfcc_feature) )
  return feature


app = Flask(__name__)
audio_model = tf.keras.models.load_model('model.h5')

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return render_template("index.html", error="No file selected.")
        file = request.files["file"]
        if not file:
            return render_template("index.html", error="No file selected.")

        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model([img])

        # results.render()  # updates results.imgs with boxes and labels
        # now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        # img_savename = f"static/{now_time}.png"
        # Image.fromarray(results.ims[0]).save(img_savename)
        # return redirect(img_savename)

        results.render()  # updates results.imgs with boxes and labels
        now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        img_savename = f'static/images/{now_time}.png'
        Image.fromarray(results.ims[0]).save(img_savename)
        img_url = '/' + img_savename  # URL for the image
    
        # results.render()  # updates results.imgs with boxes and labels
        # img_io = io.BytesIO()
        # Image.fromarray(results.ims[0]).save(img_io, "PNG")
        # img_io.seek(0)
        # img_base64 = base64.b64encode(img_io.getvalue()).decode()

        return render_template("index.html", image=img_url)

    return render_template("index.html")

@app.route('/varroa-report')
def varroa_report():
    image_names = os.listdir('static/images')
    return render_template('varroa-report.html', title='Varroa Mite Report', image_names=image_names)


@app.route('/audio', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['audio_file']
        file.save('audio.mp3')
        feature = get_feature('audio.mp3')
        prediction = audio_model.predict(feature.reshape(1,444))
        hives = ['StrongHive','WeakHive'] 
        result = hives[np.argmax(prediction)]
        os.remove('audio.mp3')
        return render_template('audio.html', result=result)
    else:
        return render_template('audio.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'custom', 'best1.pt')  # force_reload = recache latest code
    model.eval()
    app.run(port=args.port)  # debug=True causes Restarting with stat
