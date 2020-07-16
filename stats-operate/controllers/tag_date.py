from datetime import date, timedelta

from models.tag_date import ModelTagDate


class ControllerTagDate:

    @classmethod
    def operate_tag_by_date(cls, fromDate, toDate):
        dateYesterday = date.today() - timedelta(days=1)
        recordsToInsert = []
        listAdsTag = ModelTagDate.list_das_tag_by_date(fromDate, toDate)

        for tag in listAdsTag:
            cpm7 = (tag.revReal / tag.imp) / 7
            ctr7 = (tag.click / tag.imp) / 7
            item = (tag.tagId, tag.adId, dateYesterday, int(round(cpm7)), float(round(ctr7, 2)))
            recordsToInsert.append(item)

        # process insert multiple record
        ModelTagDate.create_ads_tags_operate(recordsToInsert)

        return listAdsTag
