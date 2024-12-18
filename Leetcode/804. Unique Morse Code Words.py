

"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..",
"--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]


Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...".
We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.



Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1



"""

def morse(list1: list[str]):

    morse_a = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
               'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
               'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
               'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
               'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}


    list3 = []
    list4 = []

    for words in list1:
        for letters in words:
            list3.append(morse_a.get(letters))

        list4.append("".join(list3))
        list3 = []

    return len(set(list4))


print(morse(["gin","zen","gig","msg"]))

