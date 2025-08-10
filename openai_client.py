from openai import OpenAI
import os
from dotenv import load_dotenv
import json
load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))



def load_exercises_from_file(filename="exercises.json"):
    """
    Loads exercises from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        list: A list of exercises with their details.
    """
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        raise Exception(f"File '{filename}' not found.")
    except json.JSONDecodeError:
        raise Exception(f"File '{filename}' is not a valid JSON file.")

def generate_response(prompt, model="gpt-4"):
    """
    Filters exercises by name.

    Args:
        name (str): The name of the exercise to search for.

    Returns:
        dict: The matching exercise details.

    Raises:
        HTTPException: If no exercise is found.
    """
    # Load exercises from the JSON file
    exercises = load_exercises_from_file()
    exercise_list = "\n".join([f"- {ex['name']}: {ex['description']}" for ex in exercises])

    # Construct the full prompt with exercises included
    full_prompt = (
        f"{prompt}\n\n"
        f"Here is a list of exercises you can use:\n{exercise_list}"
    )
    try:
        # Call the OpenAI API with the constructed prompt
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "Eres un entrenador personal experto."},
                {"role": "user", "content": full_prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        # Raise an exception if the API call fails
        raise Exception(f"OpenAI API error: {str(e)}")


def generate_chat_completion(messages, model="gpt-4"):
    """
    Calls the OpenAI ChatCompletion API.

    Args:
        messages (list): List of message dicts for the chat.
        model (str): Model name.

    Returns:
        str: The generated response content.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response
    except Exception as e:
        raise Exception(f"OpenAI API error: {str(e)}")
    

if __name__ == "__main__":
    # Example usage
    user_prompt = "Quiero un plan de entrenamiento para principiantes."
    try:
        response = generate_response(user_prompt)
        print("Generated Response:")
        print(response)
    except Exception as e:
        print(f"Error: {e}")