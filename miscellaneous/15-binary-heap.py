class BinaryHeap(object):
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    # 삽입 시 실행, 반복 구조 구현
    def _percolate_up(self):
        i = len(self)
        parent = i // 2
        while parent > 0:
            if self.items[i] < self.items[parent]:
                self.items[parent], self.items[i] = \
                    self.items[i], self.items[parent]
            i = parent
            parent = i // 2

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    # 추출 시 실행, 재귀 구조 구현
    def _percolate_down(self, idx):
        left = idx * 2
        right = idx * 2 + 1
        smallest = idx

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left

        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != idx:
            self.items[idx], self.items[smallest] = \
                self.items[smallest], self.items[idx]
            self._percolate_down(smallest)

    def extract(self):
        extracted = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self._percolate_down(1)
        return extracted


b = BinaryHeap()

# 삽입
b.insert(5)
b.insert(9)
b.insert(17)
b.insert(27)
b.insert(11)
b.insert(14)
b.insert(21)
b.insert(33)
b.insert(19)
b.insert(18)
print(b.items)

# 추출
for _ in range(5):
    print(b.extract(), end=' ')
