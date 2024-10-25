from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import logging

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/request/")
def request(name: str = Form(...),
            email: str = Form(...),
            theme: str = Form(...),
            phone: str = Form(...),
            comment: str = Form(...)
            ):
    logging.warning('Test message')

    return {"username": name, "email": email, "theme": theme, "phone": phone, "comment": comment}
