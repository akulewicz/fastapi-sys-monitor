from fastapi import FastAPI, status
from services import cpuservice

app = FastAPI()

@app.get("/cpu", status_code=status.HTTP_200_OK)
async def get_cpu_temp():
    cpu_temp = cpuservice.get_cpu_temp()
    return {"cpu_temp": cpu_temp}