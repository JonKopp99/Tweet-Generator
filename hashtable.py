from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(n^2) We have to loop through entire bucket and its contents to get the keys."""
        # Collect all keys in each bucket
        allKeys = []
        for bucket in self.buckets: #loop through buckets
            for key, value in bucket.items(): #loop through items in the bucket
                allKeys.append(key) #append the buckets keys
        return allKeys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(n^2) We have to loop through entire bucket and its contents to get the keys."""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        values = []
        for bucket in self.buckets: #Loop thorugh all the buckets
            for key, value in bucket.items(): #Loop through items in buucket
                values.append(value) #apend  the value to the values
        return values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(n) Loop though all the buckets once to get their items."""
        # Collect all pairs of key-value entries in each bucket
        allItems = []
        for bucket in self.buckets: #Loop through all the buckets
            allItems += (bucket.items()) #append the items from that bucket
        return allItems

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(n) Looping through the buckets to get each length of the buckets insides."""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        sum = 0
        for i in self.buckets:
            sum += i.length()
        return sum

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1)if we can assume that pythons find method is constant if its
        not constant time then most likely we can assume its O(N)at the greatest."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        i = self._bucket_index(key) #index
        bucket = self.buckets[i] #find bucket where its containted
        if(bucket.find(lambda item: item[0] == key)): #if item = key return true
            return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1)if we can assume that pythons find method is constant if its
        not constant time then most likely we can assume its O(N)at the greatest."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket = self.buckets[self._bucket_index(key)]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            return entry[1]
        else:
            raise KeyError('Key not found: {}'.format(key))


    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(1) O(1)if we can assume that pythons find method is constant if its
        not constant time then most likely we can assume its O(N)at the greatest."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        i = self._bucket_index(key) #index
        bucket = self.buckets[i]
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry is not None:
            bucket.delete(entry)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) O(1)if we can assume that pythons find method is constant if its
        not constant time then most likely we can assume its O(N)at the greatest."""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        i = self._bucket_index(key)#Index
        found = self.buckets[i].find(lambda item: item[0] == key) #item to look for
        if found:
            self.buckets[i].delete(found) #Delete found 
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
