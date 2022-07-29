class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent  

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

    def add_child(self, child):
        child.parent = self
        self.children.append(child)            

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("MAC"))
    laptop.add_child(TreeNode("ROG")) 

    mobile = TreeNode("Mobile")
    mobile.add_child(TreeNode("RealMe"))
    mobile.add_child(TreeNode("RedMi"))
    mobile.add_child(TreeNode("Iphone"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)    
    root.add_child(mobile)    
    root.add_child(tv)

    root.print_tree()    

if __name__=='__main__':
    build_product_tree()