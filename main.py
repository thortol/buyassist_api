import uvicorn
from fastapi import Request, FastAPI

from classes import MainController

app = FastAPI()
mc = MainController()

@app.get("/")
async def root():
    return "hello world"

@app.get("/get_prices")
async def get_prices(request: Request):
    '''
    Function:   Given an item, scrape amazon, lazada and shopee for competing prices
    Input:    

        {
            "item": <string with the name of the item>
        }

    Sample: 

        {
            "item": "The Legend Of Zelda Tears Of The Kingdom"
        }
    
    Output:

        {
            "amazon": <float with price on amazon>,
            "lazada": <float with price on lazada>,
            "shopee": <float with price on shopee>
        }

    Sample:

        {
            "amazon": 11.1,
            "lazada": 20.1,
            "shopee": 10.3
        }
    '''
    json = await request.json()
    return mc.get_prices(json)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)