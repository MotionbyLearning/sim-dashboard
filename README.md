# STM Dashboard

## Introduction

This repository includes some experimental work to setup a dasboard to visualize space-time matrix (STM) datasets.

## Installation

Create python environment using `conda` (or its faster implementation `mamba`):

```shell
mamba env create -f environment.yml
mamba activate mobyle
```

Download and extract the test dataset (direct download [link](https://figshare.com/ndownloader/files/41957250)):

```shell
mkdir data
wget -P data --content-disposition https://figshare.com/ndownloader/files/41957250
unzip -d data data/stm.zarr.zip
```

## Running

Start the dashboard:

```shell
python stm-dashboard.py --stm-path data/stm.zarr 
```

