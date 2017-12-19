class Tree:
    def __init__(self, label, branches=[]):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)
        self.parent = None 

    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str)

    def is_leaf(self):
        return not self.branches
    
    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()

#ideas: add/delete/update leaf; move left/right in level; track level #consider making branches a linked list
def update(t):
    new_val = input("Enter new leaf value: ")
    t.label = new_val

def add(t):
    val = input("Enter leaf value: ")
    t.branches.append(Tree(val, t))

def move(t):
    direction = input("Move up/down/left/right: ")
    if direction == "down":
        if not t.branches:
            print("Cannot move down")
        else:
            t.parent, t = t, t.branches[0]
    if direction == "up":
        if t.parent == None:
            print("Cannot move up")
        else:
            t = t.parent


    
        

def execute():
    tree = Tree(None)
    pointer = tree 
    index = 0
    while True:
        
        command = input(">>")

        if command == "update":
            update(pointer)

        elif command == "add":
            add(pointer)
        
        elif command == "move":
            move(pointer)

        
        print(tree.__repr__())
        
            
#execute()

