"""  list Node is as defined below:

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

"""

# complete this function
# return head of list after swapping
class Solution:    
    def pairWiseSwap(self, head):
        # code here
        if head is None or head.next is None:
            return head
        prev=None
        curr=head
        new_head=head.next
        
        while curr is not None and curr.next is not None:
            first_node=curr
            second_node=curr.next
            if prev:
                prev.next=second_node
            first_node.next=second_node.next
            second_node.next=first_node
            
            prev=first_node
            curr=first_node.next
        return new_head



#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
            
        dict1 = {}
        temp = lis.head
        while temp:
            dict1[temp] = temp.data
            temp = temp.next
        
        failure = LinkedList()
        failure.insert(-1)
        
        head = Solution().pairWiseSwap(lis.head)
        
        temp = head
        f = 0
        while temp:
            if dict1[temp] != temp.data:
                f = 1;
            temp = temp.next
        
        if f:
            printList(failure)
        else:
            printList(head)

# } Driver Code Ends