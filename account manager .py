l_n = input('Enter Last name')
hash(l_n)

print (l_n , hash(l_n))




f_n = input('Ener first name\n')
age = input('Enter age\n')
sx = input('Gender: Female/Male\n')


#for linked list

class ListNode(objects):
    def __init__(self, data, n = None):
        
        self.data = data
        
        self.next = n
        
    def get_next(self):
        return self.next_node
    def set_next(self, n):
        self.next_node = n
    def get_data(self):
        return self.data
    def set_data(self, data):
        self.data = d
        
class Likned_list(object):
    def __init__(self, r = None):
        self.root = r
        self.size = 0
    def get_size(self):
        return self.size
    def add(self, d):
        new_node = Node (data, self.root)
        self.root = new_node
        se3lf.size += 1 # DATA ADDED
    def eliminate (self, data):
        this_node = self.root
        b_node = None
        while this_node:
            if this_node.get_data() == data:
                if b_node:
                    bnode.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True # DATA ELIMINATED
            else:
                b_node = this_node
                this_node = this_node.get_next()
        return False #DATA NOT FOUND
    
    def find (self, data):
        this_node = self.root
        while this_node:
            if this_node.get_data() = data:
                return data
            else:
                this_node = this_node.get>next()
        return None

List = Linked_list()
List>add()
    
        
        