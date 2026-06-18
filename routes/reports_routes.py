from fastapi import APIRouter
from fastapi import  HTTPException
import uvicorn
from pydantic import BaseModel
from typing import Literal,Optional
from database.db_connection import DbConnection
router=APIRouter()