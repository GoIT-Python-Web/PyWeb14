import pathlib
from queue import Queue
from threading import Thread, Event
import logging


class Writer:
    def __init__(self, mainfile: str, event: Event):
        self.data_queue = Queue()
        self.event = event
        self.file = open(mainfile, 'x', encoding='utf-8')

    def __call__(self, *args, **kwargs):
        while True:
            if self.data_queue.empty():
                if self.event.is_set():
                    logging.info('Operation completed')
                    break
            else:
                r_file, data = self.data_queue.get()
                logging.info(f"Writing file {r_file.name}")
                self.file.write(f"{data}\n")

    def __del__(self):
        self.file.close()


def reader(data_queue: Queue):
    while True:
        if files.empty():
            logging.info('Operation read completed')
            break

        r_file = files.get()
        logging.info(f'read file {r_file.name}')
        with open(r_file, 'r', encoding="utf-8") as fr:
            data = []
            for line in fr:
                data.append(line)
            all_data = ''.join(data)
            data_queue.put((r_file, all_data))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    event = Event()
    files = Queue()

    list_files = pathlib.Path('.').joinpath("files").glob('*.js')

    [files.put(file) for file in list_files]
    writer = Writer('main.js', event)
    if files.empty():
        logging.info("Nothing!")
    else:
        tw = Thread(target=writer, name='writer')
        tw.start()

        threads = []
        for i in range(2):
            tr = Thread(target=reader, args=(writer.data_queue,), name=f"reader-{i}")
            threads.append(tr)
            tr.start()

        [th.join() for th in threads]
        event.set()
