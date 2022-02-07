import matplotlib.pyplot as plt
import numpy as np

from .kuramoto import Kuramoto


def plot_activity(activity):
    """
    Plot sin(angle) vs time for each oscillator time series.

    activity: 2D-np.ndarray
        Activity time series, node vs. time; ie output of Kuramoto.run()
    return:
        matplotlib axis for further customization
    """
    _, ax = plt.subplots(figsize=(12, 4))
    ax.plot(np.sin(activity.T))
    ax.set_xlabel('Time', fontsize=25)
    ax.set_ylabel(r'$\sin(\theta)$', fontsize=25)
    return ax


def plot_phase_coherence(activity, title=None):
    """
    Plot order parameter phase_coherence vs time.

    activity: 2D-np.ndarray
        Activity time series, node vs. time; ie output of Kuramoto.run()
    return:
        matplotlib axis for further customization
    """
    if title is not None:
        title = str(title)
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot([Kuramoto.phase_coherence(vec) for vec in activity.T], 'o')
        ax.set_ylabel('Parámetro de orden')
        ax.set_xlabel('Tiempo')
        ax.set_ylim((-0.01, 1))
        ax.set_title(title)
    else:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.plot([Kuramoto.phase_coherence(vec) for vec in activity.T], 'o')
        ax.set_ylabel('Parámetro de orden')
        ax.set_xlabel('Tiempo')
        ax.set_ylim((-0.01, 1))
    return fig, ax
