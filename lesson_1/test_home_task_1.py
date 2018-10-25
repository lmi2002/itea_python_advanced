from lesson_1.home_task_1 import Stack

"""
Test to test class methods Stack:
usage $ python -m pytest test_home_task_1.py
"""


def test_init_default_args():
    """
    Checking the default values type
    """
    st = Stack()
    assert st.limit is None
    assert st.data_type is object


def test_check_type_el():
    """
    Check of the method type
    """
    st = Stack(data_type=str, limit=2)
    st.push('str')
    assert type(st.stack[0]) == str


def test_check___str__():
    """
    Check of the method ___str__
    """
    st = Stack(data_type=int, limit=2)
    assert st.__str__() == "Stack<int>"


def test_check_limit():
    """
    Check of the method limit
    """
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    st.push(2)
    assert st.stack.__len__() == 3


def test_check_push():
    """
    Check of the method push
    """
    st = Stack(data_type=int, limit=2)
    st.stack = [1]
    st.push(2)
    assert st.stack[1] == 2


def test_check_pull():
    """
    Check of the method pull
    """
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    assert st.pull() == 2


def test_check_count():
    """
    Check of the method count
    """
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    assert st.count() == 2


def test_check_clear():
    """
    Check of the method clear
    """
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    st.clear()
    assert st.stack.__len__() == 0
