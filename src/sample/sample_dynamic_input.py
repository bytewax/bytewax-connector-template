from typing import Any

from bytewax.inputs import DynamicInput, StatelessSource


class _DynamicSource(StatelessSource):
    """Sample class implementing a Bytewax StatelessSource.

    Stateless sources of input do not track the state of their output,
    and can not participate in any guarantees that data will be processed
    at least once.
    """

    def __init__(self, resume_state):
        """Create a new instance of _SampleSource

        Args:

            resume_state: The last completed snapshot for this source.
        """
        pass

    def next(self) -> list[Any]:
        """Return the next batch of items from the input.

        This method should return a list of items from the input
        source, or raise
        https://docs.python.org/3/library/exceptions.html#StopIteration
        if no new items will be produced from the partition that this
        source represents.

        If possible, you should emit the list of items to be processed
        as (key[str], value[any]) tuples.

        An important thing to note here is that StatefulSource.next
        must never block. The Bytewax runtime employs a sort of
        cooperative multitasking, and so each operator must return
        quickly, even if it has nothing to do, so other operators in
        the dataflow that do have work can run.
        """
        pass

    def close(self):
        pass


class SampleDynamicInput(DynamicInput):
    """Sample class implementing `DynamicInput`

    A DynamicInput supports reading distinct items from any number
    of workers concurrently.

    DynamicInputs do not support storing resume state and therefore
    can only support at-most-once processing.

    The source must support supplying disjoint data for each worker.
    If you re-read the same items on multiple workers, the dataflow
    will process these as duplicate items.
    """

    def build(self, worker_index, worker_count) -> _DynamicSource:
        """Build and return a single instance of a `StatelessSource`
        subclass.

        This function will be called once on each worker as a Dataflow
        is starting.

        Args:

            worker_index: The index of the worker that this function
            is being called on.

            worker_count: The total number of workers in the Dataflow.
        """
        pass
