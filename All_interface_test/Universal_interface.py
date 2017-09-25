import json
import time
import requests
from multiprocessing import Pool,Process
from datetime import datetime
from company.All_interface_test import connect_sqldb, handle_case
from company.All_interface_test import device_bind

def all_interface(_type,_mode,_dict,_url,_headers,_file):
    url = _type + '://'+_url
    if len(_file) == 0:
        if _mode == 'GET' and _type == 'https' and _headers == None :
            print('1')
            _params = _dict
            try:
                re = requests.get(url=url, params=_params, verify=False).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'GET' and _type == 'http' and _headers == None :
            print('2')
            _params = _dict
            try:
                re = requests.get(url=url, params=_params).json()
            except:
                print('不是json')
                pass
            print(re)
        elif _mode == 'POST' and _type == 'https' and _headers == None :
            print('3')
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, verify=False).json()
            except:
                print('不是json')
            print(re)

        elif _mode == 'POST' and _type == 'http' and _headers == None :
            print('4')
            _data = _dict
            url = url
            try:
                re = requests.post(url=url, data=_data).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'GET' and _type == 'https' and _headers != None :
            print('5')
            headers = _headers
            _params = _dict
            url = url
            try:
                re = requests.get(url=url,params=_params,headers=headers, verify=False).json()
            except:
                print('不是json')

        elif _mode == 'GET' and _type == 'http' and _headers != None :
            print('6')
            headers = _headers
            _params = _dict
            url = url
            try:
                re = requests.post(url=url, params=_params, headers=headers).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'POST' and _type == 'https' and _headers != None :
            print('7')
            headers = _headers
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, headers=headers, verify=False).json()
            except:
                print('不是Json')

        else:
            print('8')
            headers = _headers
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, headers=headers).json()
            except:
                print('不是json')
                #yield connect_sqldb.sql_db(_case_id)
    else:
        if _mode == 'GET' and _type == 'https' and _headers == None:
            print('11')
            _params = _dict
            try:
                re = requests.get(url=url, params=_params, files = _file,verify=False).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'GET' and _type == 'http' and _headers == None:
            print('12')
            _params = _dict
            try:
                re = requests.get(url=url, files = _file,params=_params).json()
            except:
                print('不是json')
                pass
            print(re)
        elif _mode == 'POST' and _type == 'https' and _headers == None:
            print('13')
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, files = _file,verify=False).json()
            except:
                print('不是json')
            print(re)

        elif _mode == 'POST' and _type == 'http' and _headers == None:
            print('14')
            _data = _dict
            url = url
            try:
                re = requests.post(url=url, data=_data,files = _file).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'GET' and _type == 'https' and _headers != None:
            print('15')
            headers = _headers
            _params = _dict
            url = url
            try:
                re = requests.get(url=url, params=_params, headers=headers,files = _file, verify=False).json()
            except:
                print('不是json')

        elif _mode == 'GET' and _type == 'http' and _headers != None:
            print('16')
            headers = _headers
            _params = _dict
            url = url
            try:
                re = requests.post(url=url, params=_params, files = _file,headers=headers).json()
            except:
                print('不是Json')
            print(re)
        elif _mode == 'POST' and _type == 'https' and _headers != None:
            print('17')
            headers = _headers
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, headers=headers,files = _file, verify=False).json()
            except:
                print('不是Json')

        else:
            print('18')
            headers = _headers
            url = url
            _data = _dict
            try:
                re = requests.post(url=url, data=_data, files = _file,headers=headers).json()
            except:
                print('不是json')
                # yield connect_sqldb.sql_db(_case_id)
    try:
        re = json.dumps(re)
        sql14 = 'select app_id,interface_url from tb_case_independence where case_id = %s'%_case_id
        uu = connect_sqldb.select_db(sql14)
        uu =uu[0]                       #针对返回结果的插入结果表的
        _app_id = uu[0]
        _interface_url = uu[1]
        sql15 = 'select %s from interface_result where case_id = %s'%('app_id',_case_id)
        result = connect_sqldb.select_db(sql15)
        re = re.encode('utf-8').decode('unicode-escape')
        if len(result) == 0:
            connect_sqldb.insert_into('interface_result', _case_id, _app_id, _interface_url, re, '')
        else:
            sql16 = 'delete from interface_result where case_id = %s '%_case_id
            connect_sqldb.delete_db(sql16)
            connect_sqldb.insert_into('interface_result', _case_id, _app_id, _interface_url, re, '')

        re = json.loads(re)

        if re['code'] == 0:
            try:
                if 'accessToken' in re['data']:
                    w = re['data']['accessToken']
                    sql18 = 'select * from het_accesstoken where appid = %s'%_app_id
                    k = connect_sqldb.select_db(sql18)
                    if len(k) == 0:
                        connect_sqldb.insert_into('het_accesstoken', _app_id, w)
                    else:
                        print('擦如accesstoken')
                        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        dt = dt.split('-')
                        dt1 = dt[2].split(' ')
                        dt2 = dt1[1].split(':')
                        dt = dt[0] + dt[1] + dt1[0] + dt2[0] + dt2[1] + dt2[2]
                        sql19 = "update het_accesstoken set accesstoken = '%s',update_time = %s where appid = %s"%(w,dt,_app_id)
                        connect_sqldb.update_db(sql19)
            except:
                print('返回的不是data数据，code:0')
        elif re['code'] == 100021006 or re['code'] == 100010101:
            print('daolma')
            sql20 = 'select app_id from tb_case_independence where case_id = %s'%_case_id
            s1 = connect_sqldb.select_db(sql20)
            s1 = s1[0][0]
            print('来了')
            print(s1)
            time.sleep(3)
            sql21 = 'update tb_case_independence set app_id = %s where case_id = 1'%s1
            connect_sqldb.update_db(sql21)
            _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(1)
            all_interface(_type, _mode, _dict, _url, _headers,_file)
            time.sleep(2)
            _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
            all_interface(_type, _mode, _dict, _url, _headers,_file)
        else:
            pass

        if _case_id == 6:  # 针对设备device_id的
            _re = re['data']
            for i in range(len(_re)):
                devicename = _re[i]['productName']
                devicecode = _re[i]['deviceCode']
                deviceid = _re[i]['deviceId']
                productid = _re[i]['productId']
                mac = _re[i]['macAddress']
                onlie = _re[i]['onlineStatus']
                share = _re[i]['share']
                id = ''
                sql17 = "delete from tb_deviceid where device_id = '%s'" % deviceid
                connect_sqldb.delete_db(sql17)
                connect_sqldb.insert_into('tb_deviceid', id, productid, deviceid,
                                          devicecode, devicename, mac, onlie, share)
    except:
        print('返回的不是json数据，直接结束')

