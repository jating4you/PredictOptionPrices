# Bottom --> 10, 20, 30, 40, 50 --> Top

my_stack = [10, 20, 30, 40, 50] # List

my_stack.append (60) # The PUSH OPERATION

print (my_stack)
# New Stack: Bottom ---> 10, 20, 30, 40, 50, 60 ---> Top

my_stack.pop () # The POP OPERATION

my_stack.pop () # The same operation 'twice'

print (my_stack) # From the 'top', 50 and 60 will be removed.

from collections import deque

# This is your queue. "Roger Federer" is the first to arrive while "Novak Djokovic is the last.

my_queue = deque(["Roger Federer", "Rafael Nadal", "Novak Djokovic"])

my_queue.append ("Andre Agassi") # Now Andre Agassi arrives

my_queue.append ("Pete Sampras") # Now Pete Sampras arrives

print (my_queue) # You may have a look at the queue below
my_queue.popleft() # The second to arrive leaves now

my_queue.popleft()
print (my_queue) # This is your present queue in the order of arrival

my_graph = {'A' : ['B', 'C'], 'B': ['A','C','D'], 'C' : ['A','B','D','E'], 'D': ['B','C','E'], 'E': ['D','C']}

def define_edges(my_graph):
    edges = []
    for nodes in my_graph:
        for adjacent_nodes in my_graph [nodes]:
            edges.append((nodes, adjacent_nodes))
    return edges

print(define_edges(my_graph))
class Tree:
    def __init__(self, info, left=None, right=None):
        self.info = info
        self.left  = left
        self.right = right

    def __str__(self):
        return (str(self.info) + ', Left node: ' + str(self.left) + ', Right node: ' + str(self.right))

tree = Tree("Root Node", Tree("Branch_1", "Leave_1", "Leave_2"), Tree("Branch_2", "Leave_3", "Leave_4"))
print(tree)

new_dict = { } # Empty Dictionary

type (new_dict)
# Creating a new dictionary

new_dict = {'Jack': 2563, 'Rose': 8965, 'Hockley': 7412, 'Fabrizo':9632, 'Molly Brown': 4563}

type (new_dict)
# Printing the dictionary

print (new_dict)
print(new_dict ['Jack'])
new_dict ['Rose'], new_dict ['Hockley']
print(len (new_dict))
print(new_dict.keys ())
print(new_dict.values())
del new_dict ['Hockley']

print (new_dict)
new_dict.pop ('Fabrizo')
print (new_dict) # Our latest dictionary
sorted (new_dict)
print (new_dict) # Our latest dictionary
new_dict.clear ()
print (new_dict) # Our latest dictionary
new_tup = () # Empty Tuple
type (new_tup)
new_tup = (10, 20, 30, 40) # A tuple of integers
type (new_tup)
new_tup = (10, 20.2, 'thirty', 40) # A tuple of mixed data type
type (new_tup)
new_tup = ((10,20,30), (10.1, 20.2, 30.3),("ten", "twenty", "thirty")) # A nested tuple
type (new_tup)
new_tup = (10,(20.2,("thirty",(40)))) # A deeply nested tuple
type (new_tup)
my_tup = (10, 20, 30, 40)  # This is the 'original' tuple which you have created

print (my_tup)
my_tup [0] = "40" # Assigning a new item to the 0th index
my_tup.append (50) # Trying to Append '50' at the 4th index of the created tuple.
len (my_tup)
new_set = { } # Empty Set ---> An empty set cannot be created
type (new_set)
new_set = {'Neo', 'Morphius', 'Trinity', 'Agent Smith', 'Oracle'} # A new set
type (new_set)
print (new_set)
new_set = {'Neo', 'Morphius', 'Trinity', 'Agent Smith', 'Agent Smith', 'Agent Smith', 'Agent Smith', 'Oracle'}

print (new_set) # The set will only print unique value
x_set = set ('THEMATRIX')

type (x_set)
print (x_set) # 'THE MATRIX' has two 'T's. Only unique values will be printed.
x_set = set ('ABCDE')
y_set = set ('CDEFG')

print (x_set)
print (y_set)
x_set.union(y_set)
x_set.intersection(y_set)
x_set & y_set # Intersection can be performed by using the ampersand '&' operator
x_set.difference(y_set)
x_set - y_set # Difference can be performed using the minus '-' operator
x_set.difference_update(y_set)

print (x_set)
print (y_set)
x_set = set ('ABCDE')
y_set = set ('CDEFG')

x_set = x_set - y_set # Difference update can be abbreviated in the shown manner i.e. 'x = x-y'

print (x_set)
print (y_set)
x_set = set ('ABCDE')
y_set = set ('CDEFG')

x_set.isdisjoint(y_set)
x_set = set ('ABC')
y_set = set ('EFG')

x_set.isdisjoint(y_set)
x_set = set ('ABCDE')
y_set = set ('CDEFG')

y_set.issubset(x_set)
x_set = set ('ABCDE')
y_set = set ('CDE')

y_set.issubset(x_set)
y_set < x_set # One can check a subset using a less than '<' operator.
x_set = set ('ABCDE')
y_set = set ('CDEFG')

x_set.issuperset(y_set)
x_set = set ('ABCDE')
y_set = set ('CDE')

x_set.issuperset(y_set)
x_set > y_set # One can check a superset using a greater than '>' operator.
x_set = set ('ABCDE')

print (x_set)
x_set.add('FGH')

print (x_set)
x_set.discard('FGH')

print (x_set)
x_set.pop()
print (x_set) # There are only 4 items in the set, since one just got popped in the above cell execution.
x_set.copy()
print (x_set)