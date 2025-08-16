numbers = [1,2,3,4,5,6,7,8,9,10]
"""
even_numbersC = [x for x in numbers if x % 2 == 0]
even_numbersL = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Even numbers with Comprehension list {even_numbersC}")
print(f"\nEven numbers with lambda {even_numbersL}")

numbersGT5C = [x for x in numbers if x > 5]
numbersGT5L = list(filter(lambda x: x > 5, numbers))

print(f"Numbers greater than 5 with comprehension {numbersGT5C}")
print(f"\nNumbers greater than 5 with Lambda {numbersGT5L}")


numbers2 = [1,2,3,4,5]

squaresC = [x**2 for x in numbers]
squaresL = list(map(lambda x: x**2, numbers))

print(f"Squares with comprehension list {squaresC}")
print(f"Squares with lambda {squaresL}")
"""
words = ['hello', 'world', 'python', 'programming', 'lambda']
"""
wordsLongerC = [word for word in words if len(word) > 5]
wordsLongerL = list(filter(lambda word: len(word) > 5, words))

print(f"Words longer than 5 with comprehension {wordsLongerC}")
print(f"Words longer than 5 with lambda {wordsLongerL}")


lenWordC = [len(word) for word in words]
lenWordL = list(map(lambda word: len(word), words))

print(f"The len of each word with comprehension list {lenWordC}")
print(f"The len of each word with lambda {lenWordL}")
"""

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaresEvenC = [x**2 for x in data if x % 2 == 0]
squaresEvenL = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, data)))     

print(squaresEvenC)
print(squaresEvenL)