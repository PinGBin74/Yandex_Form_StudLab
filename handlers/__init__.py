from handlers.form import router as FormRouter
from handlers.auth import router as AuthRouter
from handlers.user import router as UserRouter

routers = [FormRouter, AuthRouter, UserRouter]
