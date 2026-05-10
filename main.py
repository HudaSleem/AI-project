import os

print("Running Loading...")
os.system("jupyter nbconvert --to notebook --execute Loading.ipynb")

print("Running Preprocessing...")
os.system("jupyter nbconvert --to notebook --execute Preprocessing.ipynb")

print("Running Training...")
os.system("jupyter nbconvert --to notebook --execute Training.ipynb")

print("Running Evaluation...")
os.system("jupyter nbconvert --to notebook --execute Evaluation.ipynb")

print("Done")
