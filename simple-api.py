from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware

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
def request(name: str = Form(...), email: str = Form(...), theme: str = Form(...), phone: str = Form(...), comment: str = Form(...)):
    return {"username": name, "email": email, "theme": theme, "phone": phone, "comment": comment}