if __name__ == '__main__':
    # _case_id = (_case_id for _case_id in [1,2])    #单个设备绑定  (C家绑定)
    # for _case_id in _case_id:
    #     if _case_id == 2:
    #         _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
    #         all_interface(_type, _mode, _dict, _url, _headers,_file)
    #         time.sleep(5)
    #         device_bind.main()
    #     else:
    #         _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
    #         all_interface(_type, _mode, _dict, _url, _headers,_file)


    _case_id = 54#执行单条接口id
    _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
    all_interface(_type, _mode, _dict, _url, _headers,_file)

    # _case_id = 30
    # sql1 = "SELECT cookie FROM beerglass_cookie WHERE id BETWEEN 2  AND 15"
    # rs = connect_sqldb.select_db(sql1)
    # _all_cookie = []
    # for i in rs:
    #     _all_cookie.append(i[0])
    # sql2 = "SELECT _uuid FROM beerglass_device WHERE id BETWEEN 2  AND 15"
    # rs1 = connect_sqldb.select_db(sql2)
    # _all_device = []
    # for i in rs1:
    #     _all_device.append(i[0])
    # __dict = dict(map(lambda x, y: [x, y], _all_cookie, _all_device))
    # for k,v in __dict.items():
    #     sql = "update het_json set cookie = '%s' where case_id = %s " % ('beerglass_openId=' + k, _case_id)
    #     connect_sqldb.update_db(sql)
    #     sql1 = "update tb_case_independence set parameter_value = '%s' where case_id = %s" % (v, _case_id)
    #     connect_sqldb.update_db(sql1)
    #     _type, _mode, _dict, _url, _headers = handle_case.sql_db(_case_id)
    #     all_interface(_type, _mode, _dict, _url, _headers)


    # sql0 = "select count(*) from tb_case_independence"
    # rss = connect_sqldb.select_db(sql0)
    # rss = rss[0][0]
    # _case_id = 1
    # while True:
    #
    #     _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
    #     all_interface(_type, _mode, _dict, _url, _headers,_file)
    #     _case_id += 1
    #     time.sleep(2)
    #     if _case_id in [2,54,55]:
    #         _type, _mode, _dict, _url, _headers,_file = handle_case.sql_db(_case_id)
    #         all_interface(_type, _mode, _dict, _url, _headers,_file)
    #         _case_id += 1
    #         time.sleep(5)
    #         device_bind.main()
    #
    #     if _case_id == rss + 1:
    #         break







