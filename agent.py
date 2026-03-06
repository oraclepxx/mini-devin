from skills.generate_design import generate_design
from skills.generate_code import generate_code
from skills.generate_tests import generate_tests
from skills.run_tests import run_tests
from skills.fix_bug import fix_bug

class DevAgent:

    def build(self, requirements):

        print("==> Generating design...")
        design = generate_design(requirements)
        print(design)

        print("\n==> Generating code...")
        generate_code(design)
        print("Code written to workspace/app/app.py")

        print("\n==> Generating tests...")
        generate_tests(requirements)
        print("Tests written to workspace/test_app.py")

        for i in range(5):

            print(f"\n==> Running tests (attempt {i + 1}/5)...")
            result = run_tests()
            print(result["output"])

            if result["success"]:
                print("✓ Tests passed!")
                return

            print(f"✗ Tests failed. Fixing bug...")

            with open("workspace/app/app.py") as f:
                code = f.read()

            fixed = fix_bug(result["output"], code)

            with open("workspace/app/app.py", "w") as f:
                f.write(fixed)
            print("Code updated.")

        print("Max iterations reached without passing tests.")
