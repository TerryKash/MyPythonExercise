import requests

def speak(a, str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(a)
    speak.Speak(str)

if __name__ == '__main__':
    r = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=***")
    r = r.json()
    # print(r)
    i = 0
    while i < 10:
        i += 1
        t= "Title"
        d= "Description"
        print(i)
        speak(" ", str(i))
        r1 = r["articles"][i]["title"]
        print("Title -", r1)
        speak(t, r1)
        r2 = r["articles"][i]["description"]
        print("Description -", r2)
        speak(d, r2)