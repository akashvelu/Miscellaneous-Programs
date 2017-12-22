class Tree:
    count = 1
    def __init__(self, label, branches=[], parent = None, index = 0, depth = 0):
        for c in branches:
            assert isinstance(c, Tree)
        self.label = label
        self.branches = list(branches)
        self.parent = parent 
        self.id = Tree. count
        self.index = index 
        self.depth = depth
        Tree.count += 1
   
    def __repr__(self):
        if self.branches:
            branches_str = ', ' + repr(self.branches)
        else:
            branches_str = ''
        return 'Tree({0}{1})'.format(self.label, branches_str) 

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
    
    def is_leaf(self):
        return not self.branches 

def update(t):
    new_val = input("Enter new leaf value: ")
    t.label = new_val

def add(t):
    val = input("Enter leaf value: ")
    t.branches.append(Tree(val, [], t, len(t.branches), t.depth+1))

def delete(t):
    if t.parent == None:
        t.branches, t.label = [], None 
    else:
        for child in t.parent.branches[t.index+1:]:
            child.index -= 1
        t.parent.branches.pop(t.index)
        return t.parent.branches[t.index]



def move(t):
    direction = input("Move up/down/left/right: ")
    if direction == "up":
        if t.parent == None:
            print("Cannot move up")
            return t
        else:
            return t.parent
    elif direction == "down":
        if not t.branches:
            print("Cannot move down")
            return t
        else:
            return t.branches[0]
    elif direction == "right":
        if t.index+1 >= len(t.parent.branches):
            print("Cannot move right")
            return t
        else:
            return t.parent.branches[t.index+1]
    elif direction == "left":
        if t.index-1 < 0:
            print("Cannot move left")
            return t
        else:
            return t.parent.branches[t.index-1]    

    
def execute():
    tree = Tree(None)
    pointer = tree
    print("Possible commands: update/add/delete/move/print/location/current")
    print("Type 'help' for description of commands")

    while True:
        print()
        print(tree.__repr__())
        command = input("> ")
        if command == "update":
            update(pointer)
        elif command == "add":
            add(pointer)
        elif command == "move":
            pointer = move(pointer)
        elif command == "print":
            print(tree)
        elif command == "location":
            print("Depth: " + str(pointer.depth) + " index: " + str(pointer.index))
        elif command == "delete":
            pointer = delete(pointer)
        elif command == "current":
            print(pointer.label)

        else:
            print("Invalid command")
            
execute()
