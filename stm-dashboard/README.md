# STM Dashboard - minimal example

Setup a minimal dashboard to visualize STM data.

## Data

Download and extract the test dataset (direct download [link](https://figshare.com/ndownloader/files/41957250)):

```shell
mkdir data
wget -P data --content-disposition https://figshare.com/ndownloader/files/41957250
unzip -d data data/stm.zarr.zip
```

## Running

After having create the environment (see [here](../README.md)), start the dashboard:

```shell
conda activate mobyle
python stm-dashboard.py --stm-path data/stm.zarr 
```


