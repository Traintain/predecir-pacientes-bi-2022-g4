from datetime import date
from typing import List, Optional
from fastapi import FastAPI
from DataModel import *
from joblib import load
import pandas as pd
from PreProcess import TextPreprocessing

# Librerías para manejo de datos
import pandas as pd
pd.set_option('display.max_columns', 25) # Número máximo de columnas a mostrar
pd.set_option('display.max_rows', 50) # Numero máximo de filas a mostar
import numpy as np
np.random.seed(3301)

# Regresion lineal
from sklearn.linear_model import LinearRegression

# Metricas
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_squared_error, r2_score

app = FastAPI()


@app.get("/")
def read_root():
   return {"Hello": "World"}



@app.get("/results/{date}")
def read_item(date: date, q: Optional[str] = None):
   return {"item_id": date, "q": q}

@app.post("/process")
def make_predictions(dataModel: List[DataModel]):
    #print(dataModel)
    data = pd.DataFrame(dataModel[0].dict(), columns=dataModel[0].dict().keys(), index=[0])
    data.columns = dataModel[0].columns()
    for i in range(1, len(dataModel)):
      temp = dataModel[i]
      temp_el = pd.DataFrame(temp.dict(), columns=temp.dict().keys(), index=[i]) 
      temp_el.columns = temp.columns()
      data = data.append(temp_el)
    model = load("assets/pipeline.joblib")
    result = model.predict(data)
    return result





