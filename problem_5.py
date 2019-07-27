import hashlib
import datetime


class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None


class LinkedList:
    def __init__(self,head=None):
        self.head=head
        self.tail=self.head
    
    def append(self,node):
        if(self.head is None):
            self.head=node
            self.tail=self.head
            return
        self.tail.next=node
        self.tail = node
    

    def get_tail(self):
        return self.tail
    
    def print_tail(self):
        print("The tail node: ")
        node = self.tail
        if(node is None):
            print(None)
            
            return
        print("\nTime: "+str(node.value.timestamp)+"\nData: " + node.value.data +"\nPrevious Hash: "+str(node.value.previous_hash)+"\nHash: "+str(node.value.hash)+"\n")
    
    def print_Linked_List(self):        
        node = self.head
        count=0
        while node:
            print("Block "+str(count))
            print("\nTime: "+str(node.value.timestamp)+"\nData: " + node.value.data +"\nPrevious Hash: "+str(node.value.previous_hash)+"\nHash: "+str(node.value.hash)+"\n")
            node = node.next
            count+=1



class Block:

    def __init__(self, timestamp, data, previous_hash):
        
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
    
    def calc_hash(self):
        
        sha = hashlib.sha256()
        hash_str = self.data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


    
def find_previous_hash(linked_List):
    
    tail = linked_List.get_tail()
    if(tail):
        return linked_List.get_tail().value.hash
    else:
        return 0
        
        
    
linked_List = LinkedList()

linked_List.print_tail() #prints None as no blocks added

block0 = Block(datetime.datetime.utcnow(), "This is the first block", find_previous_hash(linked_List))
linked_List.append(Node(block0))

linked_List.print_tail() #prints the details of the first block as it is the tail

block1 = Block(datetime.datetime.utcnow(), "This is the second block", find_previous_hash(linked_List))
linked_List.append(Node(block1))

linked_List.print_tail() #prints the details of the second block as it is the tail

linked_List.append(None)
linked_List.print_tail() #prints None as the tail node is none