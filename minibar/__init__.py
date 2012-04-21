import sys
class MiniBar:
    def __init__(self, update=lambda: 0, title="", min=0, max=1, width=50, percent=True, fill="=", empty=" ", cursor=''):
        self.title = title
        self.width = width
        self.min = min
        self.max = max
        self.update = update
        self.percent = percent
        self.fill = fill
        self.empty = empty
        self.prev_len = 0
        self.cursor = cursor
        if cursor:
            # we need to make room for the cursor
            self.width = self.width - 1

    def draw(self):
        percent = max(min((self.update() - self.min) * 1.0 / self.max, 1), 0)

        num_filled = int(round(percent * self.width))
        num_empty = self.width - num_filled

        new_str ="%s[%s%s%s]%s" % (self.title+": " if self.title else "", self.fill*num_filled, self.cursor, self.empty*num_empty, (" %d%%" % int(round(percent*100))) if self.percent else "")

        sys.stdout.write("\b" * self.prev_len)
        sys.stdout.write(new_str)
        sys.stdout.flush()
        
        self.prev_len = len(new_str)

    def end(self):
        print # just move to a new line
