"""class student:
    def __init__(self,name,rollno,javamarks,pythonmarks,mathsmarks):
        self.name=name
        self.rollno=rollno
        self.javamarks=javamarks
        self.pythonmarks=pythonmarks
        self.mathsmarks=mathsmarks

    def printall(self):
        print(self.name)
        print(self.rollno)
        print(self.javamarks)
        print(self.pythonmarks)
        print(self.mathsmarks)


obj1=student("sridhar",120,80,70,60)
print(obj1.name)
print(obj1.rollno)
print(obj1.javamarks)
print(obj1.pythonmarks)
print(obj1.mathsmarks)

obj2=student("narendra",141,70,70,60)
print(obj2.name)
print(obj2.rollno)
print(obj2.javamarks)
print(obj2.pythonmarks)
print(obj2.mathsmarks)


obj3=student("raj",121,74,76,71)
print(obj3.name)
print(obj3.rollno)
print(obj3.javamarks)
print(obj3.pythonmarks)
print(obj3.mathsmarks)
    
obj=student("raj",121,74,76,71)
obj.printall()

obj=student("narendra",141,75,76,60)
obj.printall()

    """

#LINKED LIST

"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
obj1=Node(71)
obj2=Node(72)
obj3=Node(73)
obj4=Node(74)
obj5=Node(75)
obj6=Node(76)
obj7=Node(77)
obj8=Node(78)
obj9=Node(79)
obj10=Node(80)

obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10

currentnode=obj1
while currentnode !=None:
    print(currentnode.data)
    currentnode=currentnode.next"""




##Insertion at tail position in linked list

"""class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:

        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def insertAtTail(head, ele):
    temp = Node(ele)
    if head == None:
        return temp
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertAtTail(head, ele)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)"""


# 3 types of insertion codes

"""class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def printlinkedlist(head):
    currentNode=head
    while currentNode!= None:
        print(currentNode.data,end = "-->")
        currentNode=currentNode.next
print()

def insertattail(head,ele):
    temp=Node(ele)
    if head==None:
        return temp
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=temp
    return head
#task-1
def insertathead(head,ele):
    temp=Node(ele)
    temp.next=head
    return temp
#task-2
def insertatspecificposition(head,position,ele):
    if position==0:
        return insertathead(head,ele)
    
    temp=Node(ele)
    index=0
    currentNode=head

    while index!=position-1:
        currentNode=currentNode.next
        index+=1

    nextNode=currentNode.next
    temp.next=nextNode
    currentNode.next = temp 
    return head

nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = insertattail(head, ele)
print("Final linked list is:")
printlinkedlist(head)
 
head =insertatspecificposition(head, 3, 101)
printlinkedlist(head)"""


"""def deleteTailNode(head):  
    if head==None or head.next==None:
        return None
    previous=None
    currentNode=head
    while currentNode.next!=None:
        pervious=currentNode
        currentNode=currentNode.next
    previous.next=None
    return head"""

#STAKE IMPLEMENTATION

"""def push(stack,ele):
    stack.append(ele)
    print(ele,"inserted into stake successfully")

def pop(stack):
    if len(stack)==0:
        print("stack is empty")
        return
    print(stack[-1],"deleted successfully")
    stack.pop()

stack=[]
push(stack,10)
push(stack,20)
push(stack,30)
push(stack,40)
push(stack,50)

pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)
pop(stack)"""


#QUEUE IMPLEMENTATION

"""def enQueue(Q,ele):
    Q.append(ele)
    print(ele,"inserted into Queue")

def deQueue(Q):
    if len(Q)==0:
        print("Queue is empty")
        return
    print(Q[0],"is getting deleted")
    Q.pop(0)

Q=[]
enQueue(Q,10)
enQueue(Q,20)
enQueue(Q,30)
enQueue(Q,40)
enQueue(Q,50)

deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)
deQueue(Q)"""

"""def isbalanced(word):
    stack=[]
    for ele in word:
        if ele=='(':
            stack.append(ele)
        else:
            if len(stack)==0:
                return False
            else:
                stack.pop()
    if len(stack)==0:
        return True
    return False

word='((((())'
result=isbalanced(word)
print(result)"""


"""class Solution(object):
    def isValid(self,s):
        stack=[]
        openBrackets=["(","{","["]
        for ele in s:
            if ele in openBrackets:
                stack.append(ele)
            else:
                if len(stack)==0:
                    return False
                elif ele==')':
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        return False
                elif ele==']':
                    if stack [-1]=='[':
                        stack.pop()
                    else:
                        return False
                elif ele=='}':
                    if stack[-1]=='{':
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        return False
s = '{}()'
obj = Solution()
result=obj.isValid(s)
print(result)"""


#LINEAR SEARCH

"""nums=[0,10,20,30,40,50]
target=40
flag=-1
n=len(nums)
for index in range(n):
    if nums[index]==target:
        flag=index
        break
