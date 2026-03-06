from llm import ask_llm

def generate_design(requirements):

    prompt = f"""
    Read the requirements and design the system.

    Requirements:
    {requirements}

    Output:
    - architecture
    - files
    """

    return ask_llm(prompt)