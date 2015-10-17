class node():
    def __init__(self,value,left,right):
    	self.value = value 
    	self.left = left
        self.right = right
    def __str__(self):
    	return self.value

e = node("e", None, None)
g = node("g", None, None)
m = node("m", None, None)
t = node("t", None, None)
a = node("a", e, g)
e = node("e", m, None)
h = node("h", t, None)
O = node("!", a, e)  
P = node(":)", h, O) 
root = P

# ! and :) cannot be the name,so i name them O and P

def DFS(node):
	if node.left:
		DFS(node.left)
	if node.right:
		DFS(node.right)
	print node,

DFS(root)