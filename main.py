from typing import Union
from fastapi import FastAPI
from wordle_solver import solve_wordle
from pydantic import BaseModel
app = FastAPI()

class GuessRequest(BaseModel):
    guess: str
@app.get("/")
def read_root():
    word, attempts = solve_wordle(None)
    return {"The wordle is ": f"{word}"
            f" and it took {attempts} attempts."}

@app.post("/guess")
def make_guess(data: GuessRequest):
    guess = data.guess.lower()
    word, attempts = solve_wordle(guess)
    return {"The wordle is ": f"{word} and it took {attempts} attempts."}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)