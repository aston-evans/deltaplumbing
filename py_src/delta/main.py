from delta.db import app
from delta.routes import router

app.include_router(router)
