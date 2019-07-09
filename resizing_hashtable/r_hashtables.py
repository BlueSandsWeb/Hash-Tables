

# Linked List hash table key/value pair
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Fill this in
# Resizing hash table
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0


# Research and implement the djb2 hash function
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return hash % max


# Fill this in.
# Hint: Used the LL to handle collisions
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    newPair = LinkedPair(key, value)
    # check if something already where you want to put key value pair by index
    if hash_table.storage[index] is not None:  # Best case scenerio is the else
        # set the node we're checking to be the head of the linked list
        node = hash_table.storage[index]
        # check each item in the linked list
        while True:                                 # Loop over the linked list starting at the head node
            # if linked list item key == key
            if node.key == key:                     # check if key is key we're looking for
                # change value
                # change value since it's the key you're looking for
                node.value = value
                return value
            else:                                   # this is not the key you're looking for *waves hand
                if node.next is None:               # is current node the end of the line?
                    # make a new node
                    newNode = LinkedPair(key, value)    # Make new node
                    # change node.next to be new node
                    node.next = newNode                 # add new node to the end of the linked list
                    hash_table.count += 1
                    print(hash_table.count)
                    print("newNode: ", newNode.value)
                    return newNode                      # return to leave while loop
                else:
                    # set node = node.next
                    node = node.next                 # change current node to next node for next loop
                    # loop again
    else:
        # insert key and value pair into a hash table
        hash_table.storage[index] = newPair
        print(hash_table.storage)
        print("inserted: ", hash_table.storage[index].value)
        hash_table.count += 1
        print(hash_table.count)
        return hash_table.storage[index]


# Fill this in.
# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
    # get index item should be at
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        node = hash_table.storage[index]
        # if node's key at index == key we're looking for
        if hash_table.storage[index].key == key:
            if node.next is None:
                hash_table.storage[index] = None
                hash_table.count -= 1
                print(hash_table.count)
                return node.value
            else:
                hash_table.storage[index] = node.next
                hash_table.count -= 1
                print(hash_table.count)
                return node.value

        else:  # check nodes down the linked list
            prev_node = hash_table.storage[index]
            node = hash_table.storage[index].next
            while node is not None:
                if node.key == key:
                    # set previous node's .next to be current node.next
                    prev_node.next = node.next
                    node.next = None
                    hash_table.count -= 1
                    print(hash_table.count)
                    return node.value
                else:
                    prev_node = node
                    node = node.next
    else:
        return None

# Fill this in.
# Should return None if the key is not found.


def hash_table_retrieve(hash_table, key):
    # hash the key to find the index
    index = hash(key, hash_table.capacity)
    # check the array at that index and see if there's anything there
    if hash_table.storage[index] is not None:
        node = hash_table.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            else:
                # move on to next node
                node = node.next
    else:
        return None


# Fill this in
def hash_table_resize(hash_table):
    # Make new array
    # loop over old array
    # grab first none item in array item, remove from old array
    # add to new array
    # Don't forget to rehash all the keys
    pass


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(f"retrieve: {hash_table_retrieve(ht, 'line_1')}")
    print("retrieve: ", hash_table_retrieve(ht, "line_2"))
    print("retrieve: ", hash_table_retrieve(ht, "line_3"))
    print("retrieve: ", hash_table_retrieve(ht, "line_4"))

    print('remove line_4', hash_table_remove(ht, 'line_4'))
    print('remove line_3', hash_table_remove(ht, 'line_3'))
    print('remove line_2', hash_table_remove(ht, 'line_2'))
    print('remove line_1', hash_table_remove(ht, 'line_1'))
    print(ht.storage)

    # old_capacity = len(ht.storage)
    # ht = hash_table_resize(ht)
    # new_capacity = len(ht.storage)

    # print("Resized hash table from " + str(old_capacity)
    #       + " to " + str(new_capacity) + ".")


Testing()
