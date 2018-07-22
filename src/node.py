import sets


class Node(object):

    def __init__(self, depth, root=False):
        self.depth = depth

        if root:
            self.value = '__'
            self.num_children = 2
        else:
            self.value, self.num_children = sets.random_value()

        self.left = None
        self.right = None

        #print('GENERATION   -   ', self.depth, self.value, self.num_children)

        if self.num_children == 2:
            self.left = Node(depth + 1)
            self.right = Node(depth + 1)
        elif self.num_children == 1:
            self.left = Node(depth + 1)
    # end def __init__

# end class Node
