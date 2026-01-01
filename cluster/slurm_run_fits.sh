# Path: cluster/slurm_run_fits.sh
#!/bin/bash
#SBATCH --job-name=gb_fit_array
#SBATCH --output=slurm_logs/fit_%A_%a.out
#SBATCH --error=slurm_logs/fit_%A_%a.err
#SBATCH --time=24:00:00
#SBATCH --partition=compute
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --array=0-119%12

# Load modules and activate environment (adjust to your cluster)
module load python/3.10
module load openmpi   # if using MPI with CosmoMC
source ~/venv/bin/activate

# Path to the run_single_fit.py wrapper
RUN_SCRIPT="${PWD}/analysis/run_single_fit.py"

# Define parameter grids
KC_MIN=0.1
KC_MAX=2.0
KC_N=120   # total kc points
P_VALUES=(2.0 2.5)   # p grid
FOREGROUNDS=("baseline" "conservative" "minimal")
SEEDS=(0 1 2)

# Build full parameter list in the same order on all nodes
python - <<PY > /tmp/param_list_${SLURM_ARRAY_JOB_ID}.txt
import numpy as np
kc_vals = np.linspace(${KC_MIN}, ${KC_MAX}, ${KC_N})
p_vals = ${P_VALUES}
fgs = ${FOREGROUNDS}
seeds = ${SEEDS}
for kc in kc_vals:
    for p in p_vals:
        for fg in fgs:
            for s in seeds:
                print(f"{float(kc)} {float(p)} {fg} {int(s)}")
PY

# Determine which line this array task should process
LINE_INDEX=${SLURM_ARRAY_TASK_ID}
PARAM_LINE=$(sed -n "$((LINE_INDEX+1))p" /tmp/param_list_${SLURM_ARRAY_JOB_ID}.txt)

if [ -z "$PARAM_LINE" ]; then
  echo "No parameter line for array index ${SLURM_ARRAY_TASK_ID}"
  exit 1
fi

read KC P FG SEED <<< "$PARAM_LINE"
echo "Array task ${SLURM_ARRAY_TASK_ID} running kc=${KC} p=${P} fg=${FG} seed=${SEED}"

# Choose engine: cosmomc or montepython
ENGINE="cosmomc"

# Launch with MPI ranks equal to SLURM cpus-per-task
NP=${SLURM_CPUS_PER_TASK:-8}
srun --mpi=pmix_v3 -n ${NP} python ${RUN_SCRIPT} \
    --engine ${ENGINE} --kc ${KC} --p ${P} \
    --foreground ${FG} --seed ${SEED} \
    --outdir chains --nprocs ${NP}
