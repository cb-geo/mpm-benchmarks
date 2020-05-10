import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Test location of particles
df0 = pd.read_hdf('results/boundary_inclined_friction/particles-0_4-099000.h5', 'table')
df1 = pd.read_hdf('results/boundary_inclined_friction/particles-1_4-099000.h5', 'table')
df2 = pd.read_hdf('results/boundary_inclined_friction/particles-2_4-099000.h5', 'table')
df3 = pd.read_hdf('results/boundary_inclined_friction/particles-3_4-099000.h5', 'table')
df = df0
df.append(df1)
df.append(df2)
df.append(df3)

## Assert location of particles
assert round(df['coord_x'].min() - 3.177497667722451, 8) == 0.0
assert round(df['coord_x'].max() - 4.008388126337369, 8) == 0.0
assert round(df['coord_y'].min() - (-1.8296901482239594), 8) == 0.0
assert round(df['coord_y'].max() - (-1.2655507481267576), 8) == 0.0
