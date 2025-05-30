
from fastapi import FastAPI , HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

@app.get("/")
async def welcome():
    try:
        return{"message":"Hello from RCW 1003"}
    except Exception as e:
        print(f'Exception: {e}')
        raise HTTPException(status_code=500 , detail = str(e))
    
@app.get("/test")
async def Bienvenue():
    try:
        return{"message":"Hello from server "}
    except Exception as e:
        print(f'Exception: {e}')
        raise HTTPException(status_code=500 , detail = str(e))    