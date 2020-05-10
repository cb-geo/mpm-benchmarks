import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())
# Read results as DF
df = pd.read_hdf('results/uniaxial-stress-2d-usf/particles09.h5', 'table')
# Maximum stress in yy and xx
syy = -0.9999999999999999
sxx = 0.0
# Check results are consistent
assert round(df['stress_yy'].max() - syy, 8) == 0.0
assert round(df['stress_xx'].max() - sxx, 8) == 0.0
