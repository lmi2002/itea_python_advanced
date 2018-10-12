import pytest

from home_task_1 import Stack
from home_task_1 import EmptyStackError
from home_task_1 import LimitExceedError


def test_init_defoult_args():
    st = Stack()
    assert st.limit is None
    assert st.data_type is object


def test_set_args():
    st = Stack(data_type=int, limit=3)
