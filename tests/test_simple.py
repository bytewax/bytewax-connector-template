import bytewax.operators as op
from bytewax.dataflow import Dataflow
from bytewax.testing import TestingSink, TestingSource, run_main


def test_map():
    flow = Dataflow("test")

    inp = op.input("inp", flow, TestingSource([0, 1, 2]))

    def add_one(item):
        return item + 1

    add_one = op.map("add_one", inp, add_one)

    out = []
    op.output("out", add_one, TestingSink(out))

    run_main(flow)

    assert sorted(out) == sorted([1, 2, 3])
