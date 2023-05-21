import json
from fastapi import FastAPI
from property_db import PropertyRepository
from scraper import scrape_search
from property import PropertyEncoder


from pydantic import BaseModel


class SearchId(BaseModel):
    search_id: str

class Pagination(BaseModel):
    page: int
    size: int

app = FastAPI()

@app.post("/paginated-properties")
def get_paginated_properties(pagination: Pagination):
    repository = PropertyRepository('./database/db.sqlite3')
    properties = repository.get_properties_with_pagination(pagination.page, pagination.size)
    return json.loads(json.dumps(properties, cls=PropertyEncoder))

@app.get("/properties")
def get_properties():
    repository = PropertyRepository('./database/db.sqlite3')
    properties = repository.get_properties()
    return json.loads(json.dumps(properties, cls=PropertyEncoder))


@app.post("/scrape")
def scrape(search_id: SearchId):
    repository = PropertyRepository('./database/db.sqlite3')
    properties = scrape_search(search_id=search_id.search_id)
    repository.save_properties(properties=properties)
    return {"message": "Scrape successful"}


if __name__ == "__main__":
    app.run(debug=True)