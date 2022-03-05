# rl_introduction

## Run in colab
<a href="https://colab.research.google.com/github/racousin/rl_introduction/blob/master/notebooks/main.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
## Run locally

### Install requirement


if you use Ubuntu
```bash
sudo apt-get update && sudo apt-get install libopenmpi-dev python3-dev zlib1g-dev
```

if you use mac OS X
```bash
brew install openmpi
```

if you use windows
```bash
Install Ubuntu!
```

### Setup your python environment
Be sure to be in python 3.6.5

```bash
pyenv install 3.6.5
pip3 install virtualenv
```
### Clone
```
git clone https://github.com/racousin/rl_introduction.git
```
Create a virtual environment:

```bash
cd rl_introduction
virtualenv venv -p ~/.pyenv/versions/3.6.5/bin/python
source venv/bin/activate
```

Update and install requirements
```bash
pip install -r requirments.txt 
pip install -e .
```

### Learn and train

```bash
jupyter notebook notebooks
```
### Read

- **Model-free** ([introduction_to_rl](introduction_to_rl.pdf))



