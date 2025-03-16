from fastapi import FastAPI, Request
import time

from routes import weather_routes

app = FastAPI(title="Meteo API", version="1.0")

app.include_router(weather_routes.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"{request.method} {request.url} - {process_time:.2f}s")
    return response


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)

