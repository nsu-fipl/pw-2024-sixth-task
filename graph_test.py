from graph import Node, DFS, BFS


def n(title, prev):
    node = Node(title, title, prev)
    prev.neighbours.append(node)
    return node


def root(title):
    return Node(title, title)


def traverse(r, CLS):
    bfs = CLS()
    bfs.traverse(r)
    return bfs.result


def test_bfs_one_node():
    r = root("test")
    assert traverse(r, BFS) == ['test']


def test_bfs_two_nodes():
    r = root("1")
    n("2", r)
    assert traverse(r, BFS) == ['1', '2']


def test_bfs_two_neighbours():
    r = root("1")
    n("2", r)
    n("3", r)
    assert traverse(r, BFS) == ['1', '2', '3']


def test_bfs_three_in_a_row():
    r = root("1")
    n2 = n("2", r)
    n("3", n2)
    assert traverse(r, BFS) == ['1', '2', '3']


def test_bfs_three_in_a_row_and_extra():
    r = root("1")
    n2 = n("2", r)
    n("3", n2)
    n4 = n("4", r)
    assert traverse(r, BFS) == ['1', '2', '4', '3']


def test_bfs_cicle_on_one():
    r = root("1")
    r.neighbours.append(r)
    assert traverse(r, BFS) == ['1']


def test_bfs_cicle_on_two():
    r = root("1")
    n2 = n("2", r)
    n2.neighbours.append(r)
    assert traverse(r, BFS) == ['1', '2']


def test_dfs_one_node():
    r = root("test")
    assert traverse(r, DFS) == ['test']


def test_dfs_two_nodes():
    r = root("1")
    n("2", r)
    assert traverse(r, DFS) == ['2', '1']


def test_dfs_two_neighbours():
    r = root("1")
    n("2", r)
    n("3", r)
    assert traverse(r, DFS) == ['2', '3', '1']


def test_dfs_three_in_a_row():
    r = root("1")
    n2 = n("2", r)
    n("3", n2)
    assert traverse(r, DFS) == ['3', '2', '1']


def test_dfs_three_in_a_row_and_extra():
    r = root("1")
    n2 = n("2", r)
    n("3", n2)
    n4 = n("4", r)
    assert traverse(r, DFS) == ['3', '2', '4', '1']


def test_dfs_cicle_on_one():
    r = root("1")
    r.neighbours.append(r)
    assert traverse(r, DFS) == ['1']


def test_dfs_cicle_on_two():
    r = root("1")
    n2 = n("2", r)
    n2.neighbours.append(r)
    assert traverse(r, DFS) == ['2', '1']
