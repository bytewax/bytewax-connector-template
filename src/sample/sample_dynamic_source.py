from datetime import datetime
from typing import Any, Iterable

from bytewax.inputs import DynamicSource, StatelessSourcePartition


class _SampleSourcePartition(StatelessSourcePartition):
    """Sample class implementing a Bytewax StatelessSourcePartition."""

    def __init__(self):
        """Create a new instance of SampleSource."""
        pass

    def next_batch(self, sched: datetime) -> Iterable[Any]:
        """Attempt to get the next batch of input items.

        This must participate in a kind of cooperative multi-tasking,
        never blocking but yielding an empty list if there are no new
        items yet.

        Args:
            sched: The scheduled awake time.

        Returns:
            Items immediately ready. May be empty if no new items.

        Raises:
            StopIteration: When the source is complete.

        """
        pass

    def close(self):
        pass


class SampleDynamicSource(DynamicSource):
    """Sample class implementing `DynamicSource`

    A DynamicInput supports reading distinct items from any number
    of workers concurrently.

    DynamicInputs do not support storing resume state and therefore
    can only support at-most-once processing.

    The source must support supplying disjoint data for each worker.
    If you re-read the same items on multiple workers, the dataflow
    will process these as duplicate items.
    """

    def build(self, worker_index, worker_count) -> _SampleSourcePartition:
        """Build and return an instance of a `SampleSourcePartition`.

        This function will be called once on each worker as a Dataflow
        is starting.

        Args:

            worker_index: The index of the worker that this function
            is being called on.

            worker_count: The total number of workers in the Dataflow.
        """
        pass
