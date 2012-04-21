minibar
=======

A tiny, easy to use progress bar class written in Python.

Basic Usage
-----------

The only required parameter is a function that returns a value in [0 .. 1], which represents the filled ratio of the progres bar.

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

Additional parameters may be passed that allow you to customize the appearance of the progress bar.

If your update function returns a value outside of [0 .. 1], you can specify the `min` and `max` value.

The `title` value will display text next to the progress bar. 

Specify the characters used for the filled and empty portions of the progress bar with the `fill` and `empty` parameters.

You may specify an optional `cursor` parameter that will appear between the filled and empty areas of the progress bar.

If `percent` is set to False, the percentage label to the right of the progress bar will not be displayed.

By default, the width of the progress bar (not including the borders) is 50 characters. You man adjust that with the `width` parameter.

    from minibar import MiniBar
    from time import sleep

    def myUpdateFunc():
        return i

    m = MiniBar(update=myUpdateFunc, title="Processing", width=60, min=40, max=120, fill='+', empty='.', cursor='>', percent=False)

    for i in range(40, 120):
        m.draw()
        sleep(0.05)

    m.finish()

Example output:

    Processing: [++++++++++++>...............................................]

Other fun styles
------------

    m = MiniBar(lambda: i, fill='/', empty='|') # dominoes
    [///////////////////////|||||||||||||||||||||||||||] 45%

    m = MiniBar(lambda: i, fill='~', cursor='✈') # airplane
    [~~~~~~~~~~~~~~~~~~~~~~✈                           ] 45%

    m = MiniBar(lambda: i, fill=' ', cursor='o') # rolling ball
    [                      o                           ] 45%