import time
from datetime import date, timedelta

from controllers.tag_date import ControllerTagDate


class Main:
    if __name__ == '__main__':
        optionDay = 7
        toDate = date.today() - timedelta(days=1)
        fromDate = toDate - timedelta(days=optionDay)
        tagDate = ControllerTagDate()

        # process tag date
        tagDate.operate_tag_by_date(fromDate, toDate)
        time.sleep(60)
        print("Printed after 60 seconds.")
