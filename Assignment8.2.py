import threading

odd_event = threading.Event()
even_event = threading.Event()


def printEven(n):
    for i in range(0, n, 2):
        print(i)
        odd_event.set()
        even_event.clear()
        even_event.wait()

def printOdd(n):
    odd_event.wait()
    for i in range(1, n, 2):
        print(i)
        even_event.set()
        odd_event.clear()
        odd_event.wait()

if __name__ == "__main__":
    n = 99
    t1 = threading.Thread(target=printEven, args=(n,))
    t2 = threading.Thread(target=printOdd, args=(n,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
