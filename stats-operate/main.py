from datetime import date, timedelta

from controller.tag_opera_date import TagOperaDateControl


class Main:
    optionDay = 7
    toDate = date.today() - timedelta(days=1)
    fromDate = toDate - timedelta(days=optionDay)

    tagDate = TagOperaDateControl()
    tagDate.operateTagByDate(fromDate, toDate)
