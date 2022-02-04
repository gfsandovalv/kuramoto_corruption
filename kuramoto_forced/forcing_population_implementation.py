import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy import stats as st
from modules.kuramoto import Kuramoto
from modules.plotting import plot_activity, plot_phase_coherence

# Parámetros del modelo
coupl = 2.5 # Coupling
dt = 0.1 #
T=10 # time interval (0, T)

population = 100 # number of individuals (i.e. oscillators)
honesty_freq = 100
corruption_freq = 600
forcing_amp = 0.1

# Implementation

## initialize distributions
### distribution of the population frequencies cetered at honesty_freq
population_normal_dist = st.norm(loc=honesty_freq, scale=2) ## centered at 100 and standar deviation 2
pop_natfreqs_sample = population_normal_dist.rvs(size=population) 

## plots of the samples histograms and distributions pdfs
## initialize figures
initial_population_fig, ax = plt.subplots()
x = np.linspace(population_normal_dist.ppf(0.01), population_normal_dist.ppf(0.99), 100)
ax.plot(x, population_normal_dist.pdf(x), 'k-', lw=2, label='frozen pdf'); # pdf
ax.hist(pop_natfreqs_sample, bins=int(population/10), rwidth=0.8, density=True); # histogram of the sample
ax.set_title('Población')


initial_population_fig.savefig('figs/forced_pop_initial_pop.png')
plt.close(initial_population_fig)

## create graph
graph_nx = nx.erdos_renyi_graph(n=population, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)

## intialization of model as Kuramoto Class and runing it over the graph
model = Kuramoto(coupling=coupl, dt=dt, T=T, 
                 natfreqs=pop_natfreqs_sample, forcing_amp=forcing_amp, forcing_freq=corruption_freq)
act_mat = model.run(adj_mat=graph)

## plot of order parameter
order_parameter_fig, ax = plot_phase_coherence(act_mat)
order_parameter_fig.savefig('figs/forced_pop_order_parameter.png')
plt.close(order_parameter_fig)

## mean frequencies over all timespan
mean_frequencies = model.mean_frequency(act_mat=act_mat, adj_mat=graph)

### plot
mean_frequencies_fig, ax = plt.subplots()
ax.hist(mean_frequencies, bins=10, rwidth=0.8, density=True)
ax.set_title('Histograma de las frecuencias medias')
mean_frequencies_fig.savefig('figs/forced_pop_mean_freqs.png')
plt.close(mean_frequencies_fig)