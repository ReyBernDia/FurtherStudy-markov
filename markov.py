"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

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
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()

    for num in range(len(words)-2): 
        tuple_key = (words[num], words[num+1])

        if tuple_key in chains:
            chains[tuple_key].append(words[num+2])
        else:
            chains[tuple_key] = chains.get(tuple_key, [words[num+2]])

      
    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    #try iteration except KeyError break
    
    #print random key followed by random choice value 
    random_key = choice(chains.keys())

    random_value = choice(chains[random_key])
    words.append(random_key)
    words.append(random_value)
    
    return " ".join(words)


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
