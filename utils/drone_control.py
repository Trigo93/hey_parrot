from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy
import olympe
import os
import time

DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1")
drone = olympe.Drone(DRONE_IP)

def connect():
    drone.connect()

def disconnect():
    drone.disconnect()

def takeoff():
    print("🚁 Taking off")
    drone(TakeOff()).wait().success()

def land():
    print("🛬 Landing")
    drone(Landing()).wait().success()

def move_drone(dx, dy, dz, dpsi):
    print(f"🚀 Moving dx={dx}, dy={dy}, dz={dz}, dpsi={dpsi}")
    drone(moveBy(dx, dy, dz, dpsi)).wait().success()
