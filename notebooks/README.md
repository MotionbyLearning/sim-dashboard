# Notebooks

## Run on Spider

You can start a Jupyter Lab session on Spider in one of the following ways:

1. Using a conda-based installation.
2. Using an apptainer container.

We have observed long waiting times for the Jupyter kernel to start and for importing libraries when using the first
approach. This is because conda installations typically involve a large number of small files, which do not play well with
the filesystems of HPC systems (see also the [Spider docs](https://spiderdocs.readthedocs.io/en/latest/Pages/storage_on_spider.html#internal-storage)).
The use of apptainer bypasses this issue. However, Dask JobQueue, which can be used to create (multi-node) Dask clusters
beyond a given SLURM allocation, currently does not work with the apptainer-based approach (standard "local" clusters 
can still be created within the requested SLURM allocation). 

### 1. Using a conda-based installation

* Create a Python environment with all the dependencies (see [here](../README.md#conda));
* Submit the SLURM job script [`jupyter-conda.slurm`](./jupyter-conda.slurm), modifying parameters as appropriate (remove options for 
  default values):
  ```shell
  # 10 hours, 4 cores
  sbatch --time=10:00:00 --cpus-per-task=4 jupyter-conda.slurm
  ```

### 2. Using an apptainer container.

* Submit the SLURM job script [`jupyter-apptainer.slurm`](./jupyter-apptainer.slurm), modifying parameters as appropriate (remove options for  
  default values):
  ```shell
  # 10 hours, 4 cores
  sbatch --time=10:00:00 --cpus-per-task=4 jupyter-apptainer.slurm
  ```

## Port forwarding & access

* In order to access the session, run the command printed in the SLURM output file **on your local machine** (note, the 
  command does not produce any output, and the shell with hang):
  ```shell
  # ON SPIDER: print SLURM output
  cat slurm-<JOBID>.out
  ```
  ```shell
  # ON YOUR LOCAL MACHINE: run the command in the SLURM output
  ssh -i /path/to/private/ssh/key -N -L 8889:<HOSTNAME>:<PORT> <USERNAME>@spider.surf.nl
  ```
* You can access JupyterLab using a web browser at: http://localhost:8889/lab
