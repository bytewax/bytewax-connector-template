from typing import Any

from bytewax.inputs import PartitionedInput, StatefulSource


class _PartitionedSource(StatefulSource):
    """Sample class implementing a Bytewax StatefulSource.

    Stateful sources of input should be able to replay input items in
    the same order from the instant of the most recent snapshot. This
    will cause the state and output of the dataflow to evolve in the
    same way during the resume execution as during the previous
    execution.
    """

    def __init__(self, resume_state):
        """Create a new instance of _SampleSource

        Args:

            resume_state:
                The last completed snapshot for this source.
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
        as (key[str], value[Any]) tuples.

        An important thing to note here is that StatefulSource.next
        must never block. The Bytewax runtime employs a type of
        cooperative multitasking, and so each operator must return
        quickly, even if it has nothing to do, so other operators in
        the dataflow that do have work can run.
        """
        pass

    def snapshot(self):
        """Snapshot the current state of this source.

        This function is called by Bytewax to capture the current
        state of this input for recovery.

        When starting a Dataflow from a recoverable state, the snapshot
        returned by this method will be passed to the `PartitionedInput`
        class, and should be used to resume input from that point.
        """
        pass

    def close(self):
        pass


class SampleInput(PartitionedInput):
    """Sample class implementing `PartitionedInput`

    A partition is a "sub-stream" of data that can be read
    concurrently and independently. As an example, a Kafka topic is
    divided up into partitions, each of which contains a disjoint set
    of data.

    To write a `PartitionedInput` subclass, you should be able to
    answer the following questions about your input:

    1. How many partitions of data are there?
    2. How do I build a source that can read from a single partition?
    3. How do I "rewind" a partition to re-read an item and any
       subsequent data?

    PartitionedInput sources should maintain state in order to support
    recovery.

    Fully recoverable Dataflows require the ability to replay data
    from the past.

    Each partition must contain unique data. If you re-read the same data
    in multiple partitions, the dataflow will process these duplicate
    items.
    """

    def __init__(self):
        pass

    def list_parts(self) -> list[str]:
        """List all of the parts or partitions for this input source.

        This method should return the list of partitions available
        for this worker. You do not need to list all partitions globally.
        """
        pass

    def build_part(self, for_part, resume_state) -> _PartitionedSource:
        """Build and return a single instance of a StatefulSource

        Will be called once per execution for each partition key on a
        worker that reported that partition was local in `list_parts`.

        Do not pre-build state about a partition in the
        constructor. All state must be derived from `resume_state` for
        recovery to work properly.

        Args:

            for_part:
                Which part to build a `SampleSource` for.
                Will always be one of the keys returned by `list_parts`
                on this worker.

            resume_state:
                The last completed snapshot for this source.
        """
        pass
