
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def show_corr(X, mask=True, figsize=(7,7)):
    fig, ax = plt.subplots(figsize=figsize)
    corr = X.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool)) if mask else np.ones_like(corr, dtype=bool)
    sns.heatmap(corr, mask=mask, square=True, annot=True, ax=ax)
    plt.show()