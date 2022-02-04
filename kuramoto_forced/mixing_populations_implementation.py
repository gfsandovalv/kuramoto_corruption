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
## proportions of honest and corrupted
honest_like_prop = 0.8 # proportion of "honest" individuals 
corrupted_like_prop = 1 - honest_like_prop # proportion of "corrupted" individuals 
## populations
population = 100 # number of individuals (i.e. oscillators)
honest_population = int(population * honest_like_prop)
corrupted_population = population - honest_population

honesty_freq = 100
corruption_freq = 600


# Implementation

## initialize distributions
### honest dist and sample
honesty_normal_dist = st.norm(loc=honesty_freq, scale=1) ## centered at 100 and standar deviation 1
honesty_natfreqs_sample = honesty_normal_dist.rvs(size=honest_population) 
### corrupted dist and sample
corruption_normal_dist = st.norm(loc=corruption_freq, scale=1) ## normal distribution centered at 100 and standar deviation 1
corruption_natfreqs_sample = corruption_normal_dist.rvs(size=corrupted_population) 
### population frequencies 
pop_freqs = np.concatenate((honesty_natfreqs_sample, corruption_natfreqs_sample))


## plots of the samples histograms and distributions pdfs

## initialize figures
initial_population_fig, ax = plt.subplots(1, 2)

x = np.linspace(honesty_normal_dist.ppf(0.01), honesty_normal_dist.ppf(0.99), 100)
x2 = np.linspace(corruption_normal_dist.ppf(0.01), corruption_normal_dist.ppf(0.99), 100)

ax[0].plot(x, honesty_normal_dist.pdf(x), 'k-', lw=2, label='frozen pdf'); # pdf
ax[0].hist(pop_freqs[:-corrupted_population], bins=int(honest_population/5), rwidth=0.8, density=True); # histogram of the sample
ax[0].set_title('Población honesta')

ax[1].plot(x2, corruption_normal_dist.pdf(x2), 'k-', lw=2, label='frozen pdf'); # pdf
ax[1].hist(pop_freqs[-corrupted_population:], bins=int(population/20), rwidth=0.8, density=True); # histogram of the sample
ax[1].set_title('Población corrupta')

initial_population_fig.savefig('figs/mixed_pop_initial_dist.png')
plt.close(initial_population_fig)

## create graph
graph_nx = nx.erdos_renyi_graph(n=population, p=1) # p=1 -> all-to-all connectivity
graph = nx.to_numpy_array(graph_nx)

## intialization of model as Kuramoto Class and runing it over the graph
model = Kuramoto(coupling=coupl, dt=dt, T=T, natfreqs=pop_freqs)
act_mat = model.run(adj_mat=graph)

## plot of order parameter
order_parameter_fig, ax = plot_phase_coherence(act_mat)
order_parameter_fig.savefig('figs/mixed_pop_order_parameter.png')
plt.close(order_parameter_fig)