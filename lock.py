import threading
import time

saldo_global = 0
lock = threading.Lock()


def test():
    for i in range(100):
        t = threading.Thread(target=printer, args=(i,) )
        t.start()

def printer(id):
    lock.acquire()
    print('hola',id)
    print('release',id)
    lock.release()

test()