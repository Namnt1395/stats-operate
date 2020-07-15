import pandas as pd

from model.db import Database
from object.tag_ads_date import TagAdsDate


class TagOperaDateModel:

    @classmethod
    def listAdsTagByDate(cls, fromDate, toDate):
        listAdsTagDate = []
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = "select tag_id, ad_id, rev_real, click, imp " \
                       "from stats_ads_tags_date where date >= %s and date <= %s;"
            # cursor.execute(sqlQuery, ("2019-07-01", "2019-07-30"))
            cursor.execute(sqlQuery, (fromDate, toDate))
            result = cursor.fetchall()
            if cursor.rowcount > 0:
                df = pd.DataFrame(result)
                df = pd.DataFrame(df.groupby(['tag_id', 'ad_id']).sum()[['rev_real', 'click', 'imp']])
                # row.name[0] = tag_id , row.name[1] = ad_id
                for index, row in df.iterrows():
                    tagDate = TagAdsDate(row.name[0], row.name[1], row["rev_real"], row["click"], row["imp"])
                    listAdsTagDate.append(tagDate)

        except Exception as e:
            print("An exception occurred...." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()
        return listAdsTagDate

    @classmethod
    def createAdsTagsOperate(cls, recordsToInsert):
        print("recordsToInsert", recordsToInsert)
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = " insert into operate_tag_ad_date(tag_id,ad_id,date,cpm_7,ctr_7)" \
                       " values(%s,%s,%s,%s,%s)"
            cursor.executemany(sqlQuery, recordsToInsert)
            cn.commit()
            if cursor.rowcount > 0:
                print("insert success number record :", cursor.rowcount)
        except Exception as e:
            print("Exception ..." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()

    @classmethod
    def updateAdsTagsOperate(cls, cpm7, ctr7, tagId, adId, date):
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = "  update operate_tag_ad_date set cpm_7 = %,ctr_7 = %s" \
                       "  where tag_id = %s and ad_id= %s and date=%s"
            cursor.executemany(sqlQuery, (cpm7, ctr7, tagId, adId, date))
            cn.commit()
            if cursor.rowcount > 0:
                print("insert success number record :", cursor.rowcount)
        except Exception as e:
            print("Exception ..." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()

    @classmethod
    def listAdsTagsOperate(cls, date):
        listAdsTagDateOperate = []
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = "select tag_id, ad_id, `date`, cpm_7, ctr_7 from operate_tag_ad_date where" \
                       " date >= %s and date <= %s;"
            cursor.execute(sqlQuery, (date, date))
            print(cursor)
            result = cursor.fetchall()
            for row in result:
                tagInfo = (row["tag_id"], row["ad_id"], row["date"], row["cpm_7"], row["ctr_7"])
                listAdsTagDateOperate.append(tagInfo)
        except Exception as e:
            print("Exception ..." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()
        return listAdsTagDateOperate
