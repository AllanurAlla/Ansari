'''
read_chains_example.py: an example to read MCMC chains generated by run_mcmc.py.
Y.S.Murakami 2022 @ JHU
'''

import numpy as np
import matplotlib.pyplot as plt
import h5py

###### config ######
CHAIN_PATH = 'final_v2_baseline.h5' #this file is currently being uploaded to Zenodo
BURNIN = 6000
####################

# Data is big. Select indices that you are interested in.
idx = [37,38,39,40,41,42,43,45,46]
idx = np.asarray(idx)

# Load data
samples = h5py.File(CHAIN_PATH,'r')['mcmc']['chain'][:,:,idx]

# The loaded chains are raw (=uncut) and you need to apply burnin.
# For the discussion on burnin-size, see Sec. 5.1 (MCMC Sampling) of the SH0ES paper.
samples_burnin = samples[BURNIN:,:,:]

# Once the burnin is applied, one can flatten the chains
# Don't forget to apply formula to obtain the physical quantity.
H0_idx = -1
fivelogH0 = samples_burnin[:,:,H0_idx].flatten()
H0_samples = 10**(fivelogH0/5)

# Now it's ready for analyses/plotting!
plt.figure(figsize=(8,6))
plt.hist(H0_samples,bins=100)
plt.show()