if flag==-1:
    print("not found")
else:
    print("target found at:",flag)"""


#BINARY SEARCH

"""nums=[10,20,30,40,50]
target=20
nums=sorted(nums)

left=0
right=len(nums)-1
flag=-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        flag=mid
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1

if flag==-1:
    print("target not found")
else:
    print("target found at index:",flag)""" 


#BUBBLE SORTING

"""`def performBubbleSort(nums):
    n=len(nums)
    fixThisIndex=n-1

    while fixThisIndex > 0:
        for index in range (fixThisIndex):
            if nums[index]>nums[index+1]:
                temp=nums[index]
                nums[index]=nums[index+1]
                nums[index+1]=temp
        print(nums)
        fixThisIndex -= 1

nums=[10,20,15,55,40,30,15]
print("before sorting:",nums)

performBubbleSort(nums)
print("after sorting:",nums)`"""


#SELECTION SORTING

"""def performSelectionSort(nums):
    n=len(nums)
    fixThisIndex=n-1
    while fixThisIndex > 0:
        maxEleIndex=fixThisIndex

        for index in range(fixThisIndex):
            if nums[index]>nums[maxEleIndex]:
                maxEleIndex=index

        if maxEleIndex != fixThisIndex:
            temp=nums[maxEleIndex]
            nums[maxEleIndex]=nums[fixThisIndex]
            nums[fixThisIndex]=temp
        print(nums)

        fixThisIndex -= 1

nums=[10,20,15,55,40,30,15]
print("before sorting:",nums)

performSelectionSort(nums)
print("after sorting:",nums)"""

#INSERTION SORTING

"""def performInsertionSort(nums):
    n=len(nums)
    lastEleInsortedArr=0
    for firstIndex in range(1,n):
        temp=nums[firstIndex]
        previous=lastEleInsortedArr

        while previous >= 0 and nums[previous]>temp:
            nums[previous+1]=nums[previous]
            previous -= 1
        nums[previous+1]=temp
        lastEleInsortedArr += 1

nums = [10, 8, 2, 14, 12, 7]

print("Before sorting:", nums)
 
performInsertionSort(nums)
 
print("After sorting:", nums)"""


#MERGE TWO SUBARRAYS
"""def mergetwosubarrays(nums,left,mid,right):
    temp=[]
    index1=left
    index2=mid+1
    while index1<=mid and index2<=right:
        if nums[index1]<nums[index2]:
            temp.append(nums[index1])
            index1 += 1
        else:
            temp.append(nums[index2])
            index2 += 1
    
    while index1 <= mid:
        temp.append(nums[index1])
        index1 += 1

    while index2 <= right:
        temp.append(nums[index2])
        index2 += 1

    position=left
    for ele in temp:
        nums[position]=ele
        position += 1

def mergeanddivide(nums,left,right):
    print(left,right)
    if left>=right:
        return
    mid=(left+right)//2
    mergeanddivide(nums,left,mid)
    mergeanddivide(nums,mid+1,right)
    mergetwosubarrays(nums,left,mid,right)

def performmergesort(nums):
    n=len(nums)
    mergeanddivide(nums,0,n-1)

nums=[10,8,20,12,7,6,5,11,60]

print("before sorting:",nums)

performmergesort(nums)

print("after sorting:",nums)"""


#TREE

"""class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printpreorder(root):
    if root==None:
        return
    print(root.data)

    printpreorder(root.left)

    printpreorder(root.right)


def printinorder(root):
    if root==None:
        return
    printinorder(root.left)

    print(root.data,end = ", ")

    printinorder(root.right)

def printpostorder(root):
    if root==None:
        return
    printpostorder(root.left)

    printpostorder(root.right)
     
    print(root.data,end=", ")

obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52)
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10   

printpreorder(obj1)
print()
printinorder(obj1)
print()
printpostorder(obj1)
print()"""


#LEVEL ORDER TRAVERSAL
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def printleveloredertraversal(root):
    if root == None:
        return
    Q=[root]
    result=[]
    while len(Q)>0:
        n=len(Q)
        subresult=[]
        for i in range(n):

            currNode=Q.pop(0)
            subresult.append(currNode.data)

            if currNode.left != None:
                Q.append(currNode.left)

            if currNode.right != None:
                Q.append(currNode.right)

        result.append(subresult)
    print(result)
obj1=Node(100)
obj2=Node(21)
obj3=Node(-151)
obj4=Node(87)
obj5=Node(12)
obj6=Node(52)
obj7=Node(8)
obj8=Node(27)
obj9=Node(28)
obj10=Node(7)

obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
obj3.right=obj7
obj4.right=obj8
obj5.right=obj9
obj7.left=obj10
printleveloredertraversal(obj1)
