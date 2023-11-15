#2000. Reverse Prefix of Word
"""Given a 0-indexed string word and a character ch, reverse the segment of word that 
starts at index 0 and ends at the index of the first occurrence of ch (inclusive).
 If the character ch does not exist in word, do nothing.

For example, if word = "abcdefd" and ch = "d", then you should reverse the segment
 that starts at 0 and ends at 3 (inclusive). The resulting string will be "dcbaefd".
Return the resulting string."""

def reverse_prefix_word(word,ch):
    reverse = ""
    for i,char in enumerate(word):
        if char == ch:
            return (reverse + char)[::-1] + word[i+1:]
        reverse += char
    return reverse

word = "abcdefd"
ch ="d"
output = reverse_prefix_word(word,ch)
print(f"word before reverse the prefix of word---> {word} & character---> {ch}\n")
print(f"after reverse prefix word {output}")