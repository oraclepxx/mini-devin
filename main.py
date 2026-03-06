from agent import DevAgent

with open("requirements.md") as f:
    requirements = f.read()

agent = DevAgent()

agent.build(requirements)