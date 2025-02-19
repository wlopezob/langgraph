### Install miniconda
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# activate conda
source ~/miniconda3/bin/activate
conda init

# Verify installation
conda --version
```

### Create environment from scratch
```bash
conda create -n mygraph python=3.11
conda activate mygraph
conda install -c conda-forge poetry
conda env export --from-history > environment.yml
```

### remove environment conda
```bash
conda deactivate
conda env remove -n mygraph
```

### Create environment from environment.yml
```bash
conda env create -f environment.yml
conda activate mygraph
```
# Import activate env on vscode

### init project
```bash
poetry init

#then configure pyproject.tom execute
poetry install
```

### execute langgraph on dev
```bash
langgraph dev
```

### execute fastapi on dev
```bash
fastapi dev app/api.py
```
