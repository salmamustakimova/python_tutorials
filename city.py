class Graph:
    def __init__(self):
        self.Vertexes = []
        self.Edges = []
    
    
    def add_vertex(self, v):
        self.Vertexes.append(v)
    
    
    def add_edge(self, v1, v2, w):
        # 1. Найти вершину в Vertexes -> int, None
        # 2. Если None, сообщить пользователю об отсутствии и выйти
        # 3. Если обе вершины есть, то добавить в edges тройку (v1_idx, v2_idx, w)
        if v1 and v2 in self.Vertexes:
            print(v1,v2)
            for i in range(len(self.Vertexes)):
                if self.Vertexes[i]==v1:
                   self.Edges.append(i)
                if self.Vertexes[i]==v2:  
                   self.Edges.append(i)
            self.Edges.append(w)   
            return True
        else:
            print("Вершина отсутствует")
            return False
        
    def print_graph(self):
        i = 0
        while i < len(self.Edges):
            print(f'Город 1: {self.Vertexes[self.Edges[i]].name}, город 2: {self.Vertexes[self.Edges[i+1]].name}, расстояние: {self.Edges[i+2]}')
            i += 3

class City:
    def __init__(self, name):
        self.name = name
    def __repr__(self) -> str:
        return f'City - {self.name}'


G = Graph()

a = City('a')
b = City('b')
c = City('c')
d = City('d')

G.add_vertex(a)
G.add_vertex(b)
G.add_vertex(c)
G.add_vertex(d)

G.add_edge(a, b, 4)
G.add_edge(b, c, 3)
G.add_edge(c, d, 5)

G.print_graph()

import unittest

class TestGraphMethods(unittest.TestCase):

    def test_none(self):
        G = Graph()
        a = City('a')
        b = City('b')
        self.assertFalse(G.add_edge(a, b, 4))
        self.assertEqual(len(G.Edges), 0)

    def test_one_vertex(self):
        G = Graph()
        a = City('a')
        b = City('b')

        G.add_vertex(a)
        self.assertFalse(G.add_edge(a, b, 4))
        self.assertEqual(len(G.Vertexes), 1)
    def test_two_vertex(self):
        G = Graph()
        a = City('a')
        b = City('b')
        G.add_vertex(a)
        G.add_vertex(b)
        self.assertTrue(G.add_edge(a, b, 4))
        self.assertEqual(len(G.Vertexes), 2)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()