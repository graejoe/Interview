from fastapi import FastAPI, File, UploadFile
import urllib.parse

app = FastAPI()

@app.get("/")
def read_root(q: str = None):
    query = urllib.parse.unquote_plus(q)
    if(query == 'What is your name?'):
        return "Joe Graefe"
    if(query == 'PING'):
        return "PONG"
    if(query == "What is your quest?"):
        return "coding"

    if(q[0].isnumeric()):
        sum = 0
        numbers = q.split(' ')
        for number in numbers:
            if(number.isnumeric()):
                sum += int(number)
        return sum
    else:
        listvowels = ['a', 'e', 'i', 'o', 'u']
        words = q.split(' ')
        consonants = 0
        vowels = 0
        for word in words:
            for letter in word:
                if(letter in listvowels):
                    vowels += 1
                else:
                    consonants += 1

        return "{}-{}-{}".format(len(words), consonants, vowels)

    return query