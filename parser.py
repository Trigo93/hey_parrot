
import json
import re
from olympe.messages.ardrone3.Piloting import TakeOff, Landing, moveBy

def parse_simple_command(text):
    text = text.lower()

    if "take off" in text or "takeoff" in text:
        return TakeOff()

    elif "land" in text or "landing" in text:
        return Landing()

    return None

def convert_to_olympe(text):
    if "nothing" in text:
        return None

    if "takeoff" in text:
        return TakeOff()
    
    if "landing" in text:
        return Landing()
    
    try:
        params = json.loads(text)
    except json.JSONDecodeError:
        print("❌ Invalid JSON format.")
        return None

    # Defensive default values
    dx = float(params.get("dx", 0.0))
    dy = float(params.get("dy", 0.0))
    dz = float(params.get("dz", 0.0))
    dpsi = float(params.get("dpsi", 0.0))

    print(f"🚁 Moving: dx={dx}, dy={dy}, dz={dz}, dpsi={dpsi}")
    return moveBy(dx, dy, dz, dpsi)
