# import os
# import sys
from openai_client import generate_response, load_exercises_from_file, client, generate_chat_completion
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.responses import JSONResponse


# 🧠 Fuerza UTF-8 en todo el entorno
# os.environ["PYTHONIOENCODING"] = "utf-8"
# sys.stdout.reconfigure(encoding='utf-8')

# ✅ Verifica la codificación por consola
#print("Codificación por defecto:", sys.getdefaultencoding())

app = FastAPI()

def generate_routine(goal: str, experience: str = "principiante") -> str:
    """
    Generates a workout routine based on the user's goal and experience.

    Args:
        goal (str): The user's fitness goal (e.g., "strength", "weight loss").
        experience (str): The user's experience level (e.g., "beginner", "advanced").

    Returns:
        dict: A dictionary containing the generated routine.
    """
    try:
       # Construct the AI prompt
        prompt = (
            f"Eres un entrenador personal experto. Genera una rutina de ejercicios "
            f"para un usuario con el objetivo de '{goal}' y nivel de experiencia '{experience}'. "
            f"Incluye ejercicios específicos y una breve descripción para cada uno."
        )

        # Call the OpenAI API to generate the routine
        response = generate_chat_completion(
            messages=[
                {"role": "system", "content": "Eres un entrenador personal experto."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract the AI-generated response
        routine = response.choices[0].message.content.strip()
        return {"goal": goal, "experience": experience, "routine": routine}

    except Exception as e:
        # Raise an exception if the API call fails
        raise HTTPException(status_code=500, detail=f"Error generating routine: {str(e)}")





class RoutineRequest(BaseModel):
    goal: str
    experience: str = "principiante"

@app.get("/generate-routine")
def get_routine(goal: str, experience: str = "principiante"):
    """
    Endpoint para generar una rutina de entrenamiento.
    """
    try:
        routine = generate_routine(goal, experience)
        return {"routine": routine}
    except ValueError as e:
        raise HTTPException(status_code=500, detail="Error generating routine: " + str(e))


@app.post("/generate-routine/")
async def create_routine(request: RoutineRequest):
    """
    Endpoint para generar una rutina de entrenamiento.

    Args:
        request (RoutineRequest): Datos de entrada con el objetivo y nivel de experiencia.

    Returns:
        dict: Rutina generada o mensaje de error.
    """
    return generate_routine(request.goal, request.experience)


# Filter exercises by name
def get_exercise_by_name(name: str) -> dict:
    """
    Filters exercises by name.

    Args:
        name (str): The name of the exercise to search for.

    Returns:
        dict: The matching exercise details.

    Raises:
        HTTPException: If no exercise is found.
    """
    exercises = load_exercises_from_file()
    for exercise in exercises:
        if exercise["name"].lower() == name.lower():
            return exercise
    raise HTTPException(status_code=404, detail="Exercise not found.")

class ExerciseRequest(BaseModel):
    name: str

@app.post("/get-exercise/")
async def get_exercise(request: ExerciseRequest):
    """
    Endpoint to get exercise details by name.

    Args:
        request (ExerciseRequest): Input data with the exercise name.

    Returns:
        dict: The matching exercise details or an error message.
    """
    return get_exercise_by_name(request.name)


# se ejecuta solo cuanto corras el script directamente
# commad: python routine_generator.py        
if __name__ == "__main__":
    try:
        routine = generate_routine("ganar músculo", "principiante")

        if routine:
            with open("rutina.txt", "w", encoding="utf-8") as f:
                f.write(routine)
            print("✅ Rutina generada y guardada en rutina.txt")
        else:
            print("⚠️ No se generó rutina. Revisa error_log.txt")

    except Exception as e:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(str(e))
        safe_error = str(e).encode("utf-8", errors="replace").decode("utf-8")
        print("❌ Error. Detalles guardados en error_log.txt")
        print("Mensaje:", safe_error)

