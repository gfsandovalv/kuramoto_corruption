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
corruption_freq = 700

# forcing_amps defined ahead

# Implementation

## initialize distributions
honesty_normal_dist = st.norm(loc=honesty_freq, scale=1) ## centered at 100 and standar deviation 1
honesty_natfreqs_sample = honesty_normal_dist.rvs(size=num_osc) ## sample of size = num_osc

## create graph
graph_nx = nx.erdos_renyi_graph(n=num_osc, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)
#nx.draw(graph_nx, labels=labeldict, with_labels = True)


def models_varying_forc_amp(forcing_amps):
    models = {}
    for forcing_amp in forcing_amps:
        models[str(forcing_amp)]= Kuramoto(coupling=coupl, dt=dt, T=T, 
                 natfreqs=honesty_natfreqs_sample, 
                 forcing_amp=forcing_amp, 
                 forcing_freq=corruption_freq)
    return models

def mean_freqs_varying_forc_amp(forcing_amps):
    models = models_varying_forc_amp(forcing_amps)
    mean_frequencies_for_several_forcing_amps = {}
    for key, model in models.items():
        print(key)
        act_mat = model.run(adj_mat=graph)
        mean_frequencies_for_several_forcing_amps[key] = model.mean_frequency(act_mat, graph)
    return mean_frequencies_for_several_forcing_amps


forcing_amps = [0.01, 0.1, 1, 10]
models_several_f_amps = models_varying_forc_amp(forcing_amps)
mean_frequencies_ = mean_freqs_varying_forc_amp(forcing_amps)

# initialize figures
fig, ax = plt.subplots(1, len(forcing_amps) + 1)

x = np.linspace(honesty_normal_dist.ppf(0.01), honesty_normal_dist.ppf(0.99), 100)
ax[0].plot(x, honesty_normal_dist.pdf(x), 'k-', lw=2, label='frozen pdf'); # pdf

## histogram parameters
bins = 50
rwidth = 0.9
ax[0].hist(honesty_natfreqs_sample, bins=bins, rwidth=rwidth, density=True); # histogram of the sample

i = 1
for force_amp, mean_freqs in mean_frequencies_.items():
    ax[i].hist(mean_freqs, bins=bins,rwidth=rwidth)
    ax[i].set_title('F = ' + force_amp)
    print(force_amp)
    i += 1
plt.show()
""" act_mat = list(models_several_f_amps.values())[-1].run(adj_mat=graph)
plot_phase_coherence(act_mat)
plot_activity(act_mat)
plt.show() """