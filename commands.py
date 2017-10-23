import subprocess
import os


class Commander:
    def __init__(self):
        self.confirm = [
            "yes", "affimartive", "si", "sure", "do it", "yeah", "confirm"
        ]
        self.cancel = [
            "no", "negative", "negative soldier", "don't", "wait", "cancel"
        ]

    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me you name yet")
            else:
                self.respond("My name is python commander. How are you?")
        if "launch" or "open" in text:
            app = text.split(" ", 1)[-1]
            self.respond("Opening "+ app)
            os.system(app + ".exe")

    def respond(self, response):
        print(response)
        subprocess.call('tts.exe -f 10 -v 1 "' + response + '"', shell=True)
