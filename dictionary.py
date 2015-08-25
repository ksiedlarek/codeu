import pytest


class Entry(object):

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __getitem__(self, key):
        return self.key

    def __str__(self):
        return str(self.key)


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.content = [[] for i in range(size)]

    def get(self, key):
        index = self.hash_function(key)
        for pair in self.content[index]:
            for entry in pair:
                if entry.key == key:
                    return True
        return False


    def create(self, key, data):
        entry = Entry(key, data)
        index = self.hash_function(key)
        self.content[index].append([entry])


    def hash_function(self, key):
        sum_of_letters = 0
        for letter in key:
            sum_of_letters += ord(letter)
        sum_of_letters += ord(key[0])
        return int(sum_of_letters % self.size)

    def __iter__(self):
        return iter(self.content)

table = HashTable(100)
table.create('chair', 'a tool to sit on')
table.create('riahc', 'nonsense')
table.create('cat', 'small animal')

def test_simple_word():
    assert table.get('cat') == True

def test_not_in_dict():
    assert table.get('notinside') == False

def test_anagram():
    assert table.get('chair') == True
    assert table.get('riahc') == True
