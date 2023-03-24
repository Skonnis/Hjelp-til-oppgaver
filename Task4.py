class BinarySearchTree:

    def __init__(self, value=None):
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None
    
    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()

        elif value < self.value:
            self.left_child.insert(value)

        elif value > self.value:
            self.right_child.insert(value)
        
    def compute_sum(self):
        if self.is_empty():
            return 0
        sum = self.value
        for child in [self.left_child, self.right_child]:
            sum += child.compute_sum()
        return sum
    
    def compute_count(self):
        if self.is_empty():
            return 0
        count = 1
        for child in [self.left_child, self.right_child]:
            count += child.compute_count()
        return count

my_tree = BinarySearchTree()

my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)

print("sum:", my_tree.compute_sum())
print("number of nodes:", my_tree.compute_count())
