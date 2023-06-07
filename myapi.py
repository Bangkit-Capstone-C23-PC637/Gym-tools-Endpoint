from fastapi import FastAPI, File, UploadFile, Response
import uvicorn
from PIL import Image
import numpy as np
import tensorflow as tf
import traceback

model = tf.keras.models.load_model('./saved_model/something_v2.h5')
app = FastAPI()

@app.get("/")
async def index():
    return "Halo Bandung!"

@app.post("/")

async def predict(file: UploadFile=File(...)):
    try:
        image = Image.open(file.file)
        image = np.asarray(image.resize((160, 160)))
        image = image/255
        image = np.expand_dims(image, 0)
        result = np.argmax(model.predict(image))

        if result == 0:
            return {
                'id': '1',
                'name' : 'Barbell'
                }
        elif result == 1:
            return {
                'id': '2',
                'name':'Dumbell'
                }
        elif result == 2:
            return {
                'id': '3',
                'name':'Gym ball'
                }
        elif result == 3:
            return {
                'id': '4',
                'name':'Kattle ball'
                }
        elif result == 4:
            return {
                'id': '5',
                'name':'Leg press'
                }
        elif result == 5:
            return {
                'id': '6',
                'name':'Punching bag'
                }
        elif result == 6:
            return {
                'id': '7',
                'name':'Roller ABS'
                }
        elif result == 7:
            return {
                'id': '8',
                'name':'Statis bicycle'
                }
        elif result == 8:
            return {
                'id': '9',
                'name':'Step'
                }
        elif result == 9:
            return {
                'id': '10',
                'name':'Treadmill'
                }

    except Exception as e:
        traceback.print_exc()
        return {"message" : "Internal Server Error"} 
    
if __name__ == '__main__':
    port = 8001
    print(f"Listening to http://0.0.0.0:{port}")
    uvicorn.run(app, host='0.0.0.0',port=port)
