import numpy as np

array = np.random.rand(730, 20)

def getCovMatrix(array):
    X = np.zeros_like(array)
    for i in range(X.shape[0]):
        u = np.mean(array[i])
        X[i] = array[i] - u
    print(np.linalg.matrix_rank(X))
    XT = np.transpose(X)
    covMatrix = np.dot(X, XT)
    covMatrix = covMatrix / (X.shape[1])
    return covMatrix

print(np.linalg.matrix_rank(array))
covMatrix = getCovMatrix(array)
print(np.linalg.matrix_rank(covMatrix))