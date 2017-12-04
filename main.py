import unittest
from linkedlist import Node
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree
from graph import Graph
from sort import *
import random, time
from queu import LLQueue

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
        graph.addEdge("A","B",1)
        self.assertEqual(graph.areNeighbours("A","B"),1)

    def test04_AreNoNeighboursh(self):
        graph = Graph()
        graph.addVertex("A")
        graph.addVertex("B")
        graph.addVertex("C")
        graph.addVertex("D")
        graph.addEdge("A","B",1)
        graph.addEdge("B","C",1)
        graph.addEdge("C","D",1)
        self.assertEqual(graph.areNeighbours("A","C"),False)



"""
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
        graph.addVertex("N")
        graph.addVertex("O")
        graph.addVertex("P")

        graph.addEdge("A","B",1)
        graph.addEdge("B","C",1)
        graph.addEdge("C","D",1)
        graph.addEdge("D","H",1)
        graph.addEdge("C","G",1)
        graph.addEdge("G","K",1)
        graph.addEdge("A","E",1)
        graph.addEdge("E","I",1)
        graph.addEdge("I","M",1)
        graph.addEdge("M","N",1)
        graph.addEdge("N","J",1)
        graph.addEdge("J","F",1)
        graph.addEdge("N","O",1)
        graph.addEdge("O","P",1)
        graph.addEdge("P","L",1)

        self.assertEqual(graph.findBFSPath("M","H"),['M', 'I', 'E', 'A', 'B', 'C', 'D', 'H'])


    def test05_ShowBothPaths(self):
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
        graph.addVertex("N")
        graph.addVertex("O")
        graph.addVertex("P")

        graph.addEdge("A","B",1)
        graph.addEdge("B","C",1)
        graph.addEdge("C","D",1)
        graph.addEdge("D","H",1)
        graph.addEdge("C","G",1)
        graph.addEdge("G","K",1)
        graph.addEdge("A","E",1)
        graph.addEdge("E","I",1)
        graph.addEdge("I","M",1)
        graph.addEdge("M","N",1)
        graph.addEdge("N","J",1)
        graph.addEdge("J","F",1)
        graph.addEdge("N","O",1)
        graph.addEdge("O","P",1)
        graph.addEdge("P","L",1)
        graph.addEdge("L","H",1)

        self.assertEqual(graph.findAllPaths("M","H"),[['M', 'N', 'O', 'P', 'L', 'H'], ['M', 'I', 'E', 'A', 'B', 'C', 'D', 'H']])


"""

class Test_Queue_Empty(unittest.TestCase):
    def test_isEmpty_on_empty_queue( self ):
        queue = LLQueue()
        self.assertEqual( queue.isEmpty(), True )
        self.assertEqual( queue.size(), 0 )

    def test_isEmpty_on_nonempty_queue( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        self.assertEqual( queue.isEmpty(), False )


class Test_Queue_Enqueue(unittest.TestCase):
    def test_enqueue_one_item( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        self.assertEqual( queue.isEmpty(), False )
        self.assertEqual( queue.size(), 1 )

    def test_enqueue_two_items( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        self.assertEqual( queue.isEmpty(), False )
        self.assertEqual( queue.size(), 2 )

class Test_Queue_Dequeue(unittest.TestCase):
    def test_dequeue_after_single_enqueue( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        self.assertEqual( queue.isEmpty(), True )

    def test_dequeue_after_two_enqueues( self ):
        queue = LLQueue()
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        self.assertEqual( queue.isEmpty(), False )

    def test_three_dequeues_after_three_enqueues( self ):
        queue = LLQueue()
        queue.enqueue( 25 )
        queue.enqueue( 50 )
        queue.enqueue( 75 )
        x = queue.dequeue()
        self.assertEqual( x, 25 )
        x = queue.dequeue()
        self.assertEqual( x, 50 )
        x = queue.dequeue()
        self.assertEqual( x, 75 )
        self.assertEqual( queue.isEmpty(), True )


if __name__ == '__main__':
    unittest.main(verbosity=2)



