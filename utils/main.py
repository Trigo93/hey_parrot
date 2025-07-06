from utils.voice_input import record_and_transcribe
from utils.llm import run_llm
from utils.olympe_log_remover import suppress_olympe_logs
from utils import drone_control

def main():
    drone_control.connect()

    try:
        while True:
            user_text = record_and_transcribe()
            if not user_text or len(user_text.strip()) < 2:
                print("Ignoring empty or very short input.")
                continue
            run_llm(user_text)
    except KeyboardInterrupt:
        print("Exiting.")
    finally:
        drone_control.disconnect()


if __name__ == "__main__":
    with suppress_olympe_logs():
        main()
