from typing import Union
from fastapi import FastAPI
from wordle_solver import solve_wordle
from pydantic import BaseModel
from mangum import Mangum

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

handler = Mangum(app)
