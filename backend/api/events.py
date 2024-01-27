from datetime import date
import json
from fastapi import APIRouter
from pydantic import BaseModel


class Events(BaseModel):
    name: str
    event: str
    image: str
    date: str
    description: str


router = APIRouter(
    prefix="/api/events",
    tags=["events"],
    responses={404: {"description": "Not found"}},
)


@router.get("/allevents")
async def get_events():
    fakeEvents = [
        {
        }
    ]
    json_data = json.dumps(fakeEvents)
    return json.loads(json_data)
