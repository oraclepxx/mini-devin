import anthropic

client = anthropic.Anthropic()

def ask_llm(prompt):

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=8096,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.content[0].text
