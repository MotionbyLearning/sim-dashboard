# STM Dashboard

## Introduction

This repository includes some experimental work on the visualization of space-time matrix (STM) datasets.

## Repository structure

* [`stm-dashboard`](./stm-dashboard): A minimal dashboard implementation based on panel to visualize an example STM 
  dataset.
* [`notebooks`](./notebooks):
  * [`stm-and-contextual-data.ipynb`](./notebooks/stm-and-contextual-data.ipynb): Visualize an STM dataset together with 
    some contextual data (space- and time-dependent). 

## Installation

### Conda

The `environment.yml`[./environment.yml] file allows you to create a Python environment with all the required 
dependencies using `conda` (or its faster implementation `mamba`):

```shell
mamba env create -f environment.yml
```

### Apptainer

We also provide an Apptainer (formerly known as Singularity) image with the environment already setup. Images are built
using GitHub Actions for every release and pushed to the GitHub Container Registry. Start the Python REPL in a container
using:

```shell
singularity exec \
  oras://ghcr.io/MotionbyLearning/stm-dashboard:latest \
  python
```
