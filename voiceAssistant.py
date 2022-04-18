from __future__ import annotations
import speech_recognition as sr
from googleSearch import getUrlFromTextRequest
from time import sleep
import main
import os 
from alias import alias 
def getStrFromAudio() -> str:
    os.system("clear")
    rec = sr.Recognizer()
    rec.energy_threshold = 41459.80577455177
    rec.dynamic_energy_threshold = True
    voiceData = ""

    with sr.Microphone(device_index=1) as source:
        audio   = rec.listen(source)
        try:                            voiceData   = rec.recognize_google(audio)
        except sr.UnknownValueError:    voiceData   = "NULL"

    return voiceData

def getWord(words:list[str], index:int) -> word:
    tmp = ""
    for word in words[index:]:
        tmp += f"{word} "
    return tmp

def response(sample) -> Terminal:
    if (sample[0] in alias["download"] and len(sample)>1):
        searchName = getWord(sample, 1)
        man = main.manager()
        man = man.songMode()
        i = 0
        while True:
            url = getUrlFromTextRequest(searchName, i)
            try:
                man = man.setLink(url)
                man = man.setUnsafeMode()
                man = man.runDownloaderContext()
                print(f" STATUS : OK")
                break
            except:
                print(f" STATUS : ERROR, TRYING AGAIN")
                i += 1




def mainLoop():
    while True:
        print(" :Esperando resposta [MIC]: ")
        try:
            res = getStrFromAudio()
            print(f"Resposta recebida: {res}")

            response(res.lower().split())
        except KeyboardInterrupt:
            break
if __name__ == "__main__":
    mainLoop()
