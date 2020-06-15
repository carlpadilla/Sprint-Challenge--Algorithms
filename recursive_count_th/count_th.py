'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word, initial_count=0):

    # keep track of the counter
    count = initial_count

    # get the index of 'th'
    index_th = word.find('th')

    # if not th is not found, return 0
    if index_th == -1:
        return 0
    else:
        # increment count by 1
        count += 1

    try:
        # check for next letter
        next_letter = word[index_th+2]
    except IndexError:
        # if no next letter, return the count
        return count

    count += count_th(word[index_th+2:])

    return count
