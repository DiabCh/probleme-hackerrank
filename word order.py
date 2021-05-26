'''You are given  words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Constraints:

The sum of the lengths of all the words do not exceed
All the words are composed of lowercase English letters only.

Input Format

The first line contains the integer, .
The next  lines each contain a word.

Output Format

Output  lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
Explanation

There are  distinct words. Here, "bcdef" appears twice in the input at the first and last positions.
 The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.'''
import re
# n_words = input()
# distinct= 0
# s = ''
#
# for count in range(n_words):
#     s = s +' '+ input()
# words = s.split()
# checked_words =[]
# repeated_words =[]
# for word in words:
#     if word  not in checked_words:
#         repeated_words.append(str((s.count(word))))
#         checked_words.append(word)
#         distinct += 1
#
#
# print(distinct)
# print(' '.join(repeated_words))
# print(checked_words)
#

n_words = int(input())
words = [input() for _ in range(n_words)]

repeated_words = {}
for word in words:
    try:
        repeated_word[word] += 1
    except KeyError:
        wrepeated_word[word] = 1
print(len(repeated_word))
print(*repeated_word.values())

