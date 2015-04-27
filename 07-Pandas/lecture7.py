import numpy as np
randn = np.random.randn
import pandas as pd

s = pd.Series(np.arange(5), index=['a', 'b', 'c', 'd', 'e'])
print s

pd.Series(randn(5))

s[0]
print("\n")
s[s > s.median()]
print("\n")
s[[3,2,1]]

s['a']
s['e'] = 6
s
'e' in s
'f' in s

s+s
s**2
np.exp(s)

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)

df

pd.DataFrame(df, index=['d', 'b', 'a'])

pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1,index=list(range(4)),
                                   dtype='float32'),
                    'D': np.array([3] * 4,dtype='int32'),
                    'E': 'foo' })

df2

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1,index=list(range(4)),
                                   dtype='float32'),
                    'D': np.array([3] * 4,dtype='int32'),
                    'E': 'foo' })

df2.dtypes

# Date range
dates = pd.date_range('20130101', periods=6)
# Dataframes
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df

df.head()

df.tail(3)

df.columns, df.values

df.describe()

df['A']

df[0:3]

df['20130102':'20130104']

from datetime import date
df[date(2013,1,2):date(2013,1,4)]

df.iloc[[4, 2]]

gp = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
gp

gp.groupby('A').sum()

gp.groupby(['A','B']).mean()

left = pd.DataFrame({'key': ['one', 'two'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['two', 'one'], 'rval': [4, 5]})
pd.merge(left, right, on='key')

import matplotlib.pyplot as plt
df = pd.DataFrame(randn(1000, 4), 
                  index=pd.date_range('1/1/2000', periods=1000),
                  columns=list('ABCD'))
df = df.cumsum()
ax = df.plot()

plt.savefig('ts.png')
'ts.png'

# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols)

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols)

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date',
          'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5))

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
lens = pd.merge(movie_ratings, users)

lens.head(3)

most_rated = lens.groupby('title').size().order(ascending=False)[:10]
print most_rated

movie_stats = lens.groupby('title').agg({'rating': [np.size, np.mean]})
movie_stats.head()

movie_stats.sort([('rating', 'mean')], ascending=False).head()

atleast_100 = movie_stats['rating'].size >= 100
movie_stats[atleast_100].sort([('rating', 'mean')], ascending=False).head()

### Exercise ###
### Try to plot the ratings distribution of a movie of your choice.
### you can use the hist() function to produce a histogram


### Exercise ###
### plot the mean rating by age of user

