"""
Shared plotting utilities.

Provides consistent figure setup and display helpers used across all modules.
"""

import matplotlib.pyplot as plt


def setup_plot(title: str, xlabel: str, ylabel: str,
               figsize: tuple = (10, 6)) -> tuple:
    """
    Create and configure a matplotlib figure with consistent styling.

    Returns:
        (fig, ax) tuple.
    """
    fig, ax = plt.subplots(figsize=figsize)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(True)
    return fig, ax


def show_plot():
    """Display the current plot."""
    plt.tight_layout()
    plt.show()
