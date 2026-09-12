r'''
    CENTER
    
    Assume we are given a binary tree, where each node is labeled with a
    unique label A-Z, and each node has a left and right child (which can 
    be None). We call a node a center of the tree if the removal of the node
    and its adjacent edges leaves the resulting (at most three) subtrees being
    of size at most half of the original tree. We assume a tree is represented
    by a recursive tuple (label, left subtree, right subtree).
    
    For example, in the below tree the node B is the unique center. 
    The original tree has size 6, and the three resulting subtrees by 
    removing B have sizes 2, 2, and 1.

            A
           / \
          B   F          A            C
         / \       ->     \      +     \     +    E
        C   E              F            D
         \
          D
          
        ('A',('B',('C',None,('D',None,None)),('E',None,None)),('F',None,None)) 

    Note that the center is not necessarily unique as both B and C are centers
    in the below example.

              A 
             /      
            B
           / 
          C
         /
        D

        ('A', ('B', ('C', ('D', None, None), None), None), None)

    Your task is to write a function centers(tree) that takes a tree and
    returns a sorted list of the labels of all possible centers of the tree.

    Input:  A single line containing a Python expression representing a tree.

    Output: A sorted list with all centers of the tree.

    Example:

      Input:  ('A', ('B', ('C', ('D', None, None), None), None), None)

      Ouput: ['B', 'C']

    Note: The below code already reads the input, calls the centers function,
          and prints the returned result.
'''


def centers(tree):
    def count_nodes(t):
      if not t:
          return 0
      elif isinstance(t,str):
          return 1
      else:
          return sum([count_nodes(node) for node in t])
    total_nodes=count_nodes(tree)
    
    def center_finder(tree,t_nodes):
        if not tree:
            return []
        if count_nodes(tree[1])<=t_nodes/2 and count_nodes(tree[2])<=t_nodes/2 and t_nodes-1-count_nodes(tree[1])-count_nodes(tree[2])<=t_nodes/2:
            return [tree[0]]+center_finder(tree[1],t_nodes)+center_finder(tree[2],t_nodes)
        else: 
           return center_finder(tree[1],t_nodes)+center_finder(tree[2],t_nodes)
        

    return sorted(center_finder(tree,total_nodes))




print(centers(eval(input())))
