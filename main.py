# -*- coding: utf-8 -*-
"""main

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1NgHmwS8WxJ4J3T-8FoOsp0vmMqFKbukW
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Render + FastAPI!"}