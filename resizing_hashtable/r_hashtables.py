
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
    if hash_table.count < int(hash_table.capacity * .2):
        hash_table_resize(hash_table)
    elif hash_table.count > int(hash_table.capacity * .7):
        hash_table_resize(hash_table)
    index = hash(key, hash_table.capacity)
    newPair = LinkedPair(key, value)
    if hash_table.storage[index] is not None:
        node = hash_table.storage[index]
        while True:
            if node.key == key:
                node.value = value
                return value
            else:
                if node.next is None:
                    newNode = LinkedPair(key, value)
                    node.next = newNode
                    hash_table.count += 1
                    print("newNode: ", newNode.value)
                    return newNode.value
                else:
                    node = node.next

    else:
        hash_table.storage[index] = newPair
        print(hash_table.storage[index].value)
        print("inserted!")
        hash_table.count += 1
        return hash_table.storage[index].value


# Fill this in.

# If you try to remove a value that isn't there, print a warning.
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        node = hash_table.storage[index]
        if hash_table.storage[index].key == key:
            if node.next is None:
                hash_table.storage[index] = None
                hash_table.count -= 1
                return node.value
            else:
                hash_table.storage[index] = node.next
                hash_table.count -= 1
                return node.value
        else:
            prev_node = hash_table.storage[index]
            node = hash_table.storage[index].next
            while node is not None:
                if node.key == key:
                    prev_node.next = node.next
                    node.next = None
                    hash_table.count -= 1
                    return node.value

                else:
                    prev_node = node
                    node = node.next
    else:
        return None


# Fill this in.

# Should return None if the key is not found.
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is not None:
        node = hash_table.storage[index]
        while node is not None:
            if node.key == key:
                return node.value
            else:
                node = node.next
    else:
        return None


# Fill this in
def hash_table_resize(hash_table):
    # make new array
    if hash_table.count < hash_table.capacity / 2:
        new_hash_table = HashTable(hash_table.capacity // 2)
    else:
        new_hash_table = HashTable(hash_table.capacity * 2)
    # loop over old array
    while hash_table.count > 0:
        print(f"resize running...")
        for i in hash_table.storage:
            if i is not None:
                print(f"i is... {i.key}")
                key = i.key
                value = i.value
                hash_table_remove(hash_table, key)
                hash_table_insert(new_hash_table, key, value)

    hash_table.capacity = new_hash_table.capacity
    hash_table.storage = new_hash_table.storage
    hash_table.count = new_hash_table.count
    # return hash_table
    print(f"ht in resize is... {new_hash_table.storage}")
    return new_hash_table
    # pick first item, remove from old array
    # add to new array
    # don't forget to rehash all the keys


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    # print(f"retrieve: ", {hash_table_retrieve(ht, "line_1")})
    # print(f"retrieve: ", {hash_table_retrieve(ht, "line_2")})
    # print(f"retrieve: ", {hash_table_retrieve(ht, "line_3")})

    # print('remove line_1', hash_table_remove(ht, "line_1"))
    # print('remove line_2', hash_table_remove(ht, "line_2"))
    # print('remove line_3', hash_table_remove(ht, "line_3"))
    print(ht.storage)

    old_capacity = len(ht.storage)
    print(f" ht testing is ... {ht}")
    ht = hash_table_resize(ht)
    print(f" ht testing 2 ... {ht}")
    new_capacity = len(ht.storage)
    print(f" ht testing 3 ... {ht}")
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
