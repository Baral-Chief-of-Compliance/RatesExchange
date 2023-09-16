from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from exchange_rates import get_exchange_rates


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/api/rates")
async def rates_converter(from_currency: str, to_currency: str, value: int):
    if from_currency and to_currency and value:
        for_one_amount = get_exchange_rates(from_currency, to_currency)
        result = for_one_amount * value
        return {
            "result_exchange_rate": round(result, 2)
        }
    else:
        raise HTTPException(status_code=400, detail="Bad Request")
