"""
Implement the google autocomplete feature
Given a string which represents characters typed into a text box so far, Write
as program to suggest words based on what i have typed so far

Eg.
input: cat
output: [catnip, caterpillar, cats, catskills]

"""

class Node(object):
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_word = False

class Dictionary(object):
    def __init__(self):
        self.root = Node()

    def insert_word(self, word):
        if len(word) < 1:
            return
        curr = self.root
        for i in xrange(len(word)):
            index = ord(word[i]) - 97
            if curr.children[index] is None:
                curr.children[index] = Node()
            curr = curr.children[index]
        curr.is_word = True
        return

    def insert_node(self, root, index, node):
        if root is None:
            return
        if root.children[index] is None:
            root.children[index] = node
            root.children[index].is_word = True
            return
        self.insert_node(root.children[index], index, node)


    def search_words(self, string):
        if len(string) < 1:
            return []
        result = []
        curr = self.root
        for i in xrange(len(string)):
            index = ord(string[i]) - 97
            if curr.children[index] is None:
                break
            curr = curr.children[index]
        if curr.is_word:
            result.append(string)
        self.get_words(curr, "", result)
        result = map(lambda item: string + item, result)
        return result

    def get_words(self, node, suffix, result):
        if node is None or node.is_word:
            result.append(suffix)
        for i in xrange(len(node.children)):
            if node.children[i] is not None:
                suffix += chr(i+97)
                self.get_words(node.children[i], suffix, result)
                suffix = suffix[:-1]
        return

if __name__ == '__main__':
    str1 = "cat"
    words = ["catnip", "caterpillar", "cats", "catskills"]

    dictionary = Dictionary()
    for word in words:
        dictionary.insert_word(word)
    print dictionary.search_words(str1)

