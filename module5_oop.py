from collections import defaultdict

class NumberIndexFinder:
    def __init__(self, n):
        self.n = n
        self.idxMap = defaultdict(int)

    def insert_numbers(self):
        for i in range(1, self.n+1):
            cur = input("input a number: ")
            if cur not in self.idxMap:
                self.idxMap[cur] = i

    def find_number_index(self, target):
        if target in self.idxMap:
            return self.idxMap[target]
        else:
            return -1


def main():
    n = input("input positive number N: ")
    n = int(n)

    numIdx_finder = NumberIndexFinder(n)

    numIdx_finder.insert_numbers()

    x = input("input X to see its index: ")

    res = numIdx_finder.find_number_index(x)
    print(res)

if __name__ == "__main__":
    main()
