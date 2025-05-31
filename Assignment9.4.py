import time

start = time.time()

for i in range(5):
    print("GeeksForGeeks")

time.sleep(1)
end = time.time()

print(f"Total runtime of the program is {end - start} seconds")