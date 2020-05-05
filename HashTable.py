class HashTable(object):
    def __init__(self):
        self.size = 10
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def hashFunction(self, key):
        sum = 0
        for i in range(len(key)):
            sum += ord(key[i])
        return sum % self.size

    def get(self, key):
        index = self.hashFunction(key)
        while self.keys[index]:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        return None

    def put(self, key, data):
        index = self.hashFunction(key)
        while self.keys[index]:
            if self.keys[index] == key:
                self.values[index] = data
                return
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = data


if __name__ == '__main__':
    table = HashTable()
    table.put("apple", 30)
    table.put("orange", 40)
    table.put("car", 10)
    table.put("tea", 20)

    print(table.get("orange")) # 40
    print(table.get("haha")) # None
