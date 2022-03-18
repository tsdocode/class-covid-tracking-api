from fastapi import FastAPI

from server.routes.student import router as StudentRoutes
from server.routes.positive import router as PositiveRoutes





from starlette.middleware.cors import CORSMiddleware


app = FastAPI()



app.include_router(StudentRoutes, tags=["student"], prefix="/student")
app.include_router(PositiveRoutes, tags=["positive"], prefix="/positive")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["POST","PUT","DELETE", "OPTION", "GET"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": " API for covid app "}

