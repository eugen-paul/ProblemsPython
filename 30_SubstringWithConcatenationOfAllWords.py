from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
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
