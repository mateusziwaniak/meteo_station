from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/temperature")
async def get_temperature():
    return 20

@router.get("/humidity")
async def get_humidity():
    return 50