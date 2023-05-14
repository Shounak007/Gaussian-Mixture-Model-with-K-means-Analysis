# K-Means and GMM Clustering Assignment

The first part of the project explores a K means analysis and the second part performs a Gaussian Mixture Model (GMM) clustering on a given dataset.


The repository should contain the following files:

1. This README.
2. `cluster.py` which contains the definition of the `Cluster` class and some testing code.
3. `point.py` which contains the definition of the `Point` class and some testing code.
4. `kmeans.py` which contains the skeleton of the k-means algorithm and some testing code.
5. `gmm.py` which contains the skeleton of the `gaus_mixture()` function.  
6. `gmm_data_x1.csv` and `gmm_data_x12.csv` which contain the data that will be used to test your GMM function. 

## Implementing K-Means Clustering 
First we explore how to use K-means clustering on a given dataset.

## Step 1: Complete Point class


1. `distFrom`, which calculates the (Euclidean) distance between the current point and the target point. We account for the fact that a point may be in more than two dimensions (Euclidean distance generalizes: square the difference in each dimension and take the square root of the sum). In general, for points given $n$-dimensional Euclidean space, the Euclidean distance $d$ between two $n$ dimensional vectors, say $p$ and $q$ is given by: $$d(p,q) = \sqrt{(p_{1} - q_{1})^{2} + (p_{2} - q_{2})^{2}+ \dots +(p_{i} - q_{i})^{2}+\dots+(p_{n} - q_{n})^{2}}.$$

2. `makePointList`, which takes in a data p-by-d input matrix `data` and returns a list of p `Point` objects. 


3. We can test our code by running `python3 point.py`, you should get the 

We should recieve the following:
```
[Point([0.5 2.5]), Point([0.3 4.5]), Point([-0.5  3. ]), Point([0.  1.2]), Point([10. -5.]), Point([11.  -4.5]), Point([ 8. -3.])]
2.009975124224178
```

## Step 2: Complete Cluster class


1. `avgDistance`, which computes the average distance from the center of the cluster (stored in `self.center`) to all of the points currently in the cluster (stored in `self.points`). This can most easily be done by summing the distances between each point and the current center and then dividing the sum by the total number of points.

2. `updateCenter`, which updates the center of the cluster (stored in `self.center`) to be the average position of all the points in the cluster.
Note that if there are no points in the cluster, then self.center should be unchanged

> Note that we have defined `dim` and `coords` as properties that return information about the center of the cluster -- this means that if you pass a cluster into a method that is expecting a point, operations that access `dim` and `coords` will use the center of the cluster. Think about how that might be useful in conjunction with the `closest` method defined for `Point`.

If you test your code by running `python3 cluster.py`, you should get the following:

```
Cluster: 0 points and center = [0.5, 3.5]
Cluster: 2 points and center = [0.5, 3.5]
1.4976761962286425
Cluster: 2 points and center = [1.75, 2.75]
0.3535533905932738
```


## Step 3: Implement k-means

Use the methods in `Point` and `Cluster` to implement the missing `kmeans` method in `kmeans.py`. The basic recommended procedure is outlined in `kmeans.py`.

If you test your code by running `python3 kmeans.py`, you should get the following:

```
Cluster: 4 points and center = [0.075 2.8  ]
   [0.3 4.5]
   [0.  1.2]
   [0.5 2.5]
   [-0.5  3. ]
Cluster: 3 points and center = [ 9.66666667 -4.16666667]
   [ 8. -3.]
   [10. -5.]
   [11.  -4.5]
```


## Find best number of clusters to use on GMM algorithms


This part employs GMM to cluster a data set and identify the right number of clusters in the data. The data points consist of two features, each stored in one of the two data files provided: 'gmm_data_x1.csv' and 'gmm_data_x2.csv.' As the first step, we will write the function concatenate_features() to concatenate these features into a single data structure. Then, we will write the function gaus_mixture() to use these concatenated features to run GMM clustering and obtain the optimal number of clusters given a list of candidate cluster numbers.


`concatenate_features()` takes in 2, 1-D numpy array of same length, say n. Each array represents one of the features of the n datapoints. The function returns an unified numpy array of the shape `(n, 2)` by concatenating the two numpy array arguments given to the function, where each column in the unified array represents the 1-D numpy arrays provided as input.  

`gaus_mixture()` takes in a `(n, 2)` and a list of positive integers (possible number of clusters for the data), and find the optimal number of clusters from the given list for the gaussian mixture model clustering.

Given the concatenated features and a list of the number of clusters as input, the function should return the best number of clusteres to use (from the input list of candidate cluster numbers) on the GMM.

The best number of clusters is determined by (1) fitting a GMM model using a specific number of clusters, (2) calculating its corresponding Bayes Information criterion (BIC - see formula below), and then (3) setting the number of clusters corresponding to the lowest BIC as the best number of clusters to use.

This function should be completed using the algorithm outlined in the skeleton code. In addition, consider the following hints: 

1. The GMM algorithm can be implemented using the sklearn library using `gm = GaussianMixture(n_components=d, random_state=0).fit(dataset)`, where `d` corresponds to the number of clusters to use and dataset is a (for our case) `n-by-1` array of data. Lastly, `random_state=0` is a random seed that allows for reproducibility. **In your code, you must set**  `random_state=0` when you call `GaussianMixture`.


2. The BIC formula is given by `BIC = -2log(L) + log(N)d`, where `L` is the maximum likelihood of the model, `d` is the number of parameters, and `N` is the number of data samples. When using the sklearn library, however, the BIC is given by `bic = gm.bic(dataset)`, where `gm` is the object returned when `GaussianMixture()` from Hint 1 is instantiated. `gm.bic` is how the BIC should be calculated in your implementation. 

When you run your code on the given data in `gmm_data_x1.csv` and `gmm_data_x2.csv` using `n_components=[2, 3, 4, 5, 6, 7, 8]` as the possible number of clusters, your output should be:

```
Shape of the first feature array:  (400,)
Shape of the second feature array:  (400,)
Shape of the concatenated array:  (400, 2) 
Best fit is when k = 4 clusters are used
```
