import queue
import sys

from matplotlib import pyplot

from mworks.conduit import IPCAccumClientConduit


class Conduit(IPCAccumClientConduit):

    def __init__(self,
                 resource_name,
                 start_event,
                 stop_event,
                 event_names,
                 event_handler):
        super().__init__(resource_name, start_event, stop_event, event_names)
        self.event_handler = event_handler
        self._queue = queue.Queue()

    def _post_events(self, events):
        if events:
            self._queue.put(events)
            self._stop_main_loop()

    def run(self):
        self.register_bundle_callback(self._post_events)
        pyplot.cla()
        pyplot.draw()
        while True:
            # show will execute until _stop_main_loop is called
            pyplot.show()
            self.event_handler(self, self._queue.get())

    @classmethod
    def main(cls,
             event_handler,
             event_names,
             start_event = 'start',
             stop_event = 'stop'):
        resource_name = sys.argv[1]
        with cls(resource_name,
                 start_event,
                 stop_event,
                 event_names,
                 event_handler) as conduit:
            conduit.run()
