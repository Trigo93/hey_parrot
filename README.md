# 🦜 Hey Parrot

**Voice-controlled drone interface using local LLMs and Parrot Olympe SDK**

---

## 🚀 Quickstart

### 1. Clone the repo

```bash
git clone https://github.com/Trigo93/hey_parrot.git
cd hey_parrot
```

### 2. Install dependencies

Install Python packages (ideally in a virtual environment):

```bash
pip install -r models/requirements_ollama.txt
```

Make sure `ollama` is installed and running:  
https://ollama.com/download

```bash
ollama run mistral
```

(Optional but recommended):
```bash
ollama pull llama3:8b
# Or for higher performance (if your GPU can handle it):
# ollama pull llama3:70b
```

### 3. Install `vosk` model (speech-to-text)

Download the English model manually:  
[https://alphacephei.com/vosk/models](https://alphacephei.com/vosk/models)

Recommended: `vosk-model-small-en-us-0.15` (50MB)

```bash
wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
unzip vosk-model-small-en-us-0.15.zip -d models/vosk
```

Your folder should look like: `models/vosk/vosk-model-small-en-us-0.15`

### 4. Launch the system

```bash
python main.py
```

---

## 🎤 Voice control loop

The interface listens to your voice and sends commands to the drone using:

- `takeoff()`
- `land()`
- `move_drone(dx, dy, dz, dpsi)`

Examples of natural commands:

- "take off"
- "go up 2 meters"
- "turn left and move forward 3 meters"
- "land"

---

## 🧠 LLM tool usage

We use `ollama.chat()` with `tools` (function calling) to ensure structured, safe outputs.

The LLM never replies with free-form text. It only returns a valid function call (or nothing) based on:

- A strong system prompt (`models/prompt.txt`)
- Few-shot examples loaded from `models/shots.json`

---

## 🔇 Suppress noisy Olympe logs

The script removes most `Olympe` debug logs by setting:

```python
logging.getLogger("olympe").setLevel(logging.ERROR)
```

This keeps the console clean and focused on useful outputs.

---

## 📁 Project structure

```txt
.
├── main.py                  # Main loop: speech → LLM → drone
├── utils/
│   ├── drone_control.py     # Functions mapped to LLM tool calls
│   ├── load_txt.py          # Prompt + few-shot loader
│   └── vosk_listener.py     # Speech-to-text (Vosk)
├── models/
│   ├── prompt.txt           # System prompt for LLM
│   ├── shots.json           # Few-shot examples
│   └── requirements_ollama.txt
├── doc/
│   └── archi.txt            # Architecture overview (flowchart-style)
```

---

## 📦 Dependencies

- [Parrot Olympe SDK](https://developer.parrot.com/docs/olympe/)
- `ollama` (local LLM runner)
- `vosk` (offline speech recognition)
- Python 3.10+

---

## 🤖 Why not parsing? Why LLMs?

See the full write-up in [`medium_article.md`](medium_article.md)