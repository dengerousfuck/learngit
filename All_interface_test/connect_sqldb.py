import pymysql
from datetime import datetime
import time
from company.All_interface_test.seting import case_id,appid,interface_id,\
    interface_name,\
    interface_url,parameter_name,parameter_value,_type,_mode,expected_code,\
    _sign,environment_variable ,create_time, update_time, _timestamp,headers,id,_mac,parameter_flag

# def update_db(tb,*args):
#     conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
#     cur = conn.cursor()
#     dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     dt = dt.split('-')
#     dt1 = dt[2].split(' ')
#     dt2 = dt1[1].split(':')
#     dt = dt[0] + dt[1] + dt1[0] + dt2[0] + dt2[1] + dt2[2]
#     sql = "update %s set %s = '%s',update_time = '%s' where %s = %s"%(tb,args[0],args[1],dt,args[2],args[3])
#     print(sql)
#     try:
#         cur.execute(sql)
#         cur.connection.commit()
#     except:
#         conn.rollback()
#     cur.close()
#     conn.close()
# def select_db(tb,*args):
#     conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
#     cur = conn.cursor()
#     try:
#         if type(args[0]) == str:
#             a = list((args[0],)).pop()
#             b = str(a).strip('[]').replace("'", '')
#         else:
#             a = list(args[0])
#             b = str(a).strip('[]').replace("'", '')
#     except:
#         b = args[0]
#     print(args)
#     if len(args[1]) == 0:
#         sql = "select %s from %s where '%s' = '%s'"%(b,tb,args[1],args[2])
#
#     else:
#         sql = "select %s from %s where %s = '%s'" % (b, tb, args[1], args[2])
#     print(sql)
#     try:
#         cur.execute(sql)
#     except:
#         conn.rollback()
#     result=cur.fetchall()
#     cur.close()
#     conn.close()
#     print(result)
#     return result
#
# def delete_db(tb,*args):
#     conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
#     cur = conn.cursor()
#     sql = " delete from %s where %s = '%s'"%(tb,args[0],args[1])
#     print(sql)
#     try:
#         cur.execute(sql)
#         cur.connection.commit()
#     except:
#         conn.rollback()
#     cur.close()
#     conn.close()
#     return 'ok'
#
#
# def insert_into(tb,*args):
#     conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test',charset='utf8')
#     cur = conn.cursor()
#     cc = time.time()
#     cc1 = cc * 1000
#     cc2 = str(cc1)[:13]
#     dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     dt = dt.split('-')
#     dt1 = dt[2].split(' ')
#     dt2 = dt1[1].split(':')
#     dt = dt[0] + dt[1] + dt1[0] + dt2[0] + dt2[1] + dt2[2]
#     args = list(args)
#     try:
#         cur.execute("select column_name from information_schema.columns where table_name='%s' and table_schema='test'"%(tb))
#     except:
#         conn.rollback()
#     _args = cur.fetchall()
#     a = []
#     for i in _args:
#         a.append(i[0])
#     if 'create_time' in a:
#         count = a.index('create_time')
#         while count >= len(args):
#             args.append('')
#         args[count] = dt
#     if 'update_time' in a:
#         count = a.index('update_time')
#         while count >= len(args):
#             args.append('')
#         args[count] = dt
#     if '_timestamp' in a:
#         count = a.index('_timestamp')
#         args[count] = cc2
#     args = tuple(args)
#     b= str(a).strip('[]').replace("'",'')
#     try:
#         sql = "insert into %s (%s) values %s" % (tb,b,args)
#         print(sql)
#         cur.execute(sql)
#         cur.connection.commit()
#
#     except:
#         conn.rollback()
#     cur.connection.commit()
#     cur.close()
#     conn.close()

def select_db(sql):
    db = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
    cur = db.cursor()
    try:
        print(sql)
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
    except Exception as e:
        raise e
    finally:
        cur.close()
        db.close()  # 关闭连接
    return results

def update_db(sql):
    db = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
    cur = db.cursor()
    try:
        print(sql)
        cur.execute(sql)
        cur.connection.commit()
    except Exception as e:
        db.rollback()
    finally:
        db.close()

