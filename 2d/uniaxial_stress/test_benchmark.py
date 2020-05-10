import pandas as pd
df = pd.read_hdf('results/uniaxial-stress-2d-usf/particles09.h5', 'table')
syy = -0.9999999999999999
sxx = 0.0
assert round(df['stress_yy'].max() - syy, 8) == 0.0
assert round(df['stress_xx'].max() - sxx, 8) == 0.0
