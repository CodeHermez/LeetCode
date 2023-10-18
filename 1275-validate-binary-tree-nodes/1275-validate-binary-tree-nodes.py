class Solution(object):

    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        self.vect = []
        i = 0
        arr = []
        for x in leftChild:
            if x>-1:
                i+=1
                arr.append(x)
        
        for x in rightChild:
            if x>-1:
                i+=1
                arr.append(x)

        if i+1 != n or (len(set(arr)) != len(arr)):
            return False

        val = 0 
        self.traversal(leftChild, rightChild,val,n)
        print("vect:", self.vect,"\n")
        set_list = set(self.vect)
        if(len(set_list) != len(self.vect)):
            return False
        else:
            return True
    
    def traversal(self, left, right, value,n):
        if(len(self.vect)>n):
            return
        if value != -1:
            print("value: ", value,"\n")
            print("value: ",value,"left: ",left[value],"right: ",right[value])
            self.vect.append(value)
            self.traversal(left, right, left[value],n)
            self.traversal(left, right, right[value],n)