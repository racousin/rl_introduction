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
Be sure to be in python 3.10

```bash
pyenv install 3.10
pip install virtualenv
```
### Clone
```
git clone https://github.com/racousin/rl_introduction.git
```
Create a virtual environment:

```bash
cd _rl_introduction
~/.pyenv/versions/3.10/bin/python -m venv venv
source venv/bin/activate
```

Update and install requirements
```bash
pip install -r requirements.txt
pip install -e .
```
If you also want to play with mujoco. Follow https://github.com/openai/mujoco-py and
Update and install requirements
```bash
pip install -r requirements_mujoco.txt
pip install -e .
```

### Run with docker
install docker https://docs.docker.com/engine/install/ubuntu/

```
docker build -t rl_intro .
docker run -t -p 8888:8888 --name  rl_intro -v ${PWD}/notebooks:/app/notebooks rl_intro 

```
Go on brother http://localhost:8888/
And use the copy the token from your terminal

### Learn and train

```bash
jupyter notebook notebooks
```
### Read

- **Model-free** ([introduction_to_rl](introduction_to_rl.pdf))



