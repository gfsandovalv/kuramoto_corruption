import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats as st
from modules.kuramoto import Kuramoto
from modules.plotting import plot_activity, plot_phase_coherence

n_osc = 100
coupl = 3

## frecuencias naturales usando la distribución de cauchy
normal_dist = st.norm(loc=100, scale=1)
natfreqs_sample = normal_dist.rvs(size=n_osc)

#natfreqs_sample = [1,2,5,100]
labeldict = {i:e for i, e in enumerate(np.floor(natfreqs_sample))}

graph_nx = nx.erdos_renyi_graph(n=n_osc, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)
#nx.draw(graph_nx, labels=labeldict, with_labels = True)


model = Kuramoto(coupling=coupl, dt=0.1, T=10, 
                 natfreqs=natfreqs_sample, forcing_amp=1, forcing_freq=50) 
act_mat = model.run(adj_mat=graph)


a = model.mean_frequency(act_mat, graph)
fig, ax = plt.subplots()
ax.hist(a, bins=5, rwidth=0.9)


#plot_phase_coherence(act_mat)
plt.show()