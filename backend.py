from fastapi import FastAPI, HTTPException
import openai

# Initialize FastAPI app
app = FastAPI()

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

@app.post("/generate-routine/")
async def generate_routine():
    """
    Endpoint to generate a gym routine using OpenAI's API.
    """
    try:
        # Call OpenAI API to generate the routine
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use "gpt-4" if you have access
            messages=[
                {"role": "system", "content": "You are a gym routine generator."},
                {"role": "user", "content": "Generate a gym routine"}
            ],
            max_tokens=100
        )

        # Extract and return the generated routine
        routine = response["choices"][0]["message"]["content"].strip()
        return {"routine": routine}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating routine: {str(e)}")