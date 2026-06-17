import subprocess

notebooks = [
    "Loading.ipynb",
    "Preprocessing.ipynb",
    "Training.ipynb",
    "Testing.ipynb",
    "Evaluation.ipynb"
]

for notebook in notebooks:
    print(f"Running {notebook}...")
    subprocess.run(
        ["jupyter", "nbconvert", "--to", "notebook", "--execute", notebook],
        check=True
    )

print("All files ran successfully!")
