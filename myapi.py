from fastapi import FastAPI, File, UploadFile, Response
import uvicorn
from PIL import Image
import numpy as np
import tensorflow as tf
import traceback
import time

model = tf.keras.models.load_model('./saved_model/something_v2.h5')
app = FastAPI()

@app.get("/")
async def index():
    return "This is spofity!"

@app.post("/")

async def predict(file: UploadFile=File(...)):
    try:
        image = Image.open(file.file)
        image = np.asarray(image.resize((160, 160)))
        image = image/255
        image = np.expand_dims(image, 0)

        start_time = time.time()
        result = model.predict(image)
        end_time = time.time()
        prediction = np.argmax(result)
        time_predict = round(end_time - start_time,2)

        accuracy = np.max(result)

        if prediction == 0:
            return {
                'id': '1',
                'name' : 'Barbell',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict),
                }
        elif prediction == 1:
            return {
                'id': '2',
                'name':'Dumbell',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 2:
            return {
                'id': '3',
                'name':'Gym ball',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 3:
            return {
                'id': '4',
                'name':'Kattle ball',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 4:
            return {
                'id': '5',
                'name':'Leg press',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 5:
            return {
                'id': '6',
                'name':'Punching bag',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 6:
            return {
                'id': '7',
                'name':'Roller ABS',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 7:
            return {
                'id': '8',
                'name':'Statis bicycle',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 8:
            return {
                'id': '9',
                'name':'Step',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }
        elif prediction == 9:
            return {
                'id': '10',
                'name':'Treadmill',
                "accuracy": float(accuracy),
                "time_predict": float(time_predict)
                }

    except Exception as e:
        traceback.print_exc()
        return {"message" : "Internal Server Error"} 
    
if __name__ == '__main__':
    port = 8001
    print(f"Listening to http://0.0.0.0:{port}")
    uvicorn.run(app, host='0.0.0.0',port=port)
