from datetime import date, timedelta

from model.tag_opera_date import TagOperaDateModel
from object.tag_opera_date import TagOperaDate


class TagOperaDateControl:

    @classmethod
    def operateTagByDate(cls, fromDate, toDate):
        dateYesterday = date.today() - timedelta(days=1)
        recordsToInsert = []
        recordsToUpdate = []
        listAdsTag = TagOperaDateModel.listAdsTagByDate(fromDate, toDate)
        listTagOperate = TagOperaDateModel.listAdsTagsOperate(dateYesterday)
        for tag in listAdsTag:
            cpm7 = (tag.revReal / tag.imp) / 7
            ctr7 = (tag.click / tag.imp) / 7
            item = (tag.tagId, tag.adId, dateYesterday, int(round(cpm7, 2)), float(round(ctr7, 2)))
            # item : (44, 2644, datetime.date(2020, 7, 14), 0, 0.0) , item[3] = cmp, item[4] = ctr
            if item in listTagOperate:
                indexTag = listTagOperate.index(item)
                # if new value different current value then update
                if item[3] != listTagOperate[indexTag][3] or item[4] != listTagOperate[indexTag][4]:
                    tagOpera = TagOperaDate(item[0], item[1], item[2], item[3], item[4])
                    recordsToUpdate.append(tagOpera)
            else:
                print(item)
                recordsToInsert.append(item)
        if len(recordsToUpdate) > 0:
            for record in recordsToUpdate:
                TagOperaDateModel.updateAdsTagsOperate(record.cpm7, record.ctr7, record.tagId, record.adId, record.date)
        if len(recordsToInsert) > 0:
            TagOperaDateModel.createAdsTagsOperate(recordsToInsert)

        return listAdsTag
