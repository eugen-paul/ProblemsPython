from collections import Counter
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # own implementation of the official solution
        word_len = len(words[0])

        response = list()
        rest_words_template = dict()
        words_cnt = Counter(words)
        for w in words:
            rest_words_template[w] = rest_words_template.get(w, 0)+1

        for start_offset in range(word_len):
            pos = start_offset
            window_cnt = Counter()
            words_in_window = 0
            while pos < len(s):
                # read and add current word to word counter
                current_word = s[pos:pos+word_len]
                window_cnt[current_word] += 1

                # check if new current word is OK
                if rest_words_template.get(current_word, None) is None:
                    # current word is not in words => clear window
                    window_cnt.clear()
                    words_in_window = 0
                elif words_in_window == len(words) - 1:
                    # window counter is big enough
                    if words_cnt == window_cnt:
                        # window counter is equal to words => add positon of first word to respone
                        response.append(pos - (word_len * (len(words) - 1)))
                    # remove first word from window to move window
                    pos_first_word = pos - (word_len * (len(words) - 1))
                    first_window_word = s[pos_first_word:pos_first_word+word_len]
                    window_cnt[first_window_word] -= 1
                else:
                    words_in_window += 1

                pos += word_len

        return response

    def findSubstring_3(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])

        response = list()
        rest_words_template = dict()
        for w in words:
            rest_words_template[w] = rest_words_template.get(w, 0)+1

        for i in range(len(s)-word_len*len(words)+1):
            rest_words = rest_words_template.copy()
            pos = i
            next_word = s[pos:pos+word_len]
            while next_word in rest_words:
                if rest_words[next_word] == 1:
                    rest_words.pop(next_word)
                else:
                    rest_words[next_word] = rest_words[next_word]-1
                pos += word_len
                next_word = s[pos:pos+word_len]
            if len(rest_words) == 0:
                response.append(i)

        return response

    def findSubstring_2(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])

        response = list()

        for i in range(len(s)-word_len*len(words)+1):
            rest_words = [*words]
            pos = i
            next_word = s[pos:pos+word_len]
            while next_word in rest_words:
                rest_words.remove(next_word)
                pos += word_len
                next_word = s[pos:pos+word_len]
            if len(rest_words) == 0:
                response.append(i)

        return response


def do_test(i: int, s, t, r):
    c = Solution()
    resp = c.findSubstring(s, t)
    if resp == r:
        print("OK", i)
    else:
        print("NOK", i, "expected", r, "response", resp)


if __name__ == "__main__":
    do_test(0, "barfoothefoobarman", ["foo", "bar"], [0, 9])
    do_test(1, "wordgoodgoodgoodbestword", ["word", "good", "best", "word"], [])
    do_test(2, "barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12])
    do_test(3, "aba", ["a", "b"], [0, 1])
    do_test(4, "acbca", ["a", "b"], [])
