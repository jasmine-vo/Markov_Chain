"""Generate markov text from text files."""


from random import choice
import sys

def open_and_read_file(file_path, file_path_2):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    #file.close(file_path)

    #print words

    return contents


def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    chains = {}
    words = text_string.split()

    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]
        #print key, value

        if key not in chains:
            chains[key] = []
        chains[key].append(value)

    # print chains
    return chains


def make_text(chains):
    """Returns text from chains."""

    upper_keys = []
    
    for key in chains:
        if key[0][0].isupper():
            upper_keys.append(key)

    key = choice(upper_keys)
    # key = choice(chains.keys())
    words = []
    words.append(key[0])
    words.append(key[1])
    word = choice(chains[key])
    words.append(word)
    new_key = (key[1], word)
  
    while new_key in chains and len(words) < 140:
        word = choice(chains[new_key])
        words.append(word)
        new_key = (new_key[1], word)
        if not word[-1].isalpha():
            break
            


    return " ".join(words)
   

input_path = sys.argv[1]
input_path2 = sys.argv[2]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path, input_path2)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
