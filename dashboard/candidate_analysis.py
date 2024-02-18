import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('agg')

# Code to show the candidate histogram, called in views.py by def candidate_histogram function
def candidate_histogram_code(candidates):

    sns.set_theme(style="ticks")
    sns.color_palette("PuOr", as_cmap=True)
    plt.figure(figsize=(10, 4))
    
    chart = sns.histplot(
        data=candidates, 
        x="Score", 
        multiple="stack", 
        hue='StudyProgram',
        edgecolor=".3", 
        bins=50, 
        linewidth=.5, 
        kde=True

    )
    return chart
    