from llm import ask_llm
import os

def generate_code(design):

    prompt = f"""
    Based on this design generate Python code.

    {design}

    Use FastAPI.

    Output full files.
    """

    code = ask_llm(prompt)

    os.makedirs("workspace/app", exist_ok=True)

    with open("workspace/app/app.py", "w") as f:
        f.write(code)