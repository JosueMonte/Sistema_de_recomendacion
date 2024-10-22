from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Bienvenido a la API"}

@app.get('/endpoint1')
def endpoint1():
    return {"message": "Este es el endpoint 1"}

@app.get('/endpoint2')
def endpoint2():
    return {"message": "Este es el endpoint 2"}

@app.get('/endpoint3')
def endpoint3():
    return {"message": "Este es el endpoint 3"}

@app.get('/endpoint4')
def endpoint4():
    return {"message": "Este es el endpoint 4"}

@app.get('/endpoint5')
def endpoint5():
    return {"message": "Este es el endpoint 5"}

@app.get('/endpoint6')
def endpoint6():
    return {"message": "Este es el endpoint 6"}



