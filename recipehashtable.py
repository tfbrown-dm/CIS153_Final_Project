class RecipeChainingHashTableItem:
    def __init__(self, item_key, item_value):
        self.key = item_key
        self.value = item_value
        self.next = None

class RecipeHashTable:
    def __init__(self, initial_capacity=11):
        self.table = [None] * initial_capacity

    # Return non-negative key
    def hash(self, key):
        return abs(hash(key))

    # Searches for the item with the key
    # Returns item's value if found, None if not
    def get(self, key):
        
        bucket_index = self.hash(key) % len(self.table)

        # Search linked list for key
        item = self.table[bucket_index]
        while item != None:
            if key == item.key:
                return item.value
            item = item.next

        return None

    def insert(self, key, value):
        bucket_index = self.hash(key) % len(self.table)

        # Search linked list. If key exisits in item, replace value. Otherwise insert.
        current_item = self.table[bucket_index]
        previous_item = None

        while current_item != None:
            if key == current_item.key:
                current_item.value = value
                return True
            previous_item = current_item
            current_item = current_item.next

        # Add to linked list
        if self.table[bucket_index] == None:
            self.table[bucket_index] = RecipeChainingHashTableItem(key, value)
        else:
            previous_item.next = RecipeChainingHashTableItem(key, value)
        return True