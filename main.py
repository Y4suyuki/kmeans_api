from fastapi import FastAPI

from pydantic import BaseModel, Field, validator

import pandas as pd
from sklearn.cluster import KMeans


class TrainingSet(BaseModel):
    X: list[list[int]]
    k: int = Field(
        ..., gt=0, lt=10, description="number of clusters"
    )

    @validator('X')
    def check_size(cls, v):
        if len(v) < 2:
            raise Exception("too few data points")
        elif len(v) > 100:
            raise Exception("datapoints exceeds max size 100")

        return v


app = FastAPI()


@app.post("/kmeans")
async def kmean(ts: TrainingSet):
    X = pd.DataFrame(ts.X).values
    kmeans = KMeans(n_clusters=ts.k, random_state=0).fit(X)
    labels = kmeans.labels_
    
    return labels.tolist()


@app.get("/")
async def root():
    return {"message": "Hello World"}
