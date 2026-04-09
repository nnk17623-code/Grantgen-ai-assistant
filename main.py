from fastapi import FastAPI
from modle import check_collisions
import random

app = FastAPI()

# Generate sample data
def generate_objects(n):
    data = []
    for _ in range(n):
        data.append({
            "pos": [random.randint(-50, 50) for _ in range(3)],
            "vel": [random.uniform(-1, 1) for _ in range(3)]
        })
    return data

@app.get("/")
def home():
    return {"message": "Space Debris API Running 🚀"}

@app.get("/data")
def get_data():
    satellites = generate_objects(5)
    debris = generate_objects(5)

    alerts = check_collisions(satellites, debris)

    return {
        "satellites": satellites,
        "debris": debris,
        "alerts": alerts
    }