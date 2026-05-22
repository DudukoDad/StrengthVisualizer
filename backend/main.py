from fastapi import FastAPI

# Create the application instance
app = FastAPI()

# Define a basic GET endpoint
@app.get("/")
def read_root():
    return {"message": "You are a Goober"}

# Define an endpoint with a parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}