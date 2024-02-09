from module5_mod import NumberIndexFinder

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
