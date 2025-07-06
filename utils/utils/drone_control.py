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

def get_tools():
    return [
        {
            "type": "function",
            "function": {
                "name": "takeoff",
                "description": "Command the drone to take off",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "land",
                "description": "Command the drone to land",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": []
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "move_drone",
                "description": "Move the drone with relative motion and rotation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dx": {"type": "number", "description": "Forward/backward (m)"},
                        "dy": {"type": "number", "description": "Left/right (m)"},
                        "dz": {"type": "number", "description": "Up/down (m)"},
                        "dpsi": {"type": "number", "description": "Yaw in radians"}
                    },
                    "required": ["dx", "dy", "dz", "dpsi"]
                }
            }
        }
    ]