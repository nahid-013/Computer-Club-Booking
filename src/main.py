from fastapi import FastAPI
from src.places.hall_places.routers import place_router
import uvicorn


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Привет, мир!"}


app.include_router(place_router)

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)