import sounddevice as sd
import vosk
import queue
import json

q = queue.Queue()

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, flush=True)
    q.put(bytes(indata))

def record_and_transcribe(model_path="models/vosk-model-small-en-us-0.15"):
    model = vosk.Model(model_path)
    samplerate = 16000

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, samplerate)
        print("🎙️ Please speak your command...")
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result.get("text", "")
                print(f"🗣️ Recognized: {text}")
                return text
            # partial results could be used for UI feedback, if you want
