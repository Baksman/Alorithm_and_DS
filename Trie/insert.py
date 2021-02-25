

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endString = False


class Trie:
    def __init__(self):
        self.rootNode = TrieNode()

    def insertNode(self, word):
        current: TrieNode = self.rootNode
        for i in word:
            ch = i
            node = current.children.get(ch)

            if node == None:
                node = TrieNode()
                current.children.update({ch: node})

            current = node
        current.endString
        print("Successfuly inserted")


newTrie = Trie()
newTrie.insertNode("App")
newTrie.insertNode("Appl")
