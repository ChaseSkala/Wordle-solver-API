from typing import Union
from fastapi import FastAPI
from wordle_solver import solve_wordle
from pydantic import BaseModel
app = FastAPI()

class GuessRequest(BaseModel):
    guess: str

class GuessResponse(BaseModel):
    solution: str
    attempts: list
@app.get("/")
def read_root():
    word, attempts, history = solve_wordle(None)
    return {
        "solution": word,
        "attempts": attempts,
        "history": history.to_dict()
    }

@app.post("/guess")
def make_guess(data: GuessRequest):
    word, attempts, history = solve_wordle(data.guess.lower())
    return {
        "solution": word,
        "attempts": attempts,
        "history": history.to_dict()
    }
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)