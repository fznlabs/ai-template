from fastapi import FastAPI
from pydantic import BaseModel
from logic import add_numbers

app = FastAPI()

class CalculationInput(BaseModel):
    num_1: int
    num_2: int

@app.post("/calculate")
def calculate_sum(data: CalculationInput):
    result = add_numbers(data.num_1, data.num_2)
    return {"result": result}