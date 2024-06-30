from fastapi import FastAPI, File, UploadFile
import speech_recognition as sr
import os
from pydub import AudioSegment

app = FastAPI()

# Function to convert MP3 to WAV
def convert_to_wav(mp3_file):
    # Load MP3 audio
    audio = AudioSegment.from_mp3(mp3_file)
    # Create WAV file path
    wav_file = mp3_file.replace(".mp3", ".wav")
    # Export as WAV
    audio.export(wav_file, format="wav")
    return wav_file

# Function to transcribe audio
def transcribe_audio(wav_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()
    # Load WAV audio
    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)
        try:
            # Transcribe speech using Google Web Speech API
            transcription = recognizer.recognize_google(audio_data)
            return transcription
        except sr.UnknownValueError:
            return "Speech could not be understood"
        except sr.RequestError as e:
            return f"Could not request results from Google Web Speech API; {e}"

@app.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    # Save uploaded MP3 file
    mp3_file = f"temp/{file.filename}"
    with open(mp3_file, "wb") as buffer:
        buffer.write(await file.read())
    # Convert MP3 to WAV
    wav_file = convert_to_wav(mp3_file)
    # Transcribe audio
    transcription = transcribe_audio(wav_file)
    # Remove temporary files
    os.remove(mp3_file)
    os.remove(wav_file)
    return {"transcription": transcription}
