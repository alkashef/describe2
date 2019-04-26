import numpy as np
import pandas as pd
from collections import Counter

class Describe2:

    def _unique(self, series):
        return len(series.unique())

    def _count0(self, series):
        frequencies = series.value_counts().to_dict()
        return frequencies.get(0, 0)

    def _count_positive(self, series):
        return np.sum(series.values > 0)

    def _count_negative(self, series):
        return np.sum(series.values < 0)

    def _mode(self, series):
        return Counter(series).most_common(1)[0][0]

    def _outliers_3sig(self, series):
        p_threshold = np.mean(series) + (3 * np.std(series))
        n_threshold = np.mean(series) - (3 * np.std(series))
        return np.sum(series > p_threshold) + np.sum(series < n_threshold)

    def dim(self, df):
        no_rows = len(df)
        no_cols = len(df.columns)
        print(no_rows, "rows x", no_cols, "columns")
    
    def _describe_num(self, df):
        df = df.select_dtypes(include=['number'])
        description = pd.DataFrame()
        description['Type'], description['Density'] = df.ftypes.str.split(':').str
        description['No. of Values'] = df.apply(len, axis=0)
        description['No. of Unique Values'] = df.apply(self._unique, axis=0)
        description['No. of NaN'] = description['No. of Values'] - df.count(axis=0)
        description['No. of Zeros'] = df.apply(self._count0, axis=0)
        description['No. of +ve Values'] = df.apply(self._count_positive, axis=0)
        description['Min'] = df.apply(np.min, axis=0)
        description['Max'] = df.apply(np.max, axis=0)
        description['Mean'] = df.apply(np.mean, axis=0)
        description['Std'] = df.apply(np.std, axis=0)
        description['Median'] = df.apply(np.median, axis=0)
        description['Mode'] = df.apply(self._mode, axis=0)
        description['Skew'] = df.apply(pd.DataFrame.skew, axis=0)
        description['Kurtosis'] = df.apply(pd.DataFrame.kurtosis, axis=0)
        description['No. of 3 Sigma Outliers'] = df.apply(self._outliers_3sig, axis=0)
        return description

    def _describe_obj(self, df):
        df = df.select_dtypes(include=['object'])
        description = pd.DataFrame()
        description['Type'], description['Density'] = df.ftypes.str.split(':').str
        description['No. of Values'] = df.apply(len, axis=0)
        description['No. of Unique Values'] = df.apply(self._unique, axis=0)
        description['No. of NaN'] = description['No. of Values'] - df.count(axis=0)
        return description

    def d2(self, df):
        num = self._describe_num(df)
        obj = self._describe_obj(df)
        return num, obj
