# Hey Parrot 🦜

Voice-controlled Parrot drone built with **Olympe**, **Vosk**, and a local **LLM via Ollama** — featuring robust command parsing, silent-mode voice input, and safe function-based execution.

---

## 🎯 TL;DR
- Speak natural drone commands like “rise 3 meters” or “land now.”
- LLM interprets them and triggers backend functions (`takeoff()`, `land()`, `move_drone(...)`) with zero ambiguous parsing.
- Built-in filters handle silence, noise, and unexpected inputs.
- All audio and LLM logic runs locally — no API keys required.

---

## 🧠 Why few-shot “shots”?

Few-shot examples (**shots**) teach the LLM exactly how we want it to behave:
- ✅ Show correct behavior (e.g., "rise" → `move_drone(dz: -1)`)
- 🚫 Show no‑ops for greetings like "hello" or noise like "banana"
- 🧭 Establish edge cases and coordinate conventions clearly

This dramatically reduces hallucinations and makes the model more predictable without finetuning.

---

## ✏️ Why the prompt is structured like this

Our prompt combines:
- A precise **system message** detailing tools and coordinate systems
- Eye-catching **emojis** (`⬆️`, `⬇️`) for visual anchors
- Few‑shot examples demonstrating desired behavior
- Strong language: “Only call a function if… confident” to enforce caution

Together, this setup ensures the LLM outputs **only valid tool calls**, reducing unwanted behavior.

---

## 🔌 Function scheme → Why it matters

Instead of parsing LLM text output, we use **Ollama function-calling** to:
1. **Define allowed actions** (`takeoff()`, `land()`, `move_drone(dx,dy,dz,dpsi)`)
2. Constrain model output to **calling these functions only**
3. Eliminate parsing bugs, format inconsistencies, or hallucinated commands

This makes your system both **safe** and **structured**.

---

## 📴 Olympe log remover

Olympe logs can be overwhelming and clutter your console. The repo includes a helper to:
- Mute **info/debug logs**
- ⚠️ Keep **only actual errors** visible
- Make runtime output clean, focused, and developer-friendly

---

## 🗣️ Vosk voice setup (local & offline)

We use **Vosk** for offline speech recognition. To install and use the model:

1. Download a model (e.g., small English):
   ```bash
   wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
   unzip vosk-model-small-en-us-0.15.zip -d models/vosk
   ```
2. Install dependencies:
   ```bash
   pip install vosk sounddevice
   ```
3. Modify `voice_input.py` to point to your model:
   ```python
   model = vosk.Model("models/vosk/vosk-model-small-en-us-0.15")
   ```

We can’t include the large Vosk model in the repo — but with these steps anyone can run locally and offline.

---

## 🧩 Key components

- `main.py` – Main loop: listens, interprets, and executes functions
- `llm_wrapper.py` – Starts Ollama, injects prompt + shots, handles function output
- `drone_tools.py` – Defines `takeoff()`, `land()`, `move_drone(...)` paired with Olympe
- `voice_input.py` – Handles Vosk audio streaming with silence guards
- `load_*` – Helpers for loading prompt templates & shots JSON

---

## ⚙️ Installation & Quick Start

1. Clone the repo
   ```bash
   git clone https://github.com/Trigo93/hey_parrot.git
   cd hey_parrot
   ```

2. Set up Python env
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

3. Install Ollama & pull a model
   ```bash
   ollama pull llama3:8b
   ```

4. Download and unpack Vosk model (see above).

5. Run the app!
   ```bash
   python main.py
   ```

---

## 🗺️ Next steps & customization

- Extend `drone_tools.py` with more functions (e.g., `hover()`, `flip()`)
- Add extra few-shot examples for new commands in `shots.json`
- Tweak LLM model: `llama3:8b` → `llama3:70b`, `mixtral` for more accuracy
- Fine-tune hotword detection or speech timeout behavior

---

## 📣 Contributing

Feel free to open issues, suggest new voice commands, or test on different drone models!

---

## 🧪 License

MIT License — feel free to reuse, adapt, and build upon!

---

**Fly high, fly safe — Hey Parrot at your command.**
