import scipy.io as sio
import numpy as np
mat = sio.loadmat("sortedData",squeeze_me=True)
print(mat.keys())
print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
"""
for k,v in mat.items():
	print("\n",k,"\n")
	print("\n",v,"\n")
"""
data = mat.get("Data")
"""
print(type(data))
print(data.ndim)
print(data.shape)
"""

# retrieve the output patient list 
output = [] 
for i in data[:,0]:
	output.append(i[2])

print("output before: ",output)
output = np.repeat(output,6)
print("output size: ",output.size)

d1 = data[:,1]
d2 = np.zeros((d1.shape[0]*6,5001,2))
count = 0 
for p in range(65):
	for r1 in range(6):
		for r2 in range(5001):
			for c2 in range(2):
				d2[count,r2,c2] = d1[p][r1,1][r2,c2]
		count +=1


d2 = np.transpose(d2,(0,2,1))
d2 = d2.reshape(390,10002)
#print(d2.shape)

		
