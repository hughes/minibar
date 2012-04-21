minibar
=======

A tiny, easy to use progress bar class written in Python.

Basic Usage
-----------

    from minibar import MiniBar
    from time import sleep

    m = MiniBar(lambda: i/100.0)

    for i in range(100):
        m.draw()
        sleep(0.05)

    m.finish()

Example output:

    [================================                  ] 64%

Advanced Usage
--------------

    from minibar import MiniBar
    from time import sleep

    def myUpdateFunc():
        return i

    m = MiniBar(update=myUpdateFunc, title="Processing", width=60, min=40, max=120, fill='+', empty='.', cursor='>', percent=False)

    for i in range(120):
        m.draw()
        sleep(0.05)

    m.finish()

Example output:

    Processing: [++++++++++++>...............................................]

Other fun styles
------------

    m = MiniBar(lambda: i, fill='/', empty='|') # dominoes
    [///////////////////////|||||||||||||||||||||||||||] 45%

    m = MiniBar(lambda: i, fill='~', empty=' ', cursor='✈') # airplane
    [~~~~~~~~~~~~~~~~~~~~~~✈                           ] 45%