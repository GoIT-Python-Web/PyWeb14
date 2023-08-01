from threading import Event, Thread, Timer
from time import sleep
import logging



class Storage:
    def __init__(self, goods: list=[]) -> None:
        self.goods = goods

    @staticmethod
    def arrival(goods_arrived: Event):
        logging.debug('Гармошки прибули...')
        goods_arrived.set()

class Client:
    def __init__(self, name, whishlist=[]):
        self.name = name
        self.whishlist = whishlist
    

class Store:
    def __init__(self, storage: Storage, clients: list[Client]=[]):
        self.storage = storage
        self.clients = clients


    def queue_client(self, client: Client):
        self.clients.append(client)
    
    def send_delivery(self, goods_available:Event):
        logging.debug('Чекаєм на товар...')
        sleep(0.001)
        goods_available.wait()
        for client in self.clients:
            logging.debug('Відправка товару клієнту...')
            sleep(5)
            # подумайте як можна запобігти проблем пов'язаних з видаленням клієнтів в мультипоточності
            self.clients.remove(client)


def main():
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    завіз_товару = Event()

    storage = Storage()
    rozetka = Store(storage=storage)
    for i in range(10):
        client = Client(i)
        rozetka.queue_client(client=client)

    delivery_manager1 = Thread(target=rozetka.send_delivery,  args=(завіз_товару, ))
    delivery_manager2 = Thread(target=rozetka.send_delivery,  args=(завіз_товару, ))
    delivery_manager3 = Thread(target=rozetka.send_delivery,  args=(завіз_товару, ))
    delivery_manager4 = Thread(target=rozetka.send_delivery,  args=(завіз_товару, ))
    delivery_manager5 = Thread(target=rozetka.send_delivery,  args=(завіз_товару, ))

    delivery_manager1.start()
    delivery_manager2.start()
    delivery_manager3.start()
    delivery_manager4.start()
    delivery_manager5.start()
    harmonicas_arrival = Timer(3, storage.arrival, args=(завіз_товару, ))
    harmonicas_arrival.start()




main()