import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')
data={'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new_feature=[5,7]
for i in data:
      for ii in data[i]:
            plt.scatter(ii[0],ii[1] ,s=100,color=i)
plt.scatter(new_feature[0],new_feature[1],s=100,color='b')
plt.show()
def k_nearest_neighbor(data,predict,k):
      if len(data)>=k:
            warnings.warn('K is set to a value less than total groups')
      distances=[]
      for group in data:
            for features in data[group]:
                  euclidean_distance=np.sqrt(np.sum((np.array(features)-np.array(predict))**2))
                  distances.append([euclidean_distance,group])
      votes=[i[1] for i in sorted(distances)[:k]]
      print Counter(votes).most_common(1)
      vote_result=Counter(votes).most_common(1)[0][0]

      return vote_result
result= k_nearest_neighbor(data,new_feature,k=3)
print result
if result[0]=='r':
      plt.scatter(new_feature[0], new_feature[1], s=100, color='r')
else:
      plt.scatter(new_feature[0], new_feature[1], s=100, color='k')
for i in data:
      for ii in data[i]:
            plt.scatter(ii[0],ii[1] ,s=100,color=i)
plt.show()

