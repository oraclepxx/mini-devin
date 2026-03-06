from skills.generate_design import generate_design
from skills.generate_code import generate_code
from skills.generate_tests import generate_tests
from skills.run_tests import run_tests
from skills.fix_bug import fix_bug

class DevAgent:

    def build(self, requirements):

        design = generate_design(requirements)

        generate_code(design)

        generate_tests(requirements)

        for i in range(5):

            result = run_tests()

            if result["success"]:
                print("Tests passed")
                return

            print("Tests failed, fixing...")

            with open("workspace/app/app.py") as f:
                code = f.read()

            fixed = fix_bug(result["output"], code)

            with open("workspace/app/app.py", "w") as f:
                f.write(fixed)

        print("Max iterations reached")