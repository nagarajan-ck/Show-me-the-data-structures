class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)
    

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string
        
    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
    
def union(llist_1, llist_2):
    uniondict = dict()
    unionlist = LinkedList()
    node = llist_1.head
    while node:
        if(uniondict.get(node.value)):
            uniondict[node.value]= uniondict.get(node.value)+1
        else:
            uniondict[node.value]= 1
        
        node = node.next

    node = llist_2.head
    while node:
        if(uniondict.get(node.value)):
            uniondict[node.value]= uniondict.get(node.value)+1
        else:
            uniondict[node.value]= 1
        
        node = node.next

    
    for key in uniondict:
        unionlist.append(key)
    
        
    return unionlist
    
    
def intersection(llist_1, llist_2):
    
    intersectiondict = dict()
    intersectionlist = LinkedList()
    temp_dict = dict()
    
    node = llist_1.head
    while node:       
        temp_dict[node.value]= 1        
        node = node.next

    node = llist_2.head
    while node:
        if(temp_dict.get(node.value)):
            intersectiondict[node.value]= 1        
        node = node.next

    for key in intersectiondict:
        intersectionlist.append(key)
    
    return intersectionlist    



def settheory(element_1,element_2):

    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print("\nUnion:")
    print (union(linked_list_1,linked_list_2))

    print("Intersection:")
    print (intersection(linked_list_1,linked_list_2))

    
    
element_1 = [1,2,3,4,5]
element_2 = [1,2,3,4,5,6,7,8]
settheory(element_1,element_2)

'''
Union:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 
Intersection:
1 -> 2 -> 3 -> 4 -> 5 -> 
'''

element_1 = []
element_2 = [6,21,1]
settheory(element_1,element_2)

'''
Union:
6 -> 21 -> 1 -> 
Intersection:


'''

element_1 = [1]
element_2 = [1]
settheory(element_1,element_2)

'''
Union:
1 -> 
Intersection:
1 -> 
'''



