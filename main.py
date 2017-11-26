import unittest
from linkedlist import Node
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree
from graph import Graph

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


class TestGrapghNow(unittest.TestCase):
    def test01_GRAP_Empty(self):
        grap = Graph()
        self.assertEqual(grap.isEmpty(), True)

    def test02_size(self):
        grap = Graph()
        grap.addVertex("A")
        grap.addVertex("B")
        self.assertEqual(grap.size(),2 )
    def test03_AreNeighbours(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addEdge("A","B")
        self.assertEqual(graph.areNeighbours("A","B"),1)

    def test04_AreNoNeighboursh(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addVertex("D")
        graph.addEdge("A","B")
        graph.addEdge("B","C")
        graph.addEdge("C","D")
        self.assertEqual(graph.areNeighbours("A","C"),False)


    def test04_IsConnected(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addVertex("D")
        graph.addEdge("A","B")
        graph.addEdge("B","C")
        graph.addEdge("C","D")
        self.assertEqual(graph.isConnected(),True)

    def test05_Labyrinten(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addVertex("D")
        graph.addVertex("E")
        graph.addVertex("F")
        graph.addVertex("G")
        graph.addVertex("H")
        graph.addVertex("I")
        graph.addVertex("J")
        graph.addVertex("K")
        graph.addVertex("L")
        graph.addVertex("M")
        graph.addEdge("A","B")
        graph.addEdge("B","C")
        graph.addEdge("C","D")
        graph.addEdge("D","H")
        graph.addEdge("C","G")
        graph.addEdge("G","K")
        graph.addEdge("A","E")
        graph.addEdge("E","I")
        graph.addEdge("I","M")
        graph.addEdge("M","N")
        graph.addEdge("N","J")
        graph.addEdge("J","F")
        graph.addEdge("N","O")
        graph.addEdge("O","P")
        graph.addEdge("P","L")
        self.assertEqual(graph.findDFSPath("M","H"),['M', 'I', 'E', 'A', 'B', 'C', 'D', 'H'])





if __name__ == '__main__':
    unittest.main(verbosity=2)



