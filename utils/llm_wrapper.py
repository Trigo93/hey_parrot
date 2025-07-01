# llm_wrapper.py
import subprocess
import socket
import time


def is_ollama_running(host="localhost", port=11434) -> bool:
    """Check if Ollama is running by trying to connect to its API port."""
    try:
        with socket.create_connection((host, port), timeout=1):
            return True
    except OSError:
        return False


def start_ollama_daemon():
    """Start Ollama in background if not already running."""
    print("Starting Ollama daemon...")
    subprocess.Popen(["ollama", "serve"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    # Wait for it to start up
    for _ in range(10):
        if is_ollama_running():
            print("Ollama is now running.")
            return
        time.sleep(1)
    raise RuntimeError("Ollama failed to start.")


def query_llm(prompt: str, model: str = "mistral") -> str:
    """Query a local LLM via Ollama with a text prompt."""
    if not is_ollama_running():
        start_ollama_daemon()

    # Make sure the model is pulled
    print(f"Running prompt on model '{model}'...")
    process = subprocess.Popen(
        ["ollama", "run", model],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    stdout, stderr = process.communicate(input=prompt.encode())

    if process.returncode != 0:
        raise RuntimeError(f"LLM error: {stderr.decode().strip()}")

    return stdout.decode().strip()
