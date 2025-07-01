import olympe
from olympe.messages.ardrone3.PilotingState import FlyingStateChanged
import os
from utils.voice_input import record_and_transcribe
from parser import convert_to_olympe, parse_simple_command
from utils.llm_wrapper import query_llm
from utils.load_txt import load_prompt

DRONE_IP = os.environ.get("DRONE_IP", "10.202.0.1")

def main():
    drone = olympe.Drone(DRONE_IP)
    drone.connect()

    try:
        while True:
            user_text = record_and_transcribe()

            if user_text.strip() == "":
                print("⚠️ Didn't catch that. Try again.")
                continue

            if user_text.lower() in ["exit", "quit", "stop"]:
                print("👋 Exiting voice control.")
                break

            # If user command is simple, no need to interprete with LLM
            action = parse_simple_command(user_text)

            if action is None:
                # text was not simple enough, prompt LLM to inteprete
                prompt = load_prompt("prompt.txt", user_text)
                llm_response = query_llm(prompt)
                print("LLM response: ", llm_response)
                action = convert_to_olympe(llm_response)

            print("Action: ", action)
            if action is not None:
                drone(action).wait().success()

    finally:
        drone.disconnect()


if __name__ == "__main__":
    from utils.olympe_log_remover import suppress_olympe_logs

    with suppress_olympe_logs():
        main()
