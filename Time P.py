import time

localtime = time.localtime(time.time())
print(localtime)

def procedure():
    time.sleep(2.5)


# time.clock
t0 = time.clock()
procedure()
print(time.clock() - t0)

# time.time
t0 = time.time()
procedure()
print(time.time() - t0)
