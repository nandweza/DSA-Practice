#!/usr/bin/python3

def main():
    """return a list of products of n"""
    arr = [6, 3, -2, -5, 7, 3]

    results = []

    for i in range(0, len(arr) - 1):
        results.append(arr[i] * arr[i + 1])
        print(results)
        print(max(results))


if __name__ == '__main__':
    main()