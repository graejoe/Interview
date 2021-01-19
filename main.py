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
    if(query == 'What is your quest?'):
        return "coding"
    if(query == 'Source code for this exercise?'):
        return "https://github.com/graejoe/Interview"

    if(q[0].isnumeric()):
        sum = 0
        numbers = q.split(' ')
        for number in numbers:
            if(number.isnumeric()):
                sum += int(number)
        return sum
    if(q[0] == '<'):
        combo = list(map(int, q.lstrip('< ').rstrip(' >').split(' ')))
        even = list()
        odd = list()
        answer = list()
        for number in combo:
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
        odd.sort()
        even.sort(reverse=True)
        for i in range(5):
            answer.append(odd[i] + even[i])

        return answer
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