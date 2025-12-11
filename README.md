# MTG Analysis

<!-- Describe the project --->

## Setup

Create and activate a virtual environment:

```
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```
python -m pip install -r requirements.txt
```

## Notebook Workflow

Generate the notebook:

```
jupytext --to notebook notebook/notebook.py
```

Sync `.ipynb` and `.py` files:

```
jupytext --set-formats ipynb,py notebook/notebook.ipynb
```

## Run

Start Jupyter Notebook:

```
jupyter notebook notebook/notebook.ipynb
```

## Resources

https://scryfall.com
