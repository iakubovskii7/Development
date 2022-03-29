from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="")

app = FastAPI()


@app.get("/")
def hello_jinja(request: Request):
    data = "Hello, jinja!"
    return templates.TemplateResponse("jinja2_trainer.html",
                                      {"request": request, "data": data})
