import sys
import threading

from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt

import speech_recognition as sr
import pyttsx3 as tts
from neuralintents.assistants import BasicAssistant


class Assistant(QWidget):

    def __init__(self):
        super().__init__()

        # Ses tanıma ve TTS motoru ayarları
        self.recognizer = sr.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty("rate", 150)

        # Yapay zeka asistanı
        self.assistant = BasicAssistant("intents.json")
        self.assistant.fit_model(epochs=50)
        self.assistant.save_model()

        # PyQt5 GUI ayarları
        self.initUI()

        # Asistanı ayrı bir thread'de çalıştırma
        threading.Thread(target=self.run_assistant, daemon=True).start()

    def initUI(self):
        self.setWindowTitle('Voice Assistant')

        self.label = QLabel("🤖", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 120px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.show()

    def create_file(self):
        with open("somefile.txt", "w") as f:
            f.write("hello world")

    def run_assistant(self):
        while True:
            try:
                with sr.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()

                    if "hey arche" in text:
                        self.label.setStyleSheet("color: red;")  # Rengi kırmızı yap

                        audio = self.recognizer.listen(mic)
                        text = self.recognizer.recognize_google(audio)
                        text = text.lower()
                        if text == "stop":
                            self.speaker.say("Bye")
                            self.speaker.runAndWait()
                            self.speaker.stop()
                            self.close()
                            sys.exit()

                        else:
                            if "create a file" in text:
                                self.create_file()
                            else:
                                response = self.assistant.request(text)
                                if response:
                                    self.speaker.say(response)
                                    self.speaker.runAndWait()
                            self.label.setStyleSheet("color: black;")  # Rengi tekrar siyah yap

            except Exception as e:
                print(e)
                self.label.setStyleSheet("color: black;")
                continue


if __name__ == '__main__':
    app = QApplication(sys.argv)
    assistant = Assistant()
    sys.exit(app.exec_())
