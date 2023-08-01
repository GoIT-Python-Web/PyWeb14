from threading import Event, Thread, Timer
from time import sleep
import logging



def склад(поступлення: Event):
    sleep(1)  # 
    logging.debug('Прибув товар...')
    поступлення.set()
    

def відправка_користувачу(поступлення: Event):
    logging.debug('Чекаєм на товар...')
    sleep(0.001)
    поступлення.wait()
    logging.debug('Deliveri...')



def main():
    logging.basicConfig(level=logging.DEBUG, format="%(threadName)s %(message)s")
    e = Event()

    storage = Timer( 5,function=склад, args=(e, ))
    client1 = Thread(target=відправка_користувачу, args=(e, ))
    client2 = Thread(target=відправка_користувачу, args=(e, ))

    client1.start()
    client2.start()
    storage.start()

main()