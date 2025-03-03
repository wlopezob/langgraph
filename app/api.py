from fastapi import FastAPI
from app.agent import graph

app = FastAPI()

@app.get("/")
def agent():
    return graph.invoke({"customer_name": "William", "my_var": "Hello01"})