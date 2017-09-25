import json
import  time
import hashlib
from . import connect_sqldb, password
from datetime import datetime

def sql_db(_case_id):
    sql = 'select parameter_name, parameter_value, _mode,_type, interface_url, _sign, environment_variable, headers, app_id, parameter_flag ' \
          'from tb_case_independence where case_id = %s'%_case_id
    _result = connect_sqldb.select_db(sql)
    print(sql)
    result = _result[0]
    try:
        result_name = result[0]
        _result_name = result_name.split('|')
        result_value = result[1]
        _result_value = result_value.split('|')
    except:
        pass
    _mode = result[2]
    _type = result[3]
    _url = result[4]
    _sign = result[5]
    environment_variable = result[6]
    headers = result[7]
    app_id = result[8]
    _parameter_flag = result[9]
    _file = {}
    sql1 = 'select app_secret from het_appid where appid = %s'%app_id
    _appsecret = connect_sqldb.select_db(sql1)
    print(sql1)
    appsecret = _appsecret[0][0]
    sql2 = 'select environment_value from environment where environment_variable = %s'%environment_variable
    print(sql2)
    _dns = connect_sqldb.select_db(sql2)

    dns = _dns[0][0]
    _url = dns + _url
    if _parameter_flag == None:
        pass
    else:
        parameter_flag = _parameter_flag.split(';')
        parameter_flag.pop()
        for i in range(len(parameter_flag)):
            j = parameter_flag[i].split('|')
            rs ,tb,op,ve= j[0],j[1],j[2],j[3]
            if tb in ['_het_json','het_json','device_json','conf_device_json']:
                if ve == '_case_id':
                    sql3 = 'select json from %s where %s = %s'%(tb,op,_case_id)
                    print(sql3)
                    _rs = connect_sqldb.select_db(sql3)
                    _rs = _rs[0]
                else:
                    sql4 = 'select json from %s where %s = %s' % (tb, op, ve)
                    print(sql4)
                    _rs = connect_sqldb.select_db(sql4)
                    _rs = _rs[0]
            elif tb == 'tb_case_independence':
                if ve == '_case_id':
                    sql5 = 'select app_id from %s where %s = %s' % (tb, op, _case_id)
                    print(sql5)
                    _rs = connect_sqldb.select_db(sql5)
                    _rs = _rs[0]
                else:
                    sql6 = 'select json from %s where %s = %s' % (tb, op, ve)
                    print(sql6)
                    _rs = connect_sqldb.select_db(sql6)
                    _rs = _rs[0]
            elif tb == 'beerglass_device':
                sql55 = 'select _uuid from %s where %s = %s' % (tb, op, ve)
                print(sql55)
                _rs = connect_sqldb.select_db(sql55)
                _rs = _rs[0]
            else:
                if ve == '_case_id':
                    sql7 = 'select device_id from %s where %s = %s' % (tb, op, _case_id)
                    print(sql7)
                    _rs = connect_sqldb.select_db(sql7)
                    _rs = _rs[0]
                else:

                    sql8 = "select device_id from %s where %s = '%s'" % (tb, op, ve)
                    print(sql8)
                    _rs = connect_sqldb.select_db(sql8)
                    _rs = _rs[0]
            _rs = str(_rs[0])
            index_count = _result_name.index(rs)
            _result_value[index_count] = _rs

    if 'timestamp' in _result_name:
        cc = time.time()
        cc1 = cc * 1000
        cc2 = str(cc1)[:13]
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        dt = dt.split('-')
        dt1 = dt[2].split(' ')
        dt2 = dt1[1].split(':')
        dt = dt[0] + dt[1] + dt1[0] + dt2[0] + dt2[1] + dt2[2]
        sql9 =  'update tb_case_independence set _timestamp = %s,update_time = %s where case_id = %s'% (cc2,dt,_case_id)
        print(sql9)
        connect_sqldb.update_db(sql9)
        timestamp_index = _result_name.index('timestamp')
        _result_value[timestamp_index] = cc2
    if 'accessToken' in _result_name:
        print('进来了')
        sql10 = 'select app_id from tb_case_independence where case_id = %s'%_case_id
        print(sql10)
        rs1 = connect_sqldb.select_db(sql10)
        rs1 = rs1[0][0]
        sql11 = 'select accesstoken from het_accesstoken where appid = %s'%rs1
        print(sql11)
        rs = connect_sqldb.select_db(sql11)
        result_accesstoken = rs[0][0]
        index_count = _result_name.index('accessToken')
        _result_value[index_count] = result_accesstoken
    if 'password' in _result_name:
        index_count = _result_name.index('password')
        ps = _result_value[index_count]
        md5 = password._md5(ps)
        b4 = password._baseword(md5)
        _password = b4 + appsecret
        n = hashlib.md5(_password.encode('utf-8')).hexdigest()
        index_count = _result_name.index('password')
        _result_value[index_count] = n
    if  headers == '1':
        sql12 = 'select json,cookie from het_json where case_id = %s'%_case_id
        print(sql12)
        ss = connect_sqldb.select_db(sql12)
        _headers = ss[0][0]
        cookie = ss[0][1]
        _headers = json.loads(_headers)
        _headers['Host'] =  dns
        _headers['Cookie'] = cookie
    else:
        _headers = None
    if headers == '2':
        sql12 = 'select json from _het_json where case_id = %s' % _case_id
        print(sql12)
        ss = connect_sqldb.select_db(sql12)
        _headers = None
        file = ss[0][0]
        _file = json.loads(file)
    if _sign == 1:
        __dict = dict(map(lambda x,y:[x,y],_result_name,_result_value))
        _dict = dict(sorted(__dict.items(),key=lambda __dict:__dict[0]))
        requrl = _url
        param = _mode + _type + '://' + requrl
        list = []
        for key in _dict.keys():
            list.append(key)
            list.append("=")
            list.append(_dict[key])
            list.append("&")
        for item in list:
            param += item
        param += appsecret
        #param = _mode + _type + '://' + requrl
        #param = param + parse.urlencode(_dict) + '&'  #json格式数据编码有问题
        #param += appsecret
        print(param)
        sign = password._md5(param)
        _result_name.append('sign')
        _result_value.append(sign)
    __dict = dict(map(lambda x, y: [x, y], _result_name, _result_value))
    _dict = dict(sorted(__dict.items(), key=lambda __dict: __dict[0]))
    print(_type,_mode,_dict,_url,_headers)
    return _type,_mode,_dict,_url,_headers,_file