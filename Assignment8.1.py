import threading
def print_even_numbers():
    print("List of even numbers:")
    for i in range(30, 51, 2):
        print(i, end = " ")

def print_odd_numbers():
    print("\nList of odd numbers:")
    for i in range(31, 51, 2):
        print(i, end = " ")

even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)

even_thread.start()
odd_thread.start()

even_thread.join()
odd_thread.join()