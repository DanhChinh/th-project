import time
def setInterval(seconds, start = time.time()):
    time.sleep(seconds)
    print(f"setInterval:{int(time.time()-start)}s")
    return setInterval(seconds,start)
setInterval(1)