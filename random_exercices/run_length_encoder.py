def count_consecutive_letters(letters: str, index: int) -> tuple:
    count = 0
    word = letters[index]

    while (True):
        try:
            letters[index + 1]
        except IndexError:
            break

        if letters[index] == letters[index + 1]:
            count += 1
            index += 1 
        else:
            break

    return (word, count + 1)

def differents_letter(letters: str) -> int:
    number = len(letters)
    count = 0

    for i in range(1, number):
        if not letters[i - 1] == letters[i]:
            count += 1

    return count + 1


if __name__ == "__main__":
    letters = input("Enter an array of letters: ")

    number = len(letters)
    index = 0
    number_letters = differents_letter(letters)
    count_letters = []


    for _ in range(number_letters):
        buffer = count_consecutive_letters(letters, index)
        count_letters.append(buffer)
        index += buffer[1]
    
    print(count_letters)

