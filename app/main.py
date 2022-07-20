from fastapi import FastAPI
from fastapi.responses import JSONResponse
from es import search_by_email, create_doc
from schema import Document
from typing import List
app = FastAPI()


@app.get('/row/{email}/')
def get_row(email):
    res = search_by_email(email, 'index-2')
    return JSONResponse(content=res, status_code=200)


@app.post('/row/', response_model=List[Document])
def create_row(doc: Document):
    res = create_doc(doc, 'index-2')
    return JSONResponse(content=res, status_code=200)
