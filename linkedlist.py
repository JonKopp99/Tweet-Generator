class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []
        node = self.head
        while node != None:
            items.append(node.data)
            node = node.next
        return items

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.0(1)Because it is only checking one thing"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Worst and best Running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        # TODO: Loop through all nodes and count one for each
        curr = self.head #current node
        ctr = 0

        while curr:
            ctr += 1
            curr = curr.next
        return ctr

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Runs in constant time no loops or anything."""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        newNode = Node(item)
        curr = self.head
        if not curr:
            newNode.next = self.head
            self.head = newNode
            self.tail = newNode
        else:
            while curr.next:
                curr = curr.next
            curr.next = newNode
            self.tail = newNode


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Best and Worse Running time: O(1) because we only change the first node and dont go through all of them"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        newNode = Node(item)
        if self.head:
            newNode.next = self.head
            self.head = new_node
        else:
            self.append(newNode.data)


    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(1) If the first node == quality it will return.
        TODO: Worst case running time: O(n) If the last node == quality"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current = self.head

        while current:
            if quality(current.data):
                return current.data
            else:
                current = current.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(1) If the first node is the item to delete
        TODO: Worst case running time: O(n) If we have to loop through entire ll to find the node"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        curr = self.head
        previous = None
        found = False

        while curr and not found:
            if curr.data == item and curr is self.head:
                if self.head.next == None:
                    self.tail = None
                    self.head = None
                    found = True
                else:
                    self.head = curr.next
                    found = True
            elif curr.data == item:
                if curr == self.tail:
                    previous.next = None
                    self.tail = previous
                    found = True
                else:
                    previous.next = curr.next
                    found = True
            else:
                previous = curr
                curr = curr.next
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if found == False:
            raise ValueError('Item not found: {}'.format(item))

        return curr


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
