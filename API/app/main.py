from fastapi import FastAPI

from API.app.routes.student_routes import router as student_router


app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "API de alunos funcionando"
    }


app.include_router(student_router)