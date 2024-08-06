"""https://www.youtube.com/watch?v=1-R5b3dTvhs
import sys
import stemgraphic

data = {5.5,5.5,5.1,5.1,4.9,6.6,5.5,5.6,6.7,6.9,5.2,7.2,7.4,6.7,7.2,5.1,5.6,6.0,5.8,5.7,5.2,4.9,5.3,5.8,4.8,5.7,5.3}
stemgraphic.stem_graphic(data, scale = 27)"""

import matplotlib.pyplot as plt 
  
data = [16, 25, 47, 56, 23, 45, 19, 55, 44, 27] 
stems = [1, 1, 2, 2, 2, 4, 4, 4, 5, 5] 
  
plt.ylabel('Data')   
  
plt.xlabel('stems')   
  
plt.xlim(0, 10)   
  
plt.stem(stems, data) 

