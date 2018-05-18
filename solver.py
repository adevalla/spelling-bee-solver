from trie import Trie

wordTrie = Trie()
with open('scowl/english-words-utf-8') as fh:
    for line in fh:
        wordTrie.add(line.strip())

print(wordTrie.getValidWords("abc"))
print(wordTrie.getValidWords("ocfilmr"))
