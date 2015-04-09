import random, math

# comment

random_vector   = lambda n : [random.random() for i in range(n)]
average         = lambda l : float(sum(l))/len(l)
l2_norm_squared = lambda v1,v2: sum([ (i-j)*(i-j) for i,j in zip(v1,v2)])

def average_vect(l):
	n = len(l[0])
	result = []
	for i in range(n):
		result.append(average([z[i] for z in l]))
	return result

def k_means(data,num_clusters,threshold = 0.1):
	p = len(data[0])
	n = len(data)
	centroids = [random_vector(p) for i in range(num_clusters)]
	d         = [[0 for j in range(num_clusters)] for i in range(n)]
	c         = [0 for i in range(n)]	
	delta = threshold + 1
	while delta > threshold:
		# d[i][j] is the distance between the i-th data point and j-th centroid
		for i,i_ in enumerate(data):
			for j,j_ in enumerate(centroids):
				d[i][j] = l2_norm_squared(i_,j_)
		# c[i] is the label of the centroid closest to the i-th data point
		for i in range(n):
			c[i] = d[i].index(min(d[i]))

		new_centroids = []
		for k in range(len(centroids)):
#			print [data[i] for i,j in enumerate(c) if j == k]
			new_centroids.append(average_vect([data[i] for i,j in enumerate(c) if j == k] ))
#			print new_centroids
		delta = 0
		for a,b in zip(centroids,new_centroids):
			delta = delta + l2_norm_squared(a,b)
		centroids = new_centroids[:]
	return c,centroids

#data_ = [(1,2),(2,1),(1,1),(3,2),(4,2),(-1,-2),(-2,-2),(-1,-1),(-3,-1),(-2,-2)]
data_ = [(1,2),(-2,-2),(2,1),(-1,-1),(1,1),(-3,-1),(3,2),(-2,-2),(4,2),(-1,-2)]


result = k_means(data_,2)[0]
print result
for k in range(2):
	print [data_[i] for i,j in enumerate(result) if j == k]