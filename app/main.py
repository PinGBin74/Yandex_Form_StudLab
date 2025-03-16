from fastapi import FastAPI
from app.user.user_profile.handlers import router as user_router
from app.user.auth.handlers import router as auth_router
from app.form.handlers import router as form_router
from fastapi.responses import ORJSONResponse
app = FastAPI(default_response_class=ORJSONResponse)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(form_router)
