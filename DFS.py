class node():
    def __init__(self,value,left,right):
    	self.value = value 
    	self.left = left
        self.right = right
    def __str__(self):
    	return self.value

# e = node("e", None, None)
# g = node("g", None, None)
# m = node("m", None, None)
# t = node("t", None, None)
# a = node("a", e, g)
# e = node("e", m, None)
# h = node("h", t, None)
# O = node("!", a, e)  
# P = node(":)", h, O) 
# root = P
# # ! and :) cannot be the name,so i name them O and P

g = node("G", None, None)
f = node("F", g, None)
e = node("E", None, None)
d = node("D", None, e)
c = node("C", None, None)
b = node("B", c, d)  
a = node("A", b, f) 
root = a

# pre_order
def DFS(node):
	print node,
	if node.left:
		DFS(node.left)
	if node.right:
		DFS(node.right)

# in_order
def DFS(node):
	if node.left:
		DFS(node.left)
	print node,
	if node.right:
		DFS(node.right)
		
# post_order
def DFS(node):
	if node.left:
		DFS(node.left)
	if node.right:
		DFS(node.right)
	print node,

DFS(root)
