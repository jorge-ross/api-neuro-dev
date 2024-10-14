from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estas direcciones
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],   # Permitir todos los encabezados
)

app.mount("/images", StaticFiles(directory="images"), name="images")


class PsychService(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    image_url: str


psych_services = [
    PsychService(
        id=1,
        title="Terapia Individual",
        description="Enfoque terapéutico que ayuda a identificar y cambiar patrones de pensamiento y comportamiento negativos.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=2,
        title="De pareja",
        description="Sesiones de terapia para mejorar la comunicación y resolver conflictos en relaciones de pareja.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=3,
        title="Evaluaciones",
        description="Evaluación exhaustiva de las funciones cognitivas para diagnosticar trastornos neurológicos o del desarrollo.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=4,
        title="Rehabilitación",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=5,
        title="Corporativo",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=6,
        title="Técnicas de estudio",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=7,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=8,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=9,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=10,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=12,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    ),
    PsychService(
        id=12,
        title="Orientación Psicológica",
        description="Programa de ejercicios mentales para mejorar la memoria, atención y otras funciones cognitivas después de una lesión cerebral.",
        image_url="/images/logond.png"
    )
]


@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de servicios psicológicos y neuropsicológicos"}


@app.get("/services", response_model=List[PsychService])
async def get_services():
    return psych_services


@app.get("/services/{service_id}", response_model=PsychService)
async def get_service(service_id: int):
    service = next(
        (service for service in psych_services if service.id == service_id), None)
    if service is None:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return service

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
