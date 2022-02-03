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

forcing_amp = 0.1


# Implementation

## initialize distributions
honesty_normal_dist = st.norm(loc=honesty_freq, scale=1) ## centered at 100 and standar deviation 1
honesty_natfreqs_sample = honesty_normal_dist.rvs(size=num_osc) ## sample of size = num_osc

## create graph
graph_nx = nx.erdos_renyi_graph(n=num_osc, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)
#nx.draw(graph_nx, labels=labeldict, with_labels = True)

def models_varying_corruption_freqs(corruption_freqs):
    models = {}
    for corruption_freq in corruption_freqs:
        models[str(corruption_freq)]= Kuramoto(coupling=coupl, dt=dt, T=T, 
                 natfreqs=honesty_natfreqs_sample, 
                 forcing_amp=forcing_amp, 
                 forcing_freq=corruption_freq)
    return models

def act_mats_varying_corr_freqs(corruption_freqs):
    models = models_varying_corruption_freqs(corruption_freqs)
    act_mats = {}
    for key, model in models.items():
        print(key)
        act_mats[key] = model.run(adj_mat=graph)
    return act_mats

corruption_freqs = [100, 200, 300]
act_mats = act_mats_varying_corr_freqs(corruption_freqs)

for key, act_mat in act_mats.items():
    plot_phase_coherence(act_mat, key)
plt.show()