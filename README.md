# Weeks 14 and 15 Lecture Exercises

This repository contains lecture exercises for Weeks 14 and 15 of Chem 274A.
Complete each Python exercise and push your work to GitHub. Every exercise is
autograded when you push. Detailed instructions are in each exercise's `main.py`.

## Making an environment

Use a Python environment with `pytest`, `numpy`, `pandas`, and `matplotlib`
installed. If you need to make an environment, create and activate one with:

```bash
conda create --name chem274a conda-forge::python
conda activate chem274a
conda install conda-forge::pytest conda-forge::numpy conda-forge::pandas conda-forge::matplotlib
```

The environment is active when `(chem274a)` appears at the beginning of your
terminal prompt. Run `conda deactivate` when you are finished working.

## Run the tests locally

Check individual exercises with:

```bash
python -m pytest -q
python -m pytest -q -k test_01numpy01
python -m pytest -q -k test_01numpy02
python -m pytest -q -k test_01numpy03
python -m pytest -q -k test_02pandas01
python -m pytest -q -k test_02pandas02
python -m pytest -q -k test_02pandas03
python -m pytest -q -k test_02pandas04
python -m pytest -q -k test_02pandas05
python -m pytest -q -k test_03matplotlib01
python -m pytest -q -k test_03matplotlib02
```

Plot tests run without opening a graphical window.

## Submit your work

Review your changes, commit them, and push your branch to GitHub. The
autograding workflow shows your points in its summary and uploads
`grading-results.json` as an artifact. If a test passes locally but fails on
GitHub, confirm that you committed and pushed the latest exercise files.
