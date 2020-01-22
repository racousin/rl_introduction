# rl_introduction

### Install requirement


if you use Ubuntu
```bash
sudo apt-get update && sudo apt-get install libopenmpi-dev
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
Be sure to be in python 3.6.9

```bash
pip3 install virtualenv
```

Create a virtual environment:

```bash
virtualenv venv
source venv/bin/activate
```

Update and install requirements
```bash
pip install -r requirements.txt
```

Test install
```bash
cd src/
python moon.py
```

### Learn and train

```bash
jupyter notebooks
```

### Run and display

```bash
cd src/
```

let file name empty for random of fill with save algorithm
for cart
```bash
python cart.py file_name
```

for mountain
```bash
python mountain.py file_name
```

for moon landing
```bash
python moon.py file_name
```

for pretrain moon landing
```bash
python moon.py lander
```
### Read

- **Model-free** ([introduction_to_rl](introduction_to_rl.pdf))
