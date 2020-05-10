import os
import pathlib
import pandas as pd
# Get current path
os.chdir(pathlib.Path(__file__).parent.absolute())

# Nodal forces results
## Step 300
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0300.h5', 'table')
assert round(df['stress_xx'].min() - 0.5925210678182377, 8) == 0.0
assert round(df['stress_xx'].max() - 0.5974539476363379, 8) == 0.0

## Step 510
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0510.h5', 'table')
assert round(df['stress_xx'].min() - 1.0026665338366039, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0112231542459431, 8) == 0.0

## Step 750
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0750.h5', 'table')
assert round(df['stress_xx'].min() - 1.0000053000532143, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0000225119807862, 8) == 0.0

## Step 990
df = pd.read_hdf('results/uniaxial-nodal-forces-2d/particles0990.h5', 'table')
assert round(df['stress_xx'].min() - 0.9999990078443788, 8) == 0.0
assert round(df['stress_xx'].max() - 0.9999990292713694, 8) == 0.0


# Particle traction results
## Step 300
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0300.h5', 'table')
assert round(df['stress_xx'].min() - 0.4450086768966724, 8) == 0.0
assert round(df['stress_xx'].max() - 0.5966527842046769, 8) == 0.0

## Step 510
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0510.h5', 'table')
assert round(df['stress_xx'].min() - 0.7528092313640623, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0109599915279937, 8) == 0.0

## Step 750
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0750.h5', 'table')
assert round(df['stress_xx'].min() - 0.7500090055681591, 8) == 0.0
assert round(df['stress_xx'].max() - 1.0000224746314728, 8) == 0.0

## Step 990
df = pd.read_hdf('results/uniaxial-particle-traction-2d/particles0990.h5', 'table')
assert round(df['stress_xx'].min() - 0.750002924022295, 8) == 0.0
assert round(df['stress_xx'].max() - 0.9999997782938734, 8) == 0.0
