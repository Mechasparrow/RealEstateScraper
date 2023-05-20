import json
from fastapi import FastAPI
from property_db import PropertyRepository
from property import PropertyEncoder

app = FastAPI()

@app.get("/properties")
def get_properties():
    repository = PropertyRepository('./database/db.sqlite3')
    properties = repository.get_properties()
    return json.loads(json.dumps(properties, cls=PropertyEncoder))


if __name__ == "__main__":
    app.run(debug=True)