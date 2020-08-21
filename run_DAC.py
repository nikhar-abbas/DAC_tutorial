'''
A script to showcase the DAC functionalities of WISDEM

NOTE: As long as no optimization flags are set to "True" in analysis_options.yaml, no optimization
      will be done. 
'''
import os
import wisdem
import os
import matplotlib.pyplot as plt
import glob
from wisdem.glue_code.runWISDEM import run_wisdem
from wisdem.aeroelasticse.Util import ReadFASTout
from ROSCO_toolbox.utilities import FAST_IO, FAST_Plots
fio = FAST_IO()
fpl = FAST_Plots()

## File management
run_dir = os.path.dirname( os.path.realpath(__file__) )
fname_wt_input         = os.path.join(run_dir,"BAR10.yaml") 
fname_modeling_options = os.path.join(run_dir,"modeling_options.yaml")
fname_analysis_options = os.path.join(run_dir,"analysis_options.yaml")

# Run WISDEM to generate and run openfast model
wt_opt, modeling_options, opt_options = run_wisdem(fname_wt_input, fname_modeling_options, fname_analysis_options)

# Load OpenFAST output
fast_output_files = [os.path.join(os.path.dirname(os.path.realpath(__file__)), 'BAR_00', 'OpenFAST_BAR_00.outb')]
fast_output_files += glob.glob(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'BAR_00_dac', '*.outb'))

fast_out = fio.load_FAST_out(fast_output_files, tmin=50)

plot_cases = {}
plot_cases['Baseline'] = ['Wind1VelX', 'BldPitch1', 'RotSpeed', 'GenPwr','BLFLAP1', 'RootMyb1']

fpl.plot_fast_out(plot_cases, fast_out, showplot='True')
plt.tight_layout()