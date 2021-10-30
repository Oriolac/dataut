import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

class DropColumnsTransf(BaseEstimator, TransformerMixin):
    
    def __init__(self, columns):
        self.cols = columns
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X.drop(columns=self.cols, axis=1)

class FillNaFeatOnFeat(BaseEstimator, TransformerMixin):
    
    def __init__(self, from_col, to_col):
        self.from_col = from_col
        self.to_col = to_col
    
    def fit(self, X, y=None):
        self.mean_ages = X.groupby(self.from_col)[self.to_col].mean()
        return self
    
    def transform(self, X):
        def getmedium():
            def apply_age(tup):
                if np.isnan(tup[self.to_col]):
                    return self.mean_ages[tup[self.from_col]]
                else:
                    return tup[self.to_col]
            return apply_age
        X[self.to_col] = X[[self.to_col, self.from_col]].apply(getmedium(), axis=1)
        return X