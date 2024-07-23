from fastapi import FastAPI, Request, Header, HTTPException
import pandas as pd

df = pd.DataFrame()

df["Nama"] = ["Jos", "Farhan", "Fariz", "Gocar"]
df["Lokasi"] = ["Jakarta", "Tangsel", "Gading", "Bogor"]

API_KEY = "testingapitokenkey1234" #testing api token key 1234

# buat object
app = FastAPI()

# membuat function + url (endpoint)

# endpoint untuk ambil data
@app.get("/")
def handlerData(request:Request):
    headers = request.headers

    return {"message":"This is fastapi data",
            "owner" : "Jos Ganteng",
            "slogan": "sah",
            "headers": headers
            }

@app.get("/secret")
def handlerSecret(api_key: str = Header(None)):
    if api_key != API_KEY or api_key == None:
        raise HTTPException(detail="Password salah dekk", status_code=401)
    return{
        "seret": "hanya saya dan tuhan yang tahu"
    }

@app.get("/data/{loc}")
def handlerDf(loc):
    result = df.query(f"Lokasi == '{loc}'")
    return result.to_dict(orient="records")
