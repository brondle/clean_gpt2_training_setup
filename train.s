#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --time=4:00:00
#SBATCH --mem=24GB
#SBATCH --job-name=TrainGPT-2-500steps
#SBATCH --mail-type=END
#SBATCH --mail-user=bb2906@nyu.edu
#SBATCH --output=slurm_%j.out

module purge
module load cudnn/10.0v7.4.2.24
module load cuda/10.0.130
module load anaconda3/5.3.0
cd ~
cd /scratch/bb2906/gpt_twitter_training
source activate ./env
python -u retrain.py -m="355M" -f=""
