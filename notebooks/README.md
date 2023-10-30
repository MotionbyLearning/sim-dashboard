# Notebooks

## Run on Spider

In order to start a Jupyter Lab session on Spider: 

* Create a Python environment with all the dependencies (see [here](../README.md));
* Submit the [SLURM job script](./jupyter_on_spider.bsh), modifying parameters as appropriate (remove options for 
  default values):
  ```shell
  # 10 hours, 4 cores
  sbatch --time=10:00:00 --cpus-per-task=4 jupyter_on_spider.bsh
  ```
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
* Access JupyterLab using a web browser at: https://localhost:8889/lab