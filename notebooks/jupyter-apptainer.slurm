#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00:00
#SBATCH --cpus-per-task=4
#SBATCH --partition=normal 

node=`hostname -s`
port=`shuf -i 8400-9400 -n 1`
if [ -z ${lport:+x} ]; then lport="8889" ; else lport=${lport}; fi

echo "Run the following on your local machine: "
echo "ssh -i /path/to/private/ssh/key -N -L ${lport}:${node}:${port} ${USER}@spider.surf.nl"

cd ${HOME}

apptainer exec \
  oras://ghcr.io/MotionbyLearning/stm-dashboard:latest \
  jupyter lab --no-browser --port=${port} --ip=0.0.0.0
