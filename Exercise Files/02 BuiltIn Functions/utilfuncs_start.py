# demonstrate built-in utility functions


def main():
    # use any() and all() to test sequences for boolean values
    list1 = [1, 2, 3, 4, 5, 6]
    
    # TODO: any will return true if any of the sequence values are true
    print(any(list1))
    # TODO: all will return true only if all values are true
    print(all(list1))
    # TODO: min and max will return minimum and maximum values in a sequence
    print(f"Min value of list1: {min(list1)}")
    print(f"Max value of list1: {max(list1)}")
    # TODO: Use sum() to sum up all of the values in a sequence
    print(f"Sum of all elements in List1: {sum(list1)}")
if __name__ == "__main__":
    main()
    