def insert_into(tb,*args):
    conn = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test',charset='utf8')
    cur = conn.cursor()
    cc = time.time()
    cc1 = cc * 1000
    cc2 = str(cc1)[:13]
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dt = dt.split('-')
    dt1 = dt[2].split(' ')
    dt2 = dt1[1].split(':')
    dt = dt[0] + dt[1] + dt1[0] + dt2[0] + dt2[1] + dt2[2]
    args = list(args)
    try:
        cur.execute("select column_name from information_schema.columns where table_name='%s' and table_schema='test'"%(tb))
    except:
        conn.rollback()
    _args = cur.fetchall()
    a = []
    for i in _args:
        a.append(i[0])
    if 'create_time' in a:
        count = a.index('create_time')
        while count >= len(args):
            args.append('')
        args[count] = dt
    if 'update_time' in a:
        count = a.index('update_time')
        while count >= len(args):
            args.append('')
        args[count] = dt
    if '_timestamp' in a:
        count = a.index('_timestamp')
        args[count] = cc2
    args = tuple(args)
    b= str(a).strip('[]').replace("'",'')
    try:
        sql = "insert into %s (%s) values %s" % (tb,b,args)
        print(sql)
        cur.execute(sql)
        cur.connection.commit()

    except:
        conn.rollback()
    cur.connection.commit()
    cur.close()
    conn.close()



def delete_db(sql):
    db = pymysql.connect(host='127.0.0.1', user='root', port=3307, passwd='', db='test')
    cur = db.cursor()
    try:
        print(sql)
        cur.execute(sql)  # 像sql语句传递参数
        cur.connection.commit()
    except Exception as e:
        db.rollback()
    finally:
        cur.close()
        db.close()
if __name__ == '__main__':

    # _json = {'stop': 2, 'WorkMode': 4, 'Deodorant': 1, 'Sterilize': 1, 'AirDry': 1, 'HotDry': 1, 'Incense': 1,
    #  'LogoBrightness': 23,
    #  'SetHottest': 44, 'FactorySetting': 0, 'Reset': 0, 'CleanStatisticalInfo': 0, 'updateFlag': '4f01'}
    # insert_into('het_accesstoken',30671,'3424324')
    # sql_db(_case_id)
    insert_into('tb_case_independence',case_id, appid, interface_id, interface_name, interface_url, parameter_name,parameter_value, _type, _mode, expected_code, _sign,create_time, update_time, _timestamp,  environment_variable,
                headers,parameter_flag)
    #_json = {"ModeSet":[{"Stages":1,"Pause":1,"TriggerSignal":2,"StageMode":1,"ModeTimingHour":0,"ModeTimingMin":20,"ModeTempHigh":0,"ModeTempLow":200,"SteamSwitch":0,"SteamTimingHour":0,"SteamTimingMin":0}],"ConfigurationType":1,"MenuNumber":"1193","TotalNumberOfStages":1}
    #_json = {"ModeSet": [{"Stages": 1, "Pause": 0, "TriggerSignal": 1, "StageMode": 1, "ModeTimingHour": 0, "ModeTimingMin": 3, "ModeTempHigh": 0, "ModeTempLow": 7, "SteamSwitch": 0, "SteamTimingHour": 0, "SteamTimingMin": 0}, {"Stages": 2, "Pause": 1, "TriggerSignal": 1, "StageMode": 3, "ModeTimingHour": 0, "ModeTimingMin": 1, "ModeTempHigh": 0, "ModeTempLow": 20, "SteamSwitch": 0, "SteamTimingHour": 0, "SteamTimingMin": 0}, {"Stages": 3, "Pause": 1, "TriggerSignal": 1, "StageMode": 5, "ModeTimingHour": 9, "ModeTimingMin": 2, "ModeTempHigh": 0, "ModeTempLow": 20, "SteamSwitch": 0, "SteamTimingHour": 0, "SteamTimingMin": 0}], "ConfigurationType": 2, "MenuNumber": 1078, "TotalNumberOfStages": 3}
    # _json = json.dumps(_json)
    # insert_into('_het_json',21,_json)
    # a= select_db('tb_case_independence', 'parameter_flag', 'case_id', 1)
    # b = a[0][0]
    # print(b)
    # print(type(b))

    # header = {"Accept-Encoding":"gzip, deflate, br","Accept-Language":"zh-CN,zh;q=0.8","Cache-Control":"no-cache",
    #           "Connection":"Upgrade","Host":"wss.clife.net","Origin":"https://open.clife.cn","Pragma":"no-cache",
    #           "Upgrade":"websocket","User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
    #           "Sec-WebSocket-Version":13,"Sec-WebSocket-Extensions":"permessage-deflate; client_max_window_bits",
    #           "Sec-WebSocket-Key":"a/vVeIrzOYWaSJOYxbFQeg=="}