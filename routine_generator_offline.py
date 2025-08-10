import sys
import os

sys.stdout.reconfigure(encoding='utf-8')
os.environ["PYTHONIOENCODING"] = "utf-8"

print("Codificación por defecto:", sys.getdefaultencoding())

def generate_routine(goal: str, experience: str = "principiante") -> str:
    """
    Simula una rutina semanal de entrenamiento basada en el objetivo y nivel de experiencia.

    Args:
        goal (str): Objetivo de entrenamiento (ej. "ganar músculo").
        experience (str): Nivel de experiencia (ej. "principiante").

    Returns:
        str: Rutina generada en formato texto.
    """
    rutina = {
        "principiante": {
            "ganar músculo": [
                "Lunes: Sentadillas 3x12, Flexiones 3x10, Abdominales 3x15",
                "Martes: Descanso",
                "Miércoles: Peso muerto 3x10, Press militar 3x8, Planchas 3x30s",
                "Jueves: Descanso",
                "Viernes: Zancadas 3x12, Remo con mancuerna 3x10, Abdominales 3x15",
                "Sábado: Cardio ligero 20 min",
                "Domingo: Descanso"
            ],
            "perder grasa": [
                "Lunes: Cardio HIIT 20 min, Abdominales 3x20",
                "Martes: Sentadillas 3x15, Flexiones 3x12",
                "Miércoles: Cardio moderado 30 min",
                "Jueves: Zancadas 3x15, Planchas 3x45s",
                "Viernes: Cardio HIIT 20 min",
                "Sábado: Yoga o estiramientos",
                "Domingo: Descanso"
            ]
        },
        "intermedio": {
            "ganar músculo": [
                "Lunes: Sentadillas 4x10, Press banca 4x8, Abdominales 4x20",
                "Martes: Cardio moderado 20 min",
                "Miércoles: Peso muerto 4x8, Remo 4x10, Planchas 4x45s",
                "Jueves: Descanso",
                "Viernes: Zancadas 4x12, Press militar 4x8, Abdominales 4x20",
                "Sábado: Cardio intenso 25 min",
                "Domingo: Descanso"
            ]
        }
    }

    rutina_semanal = rutina.get(experience, {}).get(goal, ["Rutina no disponible para esos parámetros."])
    return "\n".join(rutina_semanal)

if __name__ == "__main__":
    try:
        routine = generate_routine("ganar músculo", "principiante")

        if routine:
            with open("rutina.txt", "w", encoding="utf-8") as f:
                f.write(routine)
            print("✅ Rutina generada y guardada en rutina.txt")
        else:
            print("⚠️ No se generó rutina.")
    except Exception as e:
        with open("error_log.txt", "w", encoding="utf-8") as f:
            f.write(str(e))
        safe_error = str(e).encode("utf-8", errors="replace").decode("utf-8")
        print("❌ Error. Detalles guardados en error_log.txt")
        print("Mensaje:", safe_error)
