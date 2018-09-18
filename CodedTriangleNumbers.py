import pandas as pd
import string
def calc_word_val(word, d):

    # Split word into individual letters
    word_letters = [str(x) for x in str(word)]
    #print('word letters:', word_letters)
    # Find the sum of the word's letters
    sum = 0
    for letter in word_letters:
        letter_val = d[letter]
        #print('letter val:', letter_val)
        sum += letter_val

    return sum
def create_triangle_dictionary(max_t):
    num_list = list(range(1, max_t, 1))
    tlist = []
    for int in num_list:
        t = 0.5 * int * (int + 1)
        tlist.append(t)
    triang = dict(zip(num_list, tlist))

    return triang

def check_is_triangle(num, triang):

    if num in triang.values():
        return True
    else:
        return False


def main():
    # Create letter value dictionary
    letters = sorted(string.ascii_uppercase)
    d = dict(zip(letters, list(range(1, len(letters) + 1, 1))))
    print("d:", d)
    # Create triangle number dictionary
    triang = create_triangle_dictionary(1000)

    # Initialize:
    triangle_words = []
    counter = 0

    # Read in file
    file_name = 'words.txt'
    words = pd.read_csv(file_name)

    for word in words:

        # Check value of the word
        word_val = calc_word_val(word, d)

        # Check if the number is a triangel number
        if check_is_triangle(word_val, triang):
            print('The word value of ', word, ' is:', word_val)
            triangle_words.append(word)
            counter += 1

    print('There are ', counter, ' triangle words in the file')

main()