from typing import Dict

import unittest


class TrieNode:
    def __init__(self, char_pos_idx: int):
        self.char_pos_idx = char_pos_idx
        self.map_ord_to_child = {}
        self.leaf_str = False
        # True if we have an insertion of a string that ends at this node

    def insert(self, remaining_string: str) -> None:
        """If this node is one below root with root mapping c to it, 
        then this inout will be 'at'"""
        if not remaining_string:
            self.leaf_str = True
            # This is not used right now
            return
        varchar1 = ord(remaining_string[0])
        if varchar1 not in self.map_ord_to_child:
            self.map_ord_to_child[varchar1] = TrieNode(self.char_pos_idx + 1)
        # Send the new remaining string to the appropriate child
        self.map_ord_to_child[varchar1].insert(remaining_string[1:])

    def search(self, remaining_string: str) -> bool:
        if not remaining_string:
            # If there are no children of the map then return True
            # If leaf_str is True then return True
            # If we have children then return False ?
            if ((not self.map_ord_to_child) or (self.leaf_str)):
                return True
            else:
                return False
        varchar1 = ord(remaining_string[0])
        if varchar1 not in self.map_ord_to_child:
            return False
        # Send the new remaining string to the appropriate child
        return self.map_ord_to_child[varchar1].search(remaining_string[1:])

    def startsWith(self, remaining_string) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type remaining_string: str
        :rtype: bool
        """
        if not remaining_string:
            return True
        varchar1 = ord(remaining_string[0])
        if varchar1 not in self.map_ord_to_child:
            return False
        # Send the new remaining string to the appropriate child
        return self.map_ord_to_child[varchar1].startsWith(remaining_string[1:])


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(0)

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        self.root.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        return self.root.search(word)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.root.startsWith(prefix)


# Tests


class Test(unittest.TestCase):
    def test_one_node_trie(self):
        t_trie = Trie()
        t_trie.insert('app')
        result = t_trie.search('app')
        self.assertTrue(result)


unittest.main(verbosity=2)