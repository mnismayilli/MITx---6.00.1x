class node():
    def __init__(self,value,left,right):
    	self.value = value 
    	self.left = left
        self.right = right

    def __str__(self):
    	return self.value

    def __repr__(self):
    	return 'Node {}'.format(self.value)

def main():
	g = node("G", None, None)
	h = node("H", None, None)
	i = node("I", None, None)
	d = node("D", None, None)
	e = node("E", g, None)
	f = node("F", h, i)
	b = node("B", d, e)
	c = node("C", None, f)  
	a = node("A", b, c) 
	root = a
	BFS(root)


def BFS(root):
	nexts = [root]
	while nexts != []:
		current = nexts.pop(0)
		if current.left:
			nexts.append(current.left)
		if current.right:
			nexts.append(current.right)
		print current,

main()