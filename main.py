import unittest
from linkedlist import Node
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree

class TestNodeAndList(unittest.TestCase):
    def test01_get_Data( self ):
        firstnode = Node(17)
        self.assertEqual( firstnode.getData() , 17)

    def test02_set_data(self):
        firstnode = Node(17)
        firstnode.setData(20)
        self.assertEqual(firstnode.getData(), 20)

    def test03_get_next_and_Set_Next(self):
        a = Node(12)
        a.setNext(14)
        self.assertEqual(a.getNext(), 14)

class TestLinkedList(unittest.TestCase):
    def test01_is_Empty(self):
        a = LinkedList()
        self.assertEqual(a.isEmpty(),True)



    def test03_Test_Size(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.size(), 3)

    def test04_Test_ToList(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.toList(),[3,2,1])

    def test05_Test_Search(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        self.assertEqual(a.search(2).getData(), 2)

    def test06_Test_incert(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        a.insert(4, a.search(2))
        self.assertEqual(a.search(2).getNext().getData(), 4)

    def test02_Test_Remove(self):
        a = LinkedList()
        a.add(1)
        a.add(2)
        a.add(3)
        n = a.search(2)
        a.remove(n)
        self.assertEqual(a.search(2),None)

class TestBinaryTree(unittest.TestCase):
    def test01_is_Empty(self):
        binarytree = BinarySearchTree()
        self.assertEqual(binarytree.isEmpty(),True)

    def test02_Incert(self):
        binarytree = BinarySearchTree()
        binarytree.setData(10)
        binarytree.insert(17)
        self.assertEqual(binarytree.size(),2)

    def test03_to_List(self):
        binarytree = BinarySearchTree()
        binarytree.setData(10)
        binarytree.insert(17)
        binarytree.insert(16)
        binarytree.insert(14)
        self.assertEqual(binarytree.toList(), [10,14,16,17])


    def test03_to_find(self):
        binarytree = BinarySearchTree()
        binarytree.setData(10)
        binarytree.insert(17)
        binarytree.insert(16)
        binarytree.insert(14)
        self.assertEqual(binarytree.find(14),14 )




if __name__ == '__main__':
    unittest.main(verbosity=2)

