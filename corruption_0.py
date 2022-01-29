import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from kuramoto import Kuramoto, plot_activity, plot_phase_coherence

natfreqs_given = [1,2,3,500,250]
labeldict = {i:e for i, e in enumerate(natfreqs_given)}

graph_nx = nx.erdos_renyi_graph(n=len(natfreqs_given), p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)
#nx.draw(graph_nx, labels=labeldict, with_labels = True)

model = Kuramoto(coupling=0.5, dt=0.01, T=10, natfreqs=natfreqs_given)
act_mat = model.run(adj_mat=graph)


fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15, 5),
                         subplot_kw={
                             "ylim": (-1.1, 1.1),
                             "xlim": (-1.1, 1.1),
                             "xlabel": r'$\cos(\theta)$',
                             "ylabel": r'$\sin(\theta)$',                             
                         })



times = [0, 200, 999]
        
for ax, time in zip(axes, times):
    ax.plot(np.cos(act_mat[:, time]), 
            np.sin(act_mat[:, time]), 
            '*', 
            markersize=10)
    ax.set_title(f'Time = {time}')
    for key, value in labeldict.items():
        ax.annotate(value, 
                    (
                        np.cos(act_mat[:, time])[key],
                        np.sin(act_mat[:, time])[key]
                     )
                    )
        


plt.tight_layout()
plt.show()