from fastapi import FastAPI
from routes import location_data

app = FastAPI(
    title="Location Data API",
    description="API for retrieving countries, states (Nigeria), and Local Government Areas (LGAs).",
    version="1.0.0",
)

app.include_router(location_data.router, prefix="/api/v1/location", tags=["Location Data"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Location Data API! Visit /docs for API documentation."}