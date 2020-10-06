import unittest

def get_path(graph, start_node, end_node):
  visited = [start_node]
  queue = [start_node]

  distance = {}
  predecessor = {}
  
  dist_count = 0
  distance[start_node] = dist_count
  dist_count += 1

  while len(queue) > 0:
    current_node = queue.pop(0)

    if current_node in graph.keys():
      for neighbour_node in graph[current_node]:
        if neighbour_node not in visited:
          visited.append(neighbour_node)
          queue.append(neighbour_node)

          # populate distance and predecessor
          distance[neighbour_node] = dist_count
          predecessor[neighbour_node] = current_node

          if neighbour_node == end_node:
            break

      dist_count += 1

  # loop over the predecessors' values from end node to find parent
  shortest_path = []
  parent_node = predecessor[end_node]
  shortest_path.append(parent_node)

  while parent_node in predecessor.keys():
    parent_node = predecessor[parent_node]
    shortest_path.append(parent_node)

  shortest_path = list(reversed(shortest_path))
  shortest_path.append(end_node)
  print(shortest_path)



# Tests

class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)