from minibar import MiniBar
from time import sleep

m = MiniBar(lambda: i/100.0)

for i in range(101):
    m.draw()
    sleep(0.05)

m.end()

def myUpdateFunc():
    return i

m = MiniBar(update=myUpdateFunc, title="Processing", width=60, min=40, max=120, fill='+', empty='.', cursor='>', percent=False)

for i in range(40, 121):
    m.draw()
    sleep(0.05)

m.end()
