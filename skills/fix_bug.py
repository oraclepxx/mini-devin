from llm import ask_llm

def fix_bug(error_log, code):

    prompt = f"""
    The tests failed.

    Error log:
    {error_log}

    Current code:
    {code}

    Fix the code.
    Return corrected version.
    """

    return ask_llm(prompt)