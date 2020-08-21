
from matplotlib import font_manager
from matplotlib import pylab as plt

def axes_legend_label(axes, xlabel, ylabel):
    for ax in axes:
        ax.tick_params(axis='x', labelsize=16)
        ax.tick_params(axis='y', labelsize=16)
        ax.tick_params(which='major', width=1.5, length=7)
        ax.tick_params(which='minor', width=1.5, length=4)

    ax.legend(prop=font_manager.FontProperties(size=10))
    
    font_prop=font_manager.FontProperties(size=16)

    ax.set_xlabel(xlabel, fontproperties=font_prop)
    ax.set_ylabel(ylabel, fontproperties=font_prop)

def extra_ticks(et):
    ax = plt.gca()
    tx = ax.get_xticks()
    ax.set_xticks(
        list(tx)+et
    )
    ax.set_xticklabels(
        list(tx)+et
    )

