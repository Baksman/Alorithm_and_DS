

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

    def searchString(self, word):
        currentNode:TrieNode = self.rootNode
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        
        if currentNode.endString == True:
            return True
        else:
            return False


newTrie = Trie()
newTrie.insertNode("App")
newTrie.insertNode("Appl")
print(newTrie.searchString("App"))
print(newTrie.searchString("Ap"))
