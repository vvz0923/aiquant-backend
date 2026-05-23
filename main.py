
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from binance.client import Client

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class APIRequest(BaseModel):
    api_key: str
    secret_key: str

@app.post("/balance")
def get_balance(req: APIRequest):

    try:

        client = Client(
            req.api_key,
            req.secret_key
        )

        balances =
            client.futures_account_balance()

        usdt_balance = 0

        for asset in balances:

            if asset["asset"] == "USDT":

                usdt_balance =
                    asset["balance"]

        return {
            "balance": usdt_balance
        }

    except Exception as e:

        return {
            "error": str(e)
        }
