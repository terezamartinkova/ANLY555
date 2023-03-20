#-------------------------------
#Consider the following. A matrix of size mxn will require mn memory buckets to store mn elements. Thus all resulting operations on the matrix will be affected by this standard but restrictive representation. 
#For example matrix addition will require mn time proportionally. This is reasonable in many cases, however, consider cases where a matrix is very sparse. A sparse matrix is a matrix where the majority of the 
#entries are zero. In this case, traversing all mn entries is unncessary and thus computationally inefficient. We need only add non-zero elements. 

#Recall from your discussion this week where you were tasked with designing a Sparse Matrix Class which supports matrix addition.  Your goal was to make as addition efficient as you can while considering both 
#space complexity and time complexity. 
#-------------------------------


# 1.  Assuming that two SparseMatrices (A and B) are compatible for addition, and both are m x n, derive a Step Count Function Tsparse(a,b). Determine the step counts in term of the size of the input (that is,
# the number of non-zero entries in A and B). You can assume the number of non-zero entries in A is a and the number of non-zero entries in B is b.

import numpy as np

class SparseMatrix:

    def __init__(self): #0 (definition is 0)
        pass

    # In this first part we attepmt to prove that the matrices are comaptiable for adition to see how would that be reflected on multiplication
    def Tsparse(self, A,B): #0 (defintion is 0 )
        a=0; #1 (initializing takes 1 step)
        b=0; #1 (intializing takes 1 step)
        # first looping over A matrix to find out if they are non-zero values
        for e in A: #2n (initalizing for loop and starting iteration takes 2n steps when n is a number of iterations)
            for f in e: #4n^2 (nested for loop is same as normal for loop, only times the previous that this one is nested in)
                if f !=0: #4n^2 #4n^2 (nested for loop is same as normal for loop, only times the previous that this one is nested in)
                    a+=1; #4n^2 (everything in nested for loop has the same step count if it was 1 without the loop)
        
        # then looping over B matrix to find out if they are non-zero values
        for e in B: #2n (initalizing for loop and starting iteration takes 2n steps when n is a number of iterations)
            for f in e: #4n^2 #4n^2 (nested for loop is same as normal for loop, only times the previous that this one is nested in)
                if f !=0: #4n^2 #4n^2 (nested for loop is same as normal for loop, only times the previous that this one is nested in)
                    b+=1; #4n^2 (everything in nested for loop has the same step count if it was 1 without the loop)
        # returning the addition of a and b values 
        return a+b #0
    
     # T(n) = 0+0+1+1+2n+4n^2+4n^2+4n^2+2n+4n^2+4n^2+4n^2+0 
     # T(n) = (4n^2)*6 + (2n)*2 + 2 = 24n^2 + 4n + 2
     # O(n) = n^2
    
    #2. Assuming that two standard Matrices (A and B) are compatible for addition, and both are m x n, derive a Step Count Function Tstandard(m,n).
    
    def Tstandard(self, m,n): #0
        return m*n #0
    # The step count function would be the same +1 as we first need iterate over the loops to find the dimensions of the array , which we can then assing to M,N
    # # We need to add one step assigning the value to M,N, therefore the final step count function would be: 
    # T(n) = 0+0+1+1+2n+4n^2+4n^2+4n^2+2n+4n^2+4n^2+4n^2+1+0 
    # T(n) = (4n^2)*6 + (2n)*2 + 2 = 24n^2 + 4n + 3
    # O(n) = n^2

if __name__ == "__main__":
    A=np.array([[1],[2],[3],[4]])
    B=np.array([[5],[6],[7],[8]])
    C=np.array([[10],[11],[12],[13],[14]])
    D=np.array([[15],[16],[17],[18],[19]])
    E=np.array([[21],[22],[23],[24],[25],[26]])
    F=np.array([[25],[26],[27],[28],[29],[30]])
    # it doesnt matter which array we choose, to be compatiable for addition they will have the same dimensions
    m,n=A.shape
    o,p=C.shape
    q,r=F.shape


#OBSERVE. Using a sparse matrix implementation is only beneficial when the number of non-zero entries is small relative to the size of the matrix. But what is that relative number precisely???

#3. Compare Tstandard(m,n) to Tsparse(a,b) to determine the value of a or b (relative to mn), when the SparseMatrix implementation loses its benefits. 

#Hint: Set Tstandard(m,n) > Tsparse(a,b), and solve for a or b in terms of m and n.

# considering the same input for both matrices, which function outputs higher value? 
    #Tsparse
    print(SparseMatrix().Tsparse(A,B))
    print(SparseMatrix().Tsparse(C,D))
    print(SparseMatrix().Tsparse(E,F))
    #Tstandard
    print(SparseMatrix().Tstandard(m,n))
    print(SparseMatrix().Tstandard(o,p))
    print(SparseMatrix().Tstandard(q,r))

# If using Sparse Matrix as a function, we can see that that the Tstandard function would be always hald of the output of the original Tsparse function.
# Therefore, we can see that T snadard is always smaller than Tsparse
