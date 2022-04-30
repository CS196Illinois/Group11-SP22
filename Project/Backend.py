
import numpy as np
import pandas as pd
import math
from scipy import stats
import matplotlib.pyplot as plt

student = np.array(['John','Sandy','Coco','Snute','Noel','Monsoon','Eric','Allen','Michelle','Cathy'])
score = np.array([76.,96.,88.,26.,84.,79.,83,90.,90.,60.], dtype='f')
df_test = pd.DataFrame({'Name': student, 'Score' : score})

def sqrtCurver(df, median):
    dm = df['Score'].median()
    if dm > median:
        return df
    d = float((100. - median) / math.sqrt(100. - dm))
    dn = df['Score'].to_numpy()
    dn = 100. - d * np.sqrt(100. - dn)
    dn = dn.astype(int)
    dns = pd.Series(dn)
    df['Score'] = dns
    return df

def linearCurver(df, max, min):
    dfc = df.copy()
    dfc[(np.abs(stats.zscore(dfc['Score'])) < 3)]
    dmax = dfc['Score'].max()
    dmin = dfc['Score'].min()
    if dmin > min or dmax > max:
        return df
    dn = df['Score'].to_numpy()
    dn = max + (max - min) / (dmax - dmin) * (dn - dmax)
    dn = dn.astype(int)
    dns = pd.Series(dn)
    df['Score'] = dns
    return df

def GuzmanCurver(df, total):
    dn = df['Score'].to_numpy()
    dn = dn / total * 100
    dn = dn.astype(int)
    dns = pd.Series(dn)
    df['Score'] = dns
    return df

def normalCurver(df, median):
    dfc = df.copy()
    dm = df['Score'].median()
    if dm > median:
        return df
    dn = df['Score'].to_numpy()
    std = 100 - median
    for i in range(len(dn)):
        dp = stats.percentileofscore(df['Score'], dn[i], kind='strict') / 100  + 0.000000001
        dposition = stats.norm.ppf([dp, median, std])[0]
        dn[i] = dposition * std + median
    dn = dn.astype(int)
    dns = pd.Series(dn)
    df['Score'] = dns
    return df


# df_final = normalCurver(df_test.copy(), 90)
# print(df_test.to_string())
# print(df_final.to_string())
# fig, axes = plt.subplots(nrows=1, ncols=2)
# df_test.hist(ax=axes[0])
# df_final.hist(ax=axes[1])
# axes[0].set_xlim([0, 120])
# axes[1].set_xlim([0, 120])
# plt.show()

student_l = np.arange(0, 100 ,1)
score_l = np.random.randint(0, 100, size=100)
df_large = pd.DataFrame({'Name': student_l, 'Score' : score_l})
dfl_final = normalCurver(df_large.copy(), 90)
# dfl_final = GuzmanCurver(df_large.copy(), 90)
print(df_large.to_string())
print(dfl_final.to_string())
fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].hist(df_large['Score'], bins=20)
axes[1].hist(dfl_final['Score'], bins=20)
axes[0].set_xlim([0, 120])
axes[1].set_xlim([0, 120])
plt.show()

