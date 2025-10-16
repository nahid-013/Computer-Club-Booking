from fastapi import FastAPI
from src.places.hall_places.routers import place_router
from src.devices.computer_routers import computer_router
from src.devices.headphone_routers import headphone_router
from src.devices.mouse_routers import mouse_router
import uvicorn


app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Привет, мир!"}


app.include_router(place_router)
app.include_router(computer_router)
app.include_router(headphone_router)
app.include_router(mouse_router)


if __name__ == '__main__':
    uvicorn.run(app="src.main:app", host="127.0.0.1", port=8000, reload=True)