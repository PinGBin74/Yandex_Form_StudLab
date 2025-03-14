from fastapi import FastAPI
from handlers.user import router as user_router
from handlers.auth import router as auth_router
from handlers.form import router as form_router
from fastapi.responses import ORJSONResponse
app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(form_router)
