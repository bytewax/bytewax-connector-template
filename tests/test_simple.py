from bytewax.dataflow import Dataflow
from bytewax.testing import run_main, TestingInput, TestingOutput


def test_map():
    flow = Dataflow()

    inp = [0, 1, 2]
    flow.input("inp", TestingInput(inp))

    def add_one(item):
        return item + 1

    flow.map(add_one)

    out = []
    flow.output("out", TestingOutput(out))

    run_main(flow)

    assert sorted(out) == sorted([1, 2, 3])
