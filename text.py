import whisper

model = whisper.load_model("base")
result = model.transcribe("DIALOGUE.ogg")
print(result)