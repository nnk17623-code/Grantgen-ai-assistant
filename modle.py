import numpy as np

def distance(p1, p2):
    return np.sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2 +
        (p1[2] - p2[2])**2
    )

def predict_position(pos, vel, t=5):
    return [
        pos[0] + vel[0]*t,
        pos[1] + vel[1]*t,
        pos[2] + vel[2]*t
    ]

def check_collisions(satellites, debris, threshold=6):
    alerts = []

    for i, s in enumerate(satellites):
        for j, d in enumerate(debris):

            future_s = predict_position(s["pos"], s["vel"])
            future_d = predict_position(d["pos"], d["vel"])

            if distance(future_s, future_d) < threshold:
                alerts.append({
                    "satellite": i,
                    "debris": j
                })

    return alerts