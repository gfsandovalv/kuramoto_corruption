import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats as st
from modules.kuramoto import Kuramoto
from modules.plotting import plot_activity, plot_phase_coherence

# Parámetros del modelo

coupl = 3 # Coupling
dt = 0.1 #
T=10 # time interval (0, T)
num_osc = 100 # number of oscillators

honesty_freq = 100
corruption_freq = 500

forcing_amp = 1

## initialize distributions

honesty_normal_dist = st.norm(loc=honesty_freq, scale=1) ## normal distribution centered at 100 and standar deviation 1
honesty_natfreqs_sample = honesty_normal_dist.rvs(size=num_osc) ## sample of size = num_osc


## create graph
graph_nx = nx.erdos_renyi_graph(n=num_osc, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)
#nx.draw(graph_nx, labels=labeldict, with_labels = True)


model = Kuramoto(coupling=coupl, dt=dt, T=T, 
                 natfreqs=honesty_natfreqs_sample, forcing_amp=forcing_amp, forcing_freq=corruption_freq) 
act_mat = model.run(adj_mat=graph)


mean_frequencies = model.mean_frequency(act_mat, graph)

# initialize figures
fig, ax = plt.subplots(1,2)

x = np.linspace(honesty_normal_dist.ppf(0.01), honesty_normal_dist.ppf(0.99), 100)
ax[0].plot(x, honesty_normal_dist.pdf(x), 'k-', lw=2, label='frozen pdf'); # pdf

## histogram parameters
bins = 15
rwidth = 0.9
ax[0].hist(honesty_natfreqs_sample, bins=bins, rwidth=rwidth, density=True); # histogram of the sample
ax[1].hist(mean_frequencies, bins=bins,rwidth=rwidth)
plt.show()