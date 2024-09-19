from fastapi import FastAPI, Request
from models import hepsiburada
import joblib

# Read models saved during train phase
estimator_hepsiburada_loaded = joblib.load("saved_models/randomforest_with_hepsiburada.pkl")

app = FastAPI()

def make_hepsiburada_prediction(model, request):
    # parse input from request
    memory= request["memory"]
    ram= request["ram"]
    screen_size= request["screen_size"]
    power= request["power"]
    front_camera= request["front_camera"]
    rc1= request["rc1"]
    rc3= request["rc3"]
    rc5= request["rc5"]
    rc7= request["rc7"]


    # Make an input vector
    hepsiburada = [[memory, ram, screen_size, power, front_camera, rc1, rc3, rc5, rc7]]

    # Predict
    prediction = model.predict(hepsiburada)

    return prediction[0]

# Hepsiburada Prediction endpoint
@app.post("/prediction/hepsiburada")
def predict_hepsiburada(request: hepsiburada):
    prediction = make_hepsiburada_prediction(estimator_hepsiburada_loaded, request.dict())
    return prediction

# Get client info
@app.get("/client")
def client_info(request: Request):
    client_host = request.client.host
    client_port = request.client.port
    return {"client_host": client_host,
            "client_port": client_port}