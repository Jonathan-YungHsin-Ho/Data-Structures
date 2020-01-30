Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?

> The runtime complexity of `enqueue` is `O(1)`.

2. What is the runtime complexity of `dequeue`?

> The runtime complexity of `dequeue` is `O(1)`.

3. What is the runtime complexity of `len`?

> The runtime complexity of `len` is `O(1)`.

## Binary Search Tree

1. What is the runtime complexity of `insert`?

> The runtime complexity of `insert` is `O (log n)`. If the BST were poorly formed, if it were to approximate a singly-linked list, then there would be a worst case runtime complexity of `O(n)` if the whole tree had to be traversed to insert a new leaf.

2. What is the runtime complexity of `contains`?

> The runtime complexity of `contains` is `O(log n)`. If the BST were poorly formed, if it were to approximate a singly-linked list, then there would be a worst case runtime complexity of `O(n)` if the whole tree had to be traversed to find a target value.

3. What is the runtime complexity of `get_max`?

> The runtime complexity of `get_max` is `O(log n)`. If the BST were poorly formed, if it were to approximate a singly-linked list, then there would be a worst case runtime complexity of `O(n)` if the whole tree had to be traversed to find the max value.

## Heap

1. What is the runtime complexity of `_bubble_up`?

> The runtime complexity of `_bubble_up` is `O(log n)`.

2. What is the runtime complexity of `_sift_down`?

> The runtime complexity of `_sift_down` is `O(log n)`.

3. What is the runtime complexity of `insert`?

> The runtime complexity of `insert` is `O(log n)`.

4. What is the runtime complexity of `delete`?

> The runtime complexity of `delete` is `O(log n)`.

5. What is the runtime complexity of `get_max`?

> The runtime complexity of `get_max` is `O(1)`.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

> The runtime complexity of `ListNode.insert_after` is `O(1)`.

2. What is the runtime complexity of `ListNode.insert_before`?

> The runtime complexity of `ListNode.insert_after` is `O(1)`.

3. What is the runtime complexity of `ListNode.delete`?

> The runtime complexity of `ListNode.delete` is `O(1)`.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?

> The runtime complexity of `DoublyLinkedList.add_to_head` is `O(1)`.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?

> The runtime complexity of `DoublyLinkedList.remove_to_head` is `O(1)`.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?

> The runtime complexity of `DoublyLinkedList.add_to_tail` is `O(1)`.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?

> The runtime complexity of `DoublyLinkedList.remove_from_tail` is `O(1)`.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?

> The runtime complexity of `DoublyLinkedList.move_to_front` is `O(1)`.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?

> The runtime complexity of `DoublyLinkedList.move_to_end` is `O(1)`.

10. What is the runtime complexity of `DoublyLinkedList.delete`?

> The runtime complexity of `DoublyLinkedList.delete` is `O(1)`.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    The doubly linked list's `delete` method generally performs better than the JS `Arr.splice` method.
