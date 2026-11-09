from fastapi import FastAPI

app = FastAPI()

# Example in-memory storage
items = [
    {"id": 1, "title": "Write code", "completed": False},
    {"id": 2, "title": "Review notes", "completed": True},
]


@app.get("/")
def read_root():
    return {"message": "Welcome to the To-Do API!"}


# TODO: Add routes for listing tasks, creating tasks, and updating/deleting items
