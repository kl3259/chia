from chia import components
from chia.components.Factory import Factory
from chia.instrumentation.observers import (
    buffered_observer,
    json_observer,
    stream_observer,
)


class ObserverFactory(components.Factory.Factory):
    name_to_class_mapping = {
        "buffered": buffered_observer.BufferedObserver,
        "stream": stream_observer.StreamObserver,
        "json": json_observer.JSONObserver,
    }
