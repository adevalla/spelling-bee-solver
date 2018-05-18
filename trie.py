class TrieNode:
    def __init__(self, c):
        self.char = c
        self.children = []
        self.isCompleteWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("")
        self.root.isCompleteWord = True

    def add(self, word):
        n = self.root
        for c in word:
            for child in n.children:
                if child.char == c:
                    n = child
                    break
            else:
                child = TrieNode(c)
                n.children.append(child)
                n = child
        n.isCompleteWord = True

    def search(self, word):
        n = self.root
        for c in word:
            for child in n.children:
                if child.char == c:
                    n = child
                    break
            else:
                return False
        return n.isCompleteWord

    def getWords(self, prefix):
        """
        Returns list of all words in trie starting with prefix
        """
        def dfs(node, word):
            rlist = []
            word += node.char
            if node.isCompleteWord:
                rlist.append(word)
            for child in node.children:
                rlist.extend(dfs(child, word))
            return rlist

        n = self.root
        # Look for prefix in tree
        for c in prefix:
            for child in n.children:
                if child.char == c:
                    n = child
                    break
            else:
                return []
        # n is now node containing last character of prefix
        return dfs(n, prefix[:-1])

    def getValidWords(self, charstring):
        """
        Returns list of all words in trie containing *only* letters in
        charstring. Letters can occur 0 or more times. All words must
        contains charstring[0] (key).
        """
        def dfs(node, word, includesKey, charstring, wordlist=[]):
            if node.char not in charstring:
                # Invalid character, so stop building the word
                return
            word += node.char
            includesKey = includesKey or node.char == charstring[0]
            if includesKey and node.isCompleteWord:
                # completed word includes the key
                wordlist.append(word)
                # print(word)
            for child in node.children:
                dfs(child, word, includesKey, charstring, wordlist)
            return wordlist

        return dfs(self.root, "", False, charstring)
