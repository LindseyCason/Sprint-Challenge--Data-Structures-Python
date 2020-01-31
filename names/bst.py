class BinarySearchTree:
    def __init__(self, value):
        self.value = value #because we are looking at an instance of a binary search tree, self.value will be the root.
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        #If the value is less than the root....
        if value < self.value:
            if not self.left: #and there is no left assigned...
                self.left=BinarySearchTree(value) #assign a new node with the value to the left of the root.
            else:
                self.left.insert(value) #This moves us down to the left node and calls insert again and will create a node of the value once it gets to a point where there is no left child
        else:
            if not self.right:
                self.right=BinarySearchTree(value)
            else:
                self.right.insert(value)

        
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        current = self
        while True:
            if target == current.value: #if target == value return true
                return True
            if target < current.value: #if target is less than value look left...
                if current.left: #if a left exists...
                    current = current.left #changes the value to the most left and loops up to compare again
                else:
                    return False  #if there is no left child return false
            else:
                if current.right: #if a right child exists
                    current = current.right #assign it to the current and compare it to the target
                else:
                    return False #if no right child return false.


    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right: #if there is no self.right just return where your current value (this could be 3 loops down the line), greater numbers will be to the right. When the rights run out, you've found your largest number
            return self.value
        elif self.right: #otherwise, if there is a right, call the function with the new value and repeat until there are no more rights.
            return self.right.get_max()


    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)#initial call

        if self.left:
            self.left.for_each(cb)#if we can go left go left and run for each passing in cb
        if self.right:
            self.right.for_each(cb)#if we can go right go right and run for each passing in cb