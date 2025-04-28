from pydantic import BaseModel

class Device(BaseModel):
    name: str
    ip: str
    device_type: str
