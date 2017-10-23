import subprocess
import os
from get_answer import Fetcher


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
        else:
            fetcher = Fetcher("https://www.google.com.br/search?q=" + text)
            answer = fetcher.lookup()
            self.respond(answer)

    def respond(self, response):
        print(response)
        subprocess.call('tts.exe -f 10 -v 1 "' + response + '"', shell=True)
