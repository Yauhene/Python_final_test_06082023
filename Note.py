from datetime import datetime


class Note:
    units_num = 0

    def __init__(self, id, title, body, date_mark, time_mark):
        Note.units_num += 1
        # self.now = datetime.now()
        self.title = title
        self.id = id
        self.date_mark = date_mark
        # (
        #     str("{:02d}".format(datetime.now().day))
        #     + "."
        #     + str("{:02d}".format(datetime.now().month))
        #     + "."
        #     + str(datetime.now().year)
        #     + "  "
        # )
        self.time_mark = time_mark
        # (
        #     str(datetime.now().hour)
        #     + ":"
        #     + str(datetime.now().minute)
        #     + ":"
        #     + str(datetime.now().second)
        # )
        self.body = body

    def date_time(self):
        return self.datemark + " (" + self.time_mark + ")"
