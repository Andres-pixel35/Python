import multiprocessing

def calculate_squere(n):
    return n * n

if __name__ == '__main__':
    numbers = [1,2,3,4,5]

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_squere, numbers)

    print(f"Results: {results}")