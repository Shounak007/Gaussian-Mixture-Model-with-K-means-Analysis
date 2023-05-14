import numpy as np
from sklearn.mixture import GaussianMixture

def concatenate_features(X1, X2):

    """ 
    Merge the array of features X1 and X2 into a single numpy array

    Args:
    X1: an n-dimensional numpy array of numbers that contains the first feature of the n data points
    X2: an n dimensional numpy array of numbers that contains the second feature of the n data points 
    
    Returns:
    A single numpy array of the shape (n,2). In other words, a single numpy array that has n rows and
    2 columns, where the first column corresponds to X1 and the second column corresponds to X2.
    

    # Hint: Take a look at the numpy's reshape and concatenate methods.
    """

    n = len(X1)

    # 1. Using the np.reshape() method, reshape X1 to the shape (n, 1)
        # fill in
    X1_reshaped = np.reshape(X1, (n, 1))


    # 2. Using the np.reshape() method, reshape X2 to the shape (n, 1)
        # fill in
    X2_reshaped = np.reshape(X2, (n, 1))


    # 3. Using np.concatenate, stack the feature arrays and produce a single numpy array of shape (n,2)
        # fill_in
    merged_features = np.concatenate((X1_reshaped, X2_reshaped), axis=1)


    # 4. Return the final array of the shape (n,2)
        # fill_in
    return merged_features

def gaus_mixture(data, n_components):

    """Performs gaussian mixture model clustering.

    Args:
      data: an n-by-2 numpy array of numbers with n data points
      n_components: a list of digits that are possible candidates for the number of clusters to use

    Returns:
      A single digit (which is an element from n_components, i.e., the optimal number of clusters) that results in the lowest
      BIC when it is used as the number of clusters to fit a GMM

    """

    # initialize best number of clusters to first element in n_components by
    # (1) fitting a GMM on `data` using the first element in `n_components` as the number
    # of clusters (remember to set random_state=0 when you call GaussianMixture()),
    # (2) calculating the bic on `data` and making it the best bic, and (3) setting the
    # corresponding number of cluster (i.e., the first element of `n_components`
    # as the best number of clusters
    gm = GaussianMixture(n_components=n_components[0], random_state=0)
    gm.fit(data) # fill in
    best_bic = gm.bic(data)# fill in
    best_no_clusters = n_components[0]# fill in

    # for all different k values in n_components, make GMM model and calculate BIC
    for k in n_components:

        gm = GaussianMixture(n_components=k, random_state=0)
        gm.fit(data)

        # calculate BIC
        bic = gm.bic(data)

        # if current BIC is lowest, make it the best BIC and make its corresponding k the best_no_clusters
        if bic < best_bic:
            best_bic = bic
            best_no_clusters = k

        # fit GMM (remember to set random_state=0 when you call GaussianMixture())

        # calculate BIC

        # if current BIC is lowest, make it the best BIC and make its corresponding k the best_no_clusters


    return best_no_clusters


if __name__ == "__main__":
    # load data and reshape to work with GMM implementation
    X1 = np.genfromtxt('gmm_data_x1.csv', delimiter=',')
    X2 = np.genfromtxt('gmm_data_x2.csv', delimiter=',')

    print("Shape of the first feature array: ", X1.shape)
    print("Shape of the second feature array: ", X2.shape)


    # Concatenate individual feature arrays into a single numpy array
    X = concatenate_features(X1,X2)

    print("Shape of the concatenated array: ", X.shape, "\n")

    # call function and get output
    best_k = gaus_mixture(data=X, n_components=[2, 3, 4, 5, 6, 7, 8])
    print('Best fit is when k = %d clusters are used' % (best_k))
