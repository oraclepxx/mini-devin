from llm import ask_llm

def generate_tests(requirements):

    prompt = f"""
    Write pytest tests for this app.

    Requirements:
    {requirements}
    """

    tests = ask_llm(prompt)

    with open("workspace/test_app.py", "w") as f:
        f.write(tests)