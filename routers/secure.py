from fastapi import APIRouter, Depends
from auth import get_user, get_historical_data

router = APIRouter()

@router.get("/")
async def get_testroute(user: dict = Depends(get_user)):
    return user

@router.get("/get_historical_prices")
async def get_historicalprices(historical_prices: dict = Depends(get_historical_data)):
    return historical_prices