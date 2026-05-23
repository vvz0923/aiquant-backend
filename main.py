
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

@app.get("/")
def home():
    return {"status":"AI Quant Backend Running"}

@app.post("/balance")
def balance(req: APIRequest):

    try:

        client = Client(
            req.api_key,
            req.secret_key
        )

        balances = client.futures_account_balance()

        usdt_balance = "0"

        for asset in balances:

            if asset["asset"] == "USDT":

                usdt_balance = asset["balance"]

        return {
            "balance": usdt_balance
        }

    except Exception as e:

        return {
            "error": str(e)
        }

@app.get("/strategies")
def strategies(balance: float = 0):

    if balance < 1000:

        return {
            "strategies":[
                {
                    "name":"低风险 EMA 趋势策略",
                    "win_rate":"72%",
                    "position":"10%",
                    "leverage":"2X",
                    "take_profit":"5%",
                    "stop_loss":"2%",
                    "reasons":[
                        "小资金优先保护本金",
                        "EMA趋势稳定",
                        "波动率较低"
                    ]
                },
                {
                    "name":"AI 网格策略",
                    "win_rate":"69%",
                    "position":"8%",
                    "leverage":"1X",
                    "take_profit":"4%",
                    "stop_loss":"2%",
                    "reasons":[
                        "适合震荡行情",
                        "回撤较低",
                        "适合小仓位"
                    ]
                }
            ]
        }

    elif balance < 10000:

        return {
            "strategies":[
                {
                    "name":"PPO 强化学习策略",
                    "win_rate":"81%",
                    "position":"15%",
                    "leverage":"3X",
                    "take_profit":"8%",
                    "stop_loss":"3%",
                    "reasons":[
                        "AI检测趋势增强",
                        "成交量放大",
                        "ETH结构看涨"
                    ]
                },
                {
                    "name":"MACD 趋势突破策略",
                    "win_rate":"77%",
                    "position":"12%",
                    "leverage":"3X",
                    "take_profit":"7%",
                    "stop_loss":"3%",
                    "reasons":[
                        "MACD金叉",
                        "趋势延续概率高",
                        "风险中等"
                    ]
                }
            ]
        }

    else:

        return {
            "strategies":[
                {
                    "name":"机构级 AI 趋势组合",
                    "win_rate":"84%",
                    "position":"20%",
                    "leverage":"5X",
                    "take_profit":"10%",
                    "stop_loss":"4%",
                    "reasons":[
                        "大资金适合组合策略",
                        "AI判断主升趋势",
                        "市场流动性充足"
                    ]
                },
                {
                    "name":"高频波动策略",
                    "win_rate":"79%",
                    "position":"18%",
                    "leverage":"5X",
                    "take_profit":"9%",
                    "stop_loss":"4%",
                    "reasons":[
                        "适合高资金高流动性",
                        "AI识别短期波动",
                        "适合快速交易"
                    ]
                }
            ]
        }
