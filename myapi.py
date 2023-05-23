from fastapi import FastAPI, File, UploadFile
import uvicorn
from PIL import Image
import numpy as np
import tensorflow as tf


model = tf.keras.models.load_model('./saved_model/something.h5')
app = FastAPI()

@app.get("/")
async def index():
    return "Halo Bandung!"

@app.post("/")

async def predict(file: UploadFile=File(...)):
    image = Image.open(file.file)
    image = np.asarray(image.resize((150, 150)))
    image = image/255
    image = np.expand_dims(image, 0)
    result = np.argmax(model.predict(image))

    if result == 0:
      return 'Barbell'
    elif result == 1:
        return 'Dumbell'
    elif result == 2:
        return 'Gym ball'
    elif result == 3:
        return 'Kattle ball'
    elif result == 4:
        return 'Leg press'
    elif result == 5:
        return 'Punching bag'
    elif result == 6:
        return 'Roller ABS'
    elif result == 7:
        return 'Statis bicycle'
    elif result == 8:
        return 'Step'
    elif result == 9:
        return 'Treadmill'

if __name__ == '__main__':
    uvicorn.run("myapi:app", host='127.0.0.1')