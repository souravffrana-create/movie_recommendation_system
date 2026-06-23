from fastapi import FastAPI
from api.data_validation import user_data
from models.recommendation import Recommendation
from fastapi.responses import JSONResponse


app = FastAPI()



@app.get("/")
def info():
    message = "Movies Recommendation API"
    return {"message":message}

@app.get("/health")
def health():
    status = "OK"
    return {"Model Status":status}

@app.post("/recommend")
def recommend(data:user_data):
    
    input = data.Title

    try:
      result = Recommendation(input)
      return JSONResponse(status_code=200,content={"Recommendation":result})
    except Exception as e:
        return JSONResponse(status_code=500,content=str(e))
    




