import uvicorn
from fastapi import FastAPI

from src.endpoints.routers import routers


app = FastAPI()
app.include_router(routers)


if __name__ == '__main__':
    uvicorn.run("src.entrypoint:app", reload=True, host="localhost", port=8000)
