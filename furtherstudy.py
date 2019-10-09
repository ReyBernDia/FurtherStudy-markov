"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()

    return file

text = open_and_read_file("green-eggs.txt")

def make_chains(text_string,ngrams=3):
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

    for num in range(len(words)-ngrams):
        # tuple_key = (words[num], words[num+1],(words[num+2])*ngrams)
        tuple_key = tuple([words[num+idx] for idx in range(ngrams)])

        if tuple_key in chains:
            chains[tuple_key].append(words[num+ngrams])
        else:
            chains[tuple_key] = chains.get(tuple_key, [words[num+ngrams]])

      
    return chains

# print(make_chains(text,4))


def make_text(chains):
    """Return text from chains."""

    words = []

  #focus only on capital letters[0] & punctuation[-1]

  #start random text with capital and end with punctuation 
 # 

    
    a_lis = [word for word in list(chains.keys()) if word[0].istitle()]
    words.append(choice(a_lis))


    while True:

        random_key = choice(list(chains.keys())) #link
        random_value = choice(chains[random_key])

        #append until value[-1] == "." or "?" then break 
        #if not append
        words.append(random_key[0])
        words.append(random_key[1])
        words.append(random_value)
        #if yes append and then stop 
        if random_value[-1] == "." or random_value[-1] =="?":
            break 
       

        # new_key = (random_key[1],random_value)
        # if not new_key in chains.keys():
        #     break

    print(words)
    # return " ".join(words)


input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# # Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
# make_text(chains)