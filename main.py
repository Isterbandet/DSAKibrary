import unittest
from linkedlist import Node
from linkedlist import LinkedList

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

    def test02_Test_Add(self):
        a = LinkedList( )
        a.add(10)
        self.assertEqual(a.print(), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)
