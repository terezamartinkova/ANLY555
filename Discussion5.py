### Student: Tereza Martinkova
### Class: ANLY 555-01
### Date: April 2, 2023
###-------------------------------------------------------

class BinHeap:
    def __init__(self, heap):
        self.heapList = [0]
        self.currentSize = 0
        self.heap = heap


    def percUp(self,i):
        while i // self.heap > 0:
          if self.heapList[i] < self.heapList[i // self.heap]:
             tmp = self.heapList[i // self.heap]
             self.heapList[i // self.heap] = self.heapList[i]
             self.heapList[i] = tmp
          i = i // self.heap

    def insert(self,k):
      self.heapList.append(k)
      self.currentSize = self.currentSize + 1
      self.percUp(self.currentSize)

    def percDown(self,i):
      while (i * self.heap) <= self.currentSize:
          mc = self.minChild(i)
          if self.heapList[i] > self.heapList[mc]:
              tmp = self.heapList[i]
              self.heapList[i] = self.heapList[mc]
              self.heapList[mc] = tmp
          i = mc

    def minChild(self,i):
      if i * self.heap + 1 > self.currentSize:
          return i * self.heap
      else:
          if self.heapList[i*self.heap] < self.heapList[i*self.heap+1]:
              return i * self.heap
          else:
              return i * self.heap + 1

    def delMin(self):
      retval = self.heapList[1]
      self.heapList[1] = self.heapList[self.currentSize]
      self.currentSize = self.currentSize - 1
      self.heapList.pop()
      self.percDown(1)
      return retval

    def buildHeap(self,alist):
      i = len(alist) // self.heap
      self.currentSize = len(alist)
      self.heapList = [0] + alist[:]
      while (i > 0):
          self.percDown(i)
          i = i - 1

# Define function here

    def __str__(self):
        def helper_fun(node_index, levels):
            if node_index > self.currentSize:
                return ""
            else:
                output = ""
                output += helper_fun(self.heap*node_index+1, levels+1)
                output += "  "*levels + str(self.heapList[node_index]) + "\n"
                output += helper_fun(self.heap*node_index, levels+1)
                return output

        return helper_fun(1, 0)

def ordered_list(x):
   for i in range(len(x.heapList)-1):
      print(x.delMin())

bh1 = BinHeap(2)
bh1.buildHeap([9,5,6,2,3])
print('----Heap 1----')
ordered_list(bh1)

bh2 = BinHeap(3)
bh2.buildHeap([9,4,1,5,2,8,6,3])
print('----Heap 2----')
ordered_list(bh2)

bh3 = BinHeap(4)
bh3.buildHeap([7,6,3,2,8,9])
print('----Heap 3----')
ordered_list(bh3)

bh4 = BinHeap(5)
bh4.buildHeap([7,9,5,3,4,6,1])
print('----Heap 4----')
ordered_list(bh4)

bh5 = BinHeap(6)
bh5.buildHeap([3,8,1,5,2,9,6,7,4])
print('----Heap 5----')
ordered_list(bh5)

#-------------------------------------------
# Discussion for time complexity analysis. 
# One main goal associated with trees is improved 
# time complexity, but how is this related to the 
# branching factor? For example, are 2-ary heaps 
# more or less efficient than 5-ary heaps? 
# Propose an optimal value for n and justify your 
# proposition with an extensive discussion and explanation. 
#-------------------------------------------

## Discussion: 
# The branching factor is how many child nodes each node
# in the tree has. We want to see a high branching factor 
# because that means that the tree is well balanced and the 
# general paths are shorter. Therefore, higher branching factor
# also means a better time complexity. In this case our branching
# factor determins the number of nodes for each heap. When it
# comes to 2-ary vs 5-ary nodes, the difference is that a 2-ary 
# node will each have up to 2 children and the 5-ary will have up
# to 5 children. The important part of this time complexity analysis
# is the trade-off between memory space taken and efficiency due
# to its simplicity. We can see that in the above examples it seems
# like the optimal n in the n-ary would be 5.
