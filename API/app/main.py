from fastapi import FastAPI

from .routes.student_routes import router
from .db.database import engine
from .db.models import Base


app = FastAPI()


@app.on_event("startup")
def startup():

    Base.metadata.create_all(
        bind=engine
    )


app.include_router(router)