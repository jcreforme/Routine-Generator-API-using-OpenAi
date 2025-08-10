from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from routine_generator import generate_routine

app = FastAPI()

@app.get("/generate-routine")
def get_routine(goal: str = Query(...), experience: str = Query("principiante")):
    try:
        # Ensure the inputs and outputs are properly handled as UTF-8
        routine = generate_routine(goal, experience)
        return JSONResponse(content={"routine": routine}, media_type="application/json")
    except UnicodeEncodeError as e:
        return JSONResponse(content={"error": f"Encoding error: {str(e)}"}, media_type="application/json")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, media_type="application/json")