class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [ word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned ]
        counts_word = collections.Counter(words)
        return counts_word.most_common(1)[0][0]
