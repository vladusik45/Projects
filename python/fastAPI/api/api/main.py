from fastapi import FastAPI
from users import router as users_router
from apartments import router as apartments_router

app = FastAPI(
    title="Apartments API",
    version="2.0"
)

app.include_router(users_router, prefix="/api")
app.include_router(apartments_router, prefix="/api")
