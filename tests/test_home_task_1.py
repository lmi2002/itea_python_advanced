import pytest

from home_task_1 import Stack


def test_init_default_args():
    st = Stack()
    assert st.limit is None
    assert st.data_type is object
    assert st.limit is int


def test_check_type_el():
    st = Stack(data_type=int, limit=2)
    assert st.push('str')


def test_check___str__():
    st = Stack(data_type=int, limit=2)
    assert st.__str__() == "Stack<'int'>"


def test_check_limit():
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    assert st.push(2)


def test_check_pull():
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    assert st.pull() == 2
    st.stack = []
    assert st.pull()


def test_check_count():
    st = Stack(data_type=int, limit=2)
    stack = st.stack[1, 2]
    assert stack.count() == 2


def test_check_clear():
    st = Stack(data_type=int, limit=2)
    st.stack = [1, 2]
    st.clear()
    assert not st.stack
