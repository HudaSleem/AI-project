import os

def run_notebook(name):
    print(f"Running {name}...")
    os.system(f"jupyter nbconvert --to notebook --execute {name}.ipynb")

run_notebook("Loading")
run_notebook("Preprocessing")
run_notebook("Training")
run_notebook("Evaluation")

print("Pipeline completed successfully!")
