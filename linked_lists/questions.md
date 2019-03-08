1. Write code to remove duplicates from an unsorted linked list
```python
class ElemSLL:
    def __init__(self, data):
        self.next = None
        self.data = data

def remove_dups(head: ElemSLL) -> ElemSLL:
    seen = set([])
    next_to_see = head
    prev_distinct = None
    while ( next_to_see is not None ):
        if (next_to_see.data in seen):
            # skip this node
            prev_distinct.next = next_to_see.next
        else:
            # increment the prev_distinct pointer to the current element
            prev_distinct = next_to_see
            # add the most recently added distinct value to the set so as to not add duplicates
            seen.add(next_to_see.data)  
        next_to_see = prev_distinct.next
    return (head)
```

```C++
#include <iostream>
#include <unordered_set>
using namespace std;

// Data Structure to store a linked list node
struct Node
{
	int data;
	Node* next;
};

// Helper function to print given linked list
void printList(Node* head)
{
	Node* ptr = head;
	while (ptr)
	{
		cout << ptr->data << " -> ";
		ptr = ptr->next;
	}

	cout << "null";
}

// Helper function to insert a new node in the beginning of the linked list
void push(Node** headRef, int data)
{
	Node* newNode = new Node();

	newNode->data = data;
	newNode->next = *headRef;
	*headRef = newNode;
}

// Function to remove duplicates from a sorted list
void RemoveDuplicates(Node* head)
{
	Node* previous = nullptr;
	Node* current = head;

	// take an empty set to store linked list nodes for future reference
	unordered_set<int> set;

	// do till linked list is not empty
	while (current != nullptr)
	{
		// if current node is seen before, delete it
		if (set.find(current->data) != set.end())
		{
			previous->next = current->next;
			delete current;
		}
		else
		{
			// insert current node into the set and proceed to next node
			set.insert(current->data);
			previous = current;
		}
		current = previous->next;
	}
}

// main method to remove remove duplicates from list
int main()
{
	// input keys
	int keys[] = {5, 3, 4, 2, 5, 4, 1, 3};
	int n = sizeof(keys)/sizeof(keys[0]);

	// points to the head node of the linked list
	Node* head = nullptr;

	// construct linked list
	for (int i = n-1; i >= 0; i--)
		push(&head, keys[i]);

	RemoveDuplicates(head);

	// print linked list
	printList(head);

	return 0;
}
```

2. Find the kth to last element of a singly linked list. If k == 1, then last element is needed. If k == 2 then second last element is needed

```python
class ElemSLL:
    def __init__(self, data):
        self.next = None
        self.data = data

def get_kth_to_last(head: ElemSLL , k:int) -> ElemSLL:
    if head is None:
        return (head)
    tail: ElemSLL = head
    for i in range(k):
        tail = tail.next
    while (tail is not None):
        tail = tail.next
        head = head.next
    return (head)
```

3. Delete middle node
```python
def del_spec_elem(head, elem):
    if (head == elem):
        return (head.next)
    else:
        prev = head
        cur = prev.next
        while (cur != elem) and (cur is not None):
            prev = prev.next
            cur = cur.next
        if cur is not None:
            prev.next = cur.next
    return (head)
```

4. Partition a SLL with a value
```python
def partition_sll_value(head, part_data):
    less_sll = None
    less_tail = None
    more_sll = None
    more_tail = None
    while ( head is not None ):
        if (head.data < part_data):
            # add to less
            if (less_tail is None):
                less_tail = head
                less_sll = less_tail
            else:
                less_tail.next = head
                less_tail = head
        else:
            # add to end of more
            if (more_tail is None):
                more_tail = head
                more_sll = more_tail
            else:
                more_tail.next = head
                more_tail = head
        head = head.next
    if less_tail is not None:
        less_tail.next = None
    if more_tail is not None:
        more_tail.next = None
    if (less_sll is None):
        return (more_sll)
    elif (more_sll is None):
        return (less_sll)
    else:
        # check less_tail.next should be None
        less_tail.next = more_sll
        return (less_sll)
```

4. [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
```C++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int carry = 0;
        ListNode* head_store_in = nullptr;
        ListNode* store_in = nullptr;
        
        while ( (l1 != nullptr) || (l2 != nullptr) || (carry != 0))
        {
            // this will be a non zero value
            int sum_val = carry ;
            if (l1 != nullptr){
                sum_val += l1->val;
            }
            if (l2 != nullptr){
                sum_val += l2->val;
            }
            carry = sum_val / 10;
            sum_val = sum_val % 10;
            // store value
            if (head_store_in == nullptr){
                head_store_in = new ListNode(sum_val);
                store_in = head_store_in;
            } else {
                store_in->next = new ListNode(sum_val);
                store_in = store_in->next;
            }
            // increment pointers
            if (l1 != nullptr){ l1 = l1->next; }
            if (l2 != nullptr){ l2 = l2->next; }
        }
        return (head_store_in);
    }
};
```