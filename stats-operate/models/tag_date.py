import pandas as pd

from models.db import Database
from object.obj_tag_date import ObjTagDate


class ModelTagDate:

    @classmethod
    def list_das_tag_by_date(cls, fromDate, toDate):
        listAdsTagDate = []
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = "select tag_id, ad_id, rev_real, click, imp " \
                       "from stats_ads_tags_date where date >= %s and date <= %s;"
            cursor.execute(sqlQuery, ("2019-07-01", "2019-07-30"))
            # cursor.execute(sqlQuery, (fromDate, toDate))
            result = cursor.fetchall()
            if cursor.rowcount > 0:
                df = pd.DataFrame(result)
                df = pd.DataFrame(df.groupby(['tag_id', 'ad_id']).sum()[['rev_real', 'click', 'imp']])
                print(df)
                # row.name[0] = tag_id , row.name[1] = ad_id
                for index, row in df.iterrows():
                    tagDate = ObjTagDate(row.name[0], row.name[1], row["rev_real"], row["click"], row["imp"])
                    listAdsTagDate.append(tagDate)

        except Exception as e:
            print("An exception occurred...." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()
        return listAdsTagDate

    @classmethod
    def create_ads_tags_operate(cls, recordsToInsert):
        print("recordsToInsert", recordsToInsert)
        try:
            cn = Database.connection()
            cursor = cn.cursor(dictionary=True)
            sqlQuery = " insert into operate_tag_ad_date(tag_id,ad_id,date,cpm_7,ctr_7)" \
                       " values(%s,%s,%s,%s,%s)" \
                       " on duplicate key update cpm_7=values(cpm_7), ctr_7=values(ctr_7)"
            cursor.executemany(sqlQuery, recordsToInsert)
            cn.commit()
            if cursor.rowcount > 0:
                print("rowcount :", cursor.rowcount)
        except Exception as e:
            print("Exception ..." + e)
        finally:
            if cn.is_connected():
                cursor.close()
                cn.close()
