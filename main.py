import itertools

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# итератор
class FlatIterator:
    def __init__(self, some_list):
        self.some_list = some_list
        self.cursor = -1
        self.nest_cursor = 0
        self.list_len = len(self.some_list)

    def __iter__(self):
        self.cursor += 1
        self.nest_cursor = 0
        return self

    def __next__(self):
        while self.cursor - self.list_len and self.nest_cursor == len(self.some_list[self.cursor]):
            iter(self)
        if self.cursor == self.list_len:
            raise StopIteration
        self.nest_cursor += 1
        return self.some_list[self.cursor][self.nest_cursor - 1]


if __name__ == '__main__':
    for item in FlatIterator(nested_list):
        print(item)
    flat_list = [item for item in FlatIterator(nested_list)]
    print(flat_list)

    # генератор
    for i in itertools.chain.from_iterable(nested_list):
        print(i)
