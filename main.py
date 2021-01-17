from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.get("/")
def read_root(q: str = None):
    if(q == None):
        question = "Invalid or missing question"
        sum = "Missing Question"
    elif(q.find('+') != -1):
        sum = 0
        question = ""
        numbers = q.split('+')
        for number in numbers:
            sum += int(number)
        
        for item in q:
            question += item
    return {"Question": question,
        "Answer" : sum    }