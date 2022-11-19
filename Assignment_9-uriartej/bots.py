import threading
import json
from time import sleep

def bot_fetcher(items, cart, lock):
    inventory = {}
    with open('inventory.dat', 'r') as f:
        inventory = json.load(f)
    for i in items:
        values = inventory[i]
        slp = values[1]
        items = values[0]
        sleep(slp)
        lock.acquire()
        cart.append([i, items])
        lock.release()


def bot_clerk(items):
    bot_0 = []
    bot_1 = []
    bot_2 = []
    cart = []
    threads = []
    lock = threading.Lock()
    for n,j in enumerate(items):
        bot_num = n % 3
        if bot_num == 0:
            bot_0.append(j)
        elif bot_num == 1:
            bot_1.append(j)
        elif bot_num == 2:
            bot_2.append(j)
    if len(bot_0) > 0:
        p = threading.Thread(target = bot_fetcher, args = (bot_0, cart, lock))
        p.start()
        threads.append(p)
    if len(bot_1) > 0:
        p = threading.Thread(target = bot_fetcher, args = (bot_1, cart, lock))
        p.start()
        threads.append(p)
    if len(bot_2) > 0:
        p = threading.Thread(target = bot_fetcher, args = (bot_2, cart, lock))
        p.start()
        threads.append(p)
    for p in threads:
        p.join()
    return cart