# project_1
Fintech Bootcamp Project 1

# How to set up the Google Earth Engine

### 1) Setup a new GE environment.

```shell
conda create -n geenv python=3.7 anaconda -y

conda activate geenv

```
### 2) We need to install some libraries

```shell
conda install mamba -c conda-forge

mamba install geemap -c conda-forge

mamba install jupyter_contrib_nbextensions -c conda-forge

```

### 3) And Finally run Jupyter Notebook

```shell
jupyter notebook
```
