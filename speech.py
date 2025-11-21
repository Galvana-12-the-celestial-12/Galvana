import sounddevice as sd
import numpy as np
import speech_recognition as sr
import random
from googletrans import Translator
import tensorflow
import uvicorn
import fastapi
words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"],
    "insane": ["энергия","пустота", "ноль", "голос", ""]}
while True:
    
    start = input("Начать игру? ")
    if start == "Да" or "да":
        level = input("Выберите сложность (easy, medium, hard, insane). ")

        if level == "easy":
            a = random.choice(words_by_level["easy"])
            print(a)
        elif level == "medium":
            a = random.choice(words_by_level["medium"])
            print(a)
        elif level == "hard":
            a = random.choice(words_by_level["hard"])
            print(a)
        elif level == "insane":
            a = random.choice(words_by_level["insane"])
            print(a)
        duration = 5  # секунды записи
        sample_rate = 44100
        print("Говори...")
        recording = sd.rec(
        int(duration * sample_rate), # длительность записи в сэмплах
        samplerate=sample_rate,      # частота дискретизации
        channels=1,                  # 1 — это моно
        dtype="int16")               # формат аудиоданных
        sd.wait()  # ждём завершения записи
        print("Запись завершена, теперь распознаём...")
        audio_bytes = recording.ravel().tobytes()
        audio = sr.AudioData(audio_bytes, sample_rate, sample_width=2)
        recognizer = sr.Recognizer()
        try:
            text = recognizer.recognize_google(audio, language="en-EN")
            print("Ты сказал:", text)
            translator = Translator()
            translated = translator.translate(a, dest='en')  # здесь 'en' — это английский
            if translated == text:
                print("Правильно!") 
        except sr.UnknownValueError:
            print("Не удалось распознать речь")
        except sr.RequestError as e:
            print(f'Ошибка сервиса: {e}')



