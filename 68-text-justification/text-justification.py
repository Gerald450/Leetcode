from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = []
        line_length = 0

        i = 0
        while i < len(words):
            word = words[i]

            if line_length + len(line) + len(word) > maxWidth:
                # Time to justify current line
                spaces_needed = maxWidth - line_length
                if len(line) == 1:
                    result.append(line[0] + ' ' * spaces_needed)
                else:
                    even_space = spaces_needed // (len(line) - 1)
                    extra_space = spaces_needed % (len(line) - 1)
                    justified = ''
                    for j in range(len(line) - 1):
                        justified += line[j] + ' ' * (even_space + (1 if j < extra_space else 0))
                    justified += line[-1]
                    result.append(justified)

                # Reset line
                line = []
                line_length = 0
            else:
                line.append(word)
                line_length += len(word)
                i += 1

        # Last line (left-justified)
        last_line = ' '.join(line)
        last_line += ' ' * (maxWidth - len(last_line))
        result.append(last_line)

        return result
