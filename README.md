# Routine Generator API

A FastAPI-based application that uses OpenAI's GPT-4 model to generate personalized workout routines based on user goals and experience levels.

![WhatsApp Image 2025-08-09 at 5 48 20 PM](https://github.com/user-attachments/assets/02fc83b3-5785-47ac-bb19-4a6a8c575863)
![WhatsApp Image 2025-08-09 at 5 49 12 PM](https://github.com/user-attachments/assets/a092febf-e567-4b79-a8e4-905bec41af91)
![WhatsApp Image 2025-08-09 at 5 49 53 PM](https://github.com/user-attachments/assets/a8f11e22-d260-4144-a33b-03170638679a)

## Features

- Generates workout routines tailored to user goals (e.g., weight loss, strength training).
- Supports different experience levels (e.g., beginner, intermediate, advanced).
- Leverages OpenAI's GPT-4 model for intelligent and detailed responses.
- Get exercise from a Database (e.g., Pierna, Abdomen, Pecho)

## Requirements

- Python 3.8 or higher
- OpenAI Python library (`openai`)
- FastAPI (`fastapi`)
- Uvicorn (`uvicorn`)

## Installation

1. Clone the repository:
```bash
   git clone https://github.com/your-username/routine-generator.git
   cd routine-generator
   ```

2. Create a virtual environment and activate it:
```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key as an environment variable: bash export OPENAI_API_KEY=your_openai_api_key Or replace your_openai_api_key directly in the code.


Usage
1. Start the FastAPI server:
```bash
   uvicorn routine_generator:app --reload
   ```

2. Access the API documentation at:
```bash
   http://127.0.0.1:8000/docs
   ```

3. Use the /generate-routine endpoint to generate a workout routine. Example request:
```bash
   {
    "goal": "weight loss",
    "experience": "beginner"
    }
   ```

Example Response
```bash
    {
        "goal": "weight loss",
        "experience": "beginner",
        "routine": "1. Warm-up: 5 minutes of light jogging...\n2. Strength training: 3 sets of squats..."
    }
```

Project Structure
routine-generator/
├── routine_generator.py  # Main application code
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation


Dependencies
OpenAI Python Library
FastAPI
Uvicorn
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
OpenAI for providing the GPT-4 model.
FastAPI for the web framework.
```






