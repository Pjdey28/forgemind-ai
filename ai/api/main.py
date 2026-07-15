from fastapi import FastAPI

from api.routes.upload import router as upload_router

from api.routes.query import router as query_router

from api.routes.health import router as health_router


app = FastAPI(

    title="IndustrialBrain AI"

)

app.include_router(upload_router)

app.include_router(query_router)

app.include_router(health_router)