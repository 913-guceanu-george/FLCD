class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.keys = list()

    def hash(self, key) -> int:
        a = 0
        for i in key:
            a += ord(i)
        return a % self.size

    def insert(self, key, value) -> None:
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
            self.keys.append(key)

    def search(self, key):
        hash_key = self.hash(key)
        bucket = self.table[hash_key]
        for _, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
        return -1

    def delete(self, key) -> None:
        hash_key = self.hash(key)
        key_exists = False
        bucket = self.table[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            self.keys.remove(key)

    def __str__(self):
        return str(self.table)

    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, value):
        self.insert(key, value)
