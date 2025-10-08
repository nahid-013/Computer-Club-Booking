from pydantic import BaseModel

class Computer(BaseModel):
    model: str
    CPU: str
    RAM: str
    GPU: str

class Headphones(BaseModel):
    model: str

class Mouse(BaseModel):
    model: str

class Place(BaseModel):
    place_type: str
    computer_id: int
    headphones_id: int
    mouse_id: int
    free: bool
    ready: bool

class UpdatePlace(BaseModel):
    place_type: str
    computer_id: int
    headphones_id: int
    mouse_id: int
    free: bool
    ready: bool