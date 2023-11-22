from fastapi import FastAPI

app = FastAPI()

#app.get("/home")

@app.get("/home")
def home():
    #fastapi==0.98.0
    #uvicorn==0.22.0
    #press i to write and escape and :wq (write and quit) to exit
    return "success": True, "message":"Hello World"
