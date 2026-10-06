from fastapi import FastAPI
from quote_engine.pipeline import run_pipeline

app=FastAPI(title='AI Construction Quote Engineering API',version='1.0.0')

@app.get('/health')
def health(): return {'status':'ok'}

@app.post('/v1/quotes/validate')
def validate(payload: dict): return run_pipeline(payload)
