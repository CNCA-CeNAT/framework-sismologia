#!/opt/intel/intelpython35/bin/python3

#PBS -N tremor_python
#PBS -q phi-n6h96
#PBS -l nodes=6:ppn=64
#PBS -l walltime=48:00:00 

import modules
import sys

modules.load('intelpython/3.5')

path = '/home/gmocornejos/computational_seismology/LP-location/'

exe = path + 'tremor_location.py'
conf = path + 'location.conf'

try:
    configuration = sys.argv[1]
except IndexError:
    raise SystemExit('configuration no specified at command line')

modules.run('time mpirun python ' + exe + ' ' + conf + ' ' + sys.argv[1])


