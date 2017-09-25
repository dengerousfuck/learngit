import socket
import time
import binascii
import struct
import json
import subprocess
from company.All_interface_test import connect_sqldb

def pro():
    sql1 = "select result_json from interface_result where case_id = 2"
    rs = connect_sqldb.select_db(sql1)
    rs = rs[0][0]
    rs = json.loads(rs)
    userkey = rs['data']['userKey'].encode('utf-8')
    userkey = binascii.b2a_hex(userkey).decode()
    sql2 = 'select parameter_name, parameter_value, _mode,_type, interface_url, _sign, environment_variable, headers, app_id, parameter_flag ' \
           'from tb_case_independence where case_id = 2'
    _result = connect_sqldb.select_db(sql2)
    print(sql2)
    result = _result[0]
    try:
        result_name = result[0]
        _result_name = result_name.split('|')
        result_value = result[1]
        _result_value = result_value.split('|')
    except:
        pass
    productid_index = _result_name.index('productId')
    product_id = _result_value[productid_index]
    sql3 = "select device_key from open_device where product_id = %s" % product_id
    _rs = connect_sqldb.select_db(sql3)
    devicekey = _rs[0][0].encode('utf-8')
    devicekey = binascii.b2a_hex(devicekey).decode()
    return devicekey + userkey
class data_frame():
    def __init__(self):
        pass

    def device_protocol_header():
        protocol_header = '5A'
        _protocol_header = string_conversion(protocol_header)
        return _protocol_header

    def device_protocol_data():
        protocol_data = '4000'
        _protocol_data = string_conversion(protocol_data)
        return _protocol_data

    def device_protocol_reserved():  # 保留字节
        protocol_reserved = '0000000000000000'
        _protocol_reserved = string_conversion(protocol_reserved)
        return _protocol_reserved

    def device_control_data(self, data):  # 控制字的选择
        if data == 1:
            control_data = '0402'
        elif data == 2:
            control_data = '0401'
        else:
            return
        return string_conversion(control_data)

    def device_detailed_data(self, data):  # 控制内容选择（加密、心跳、故障）
        if data == 1:
            detailed_data = '00000000'  # 344434637333538393833373533443341
        elif data == 2:
            detailed_data = pro() + '0002020101004C50423130302D312D3030303100000000000000000000000000030000000100000000' \
                                    '1C024865742D413136313132410000000000000000000000000000000000000000000000000000'#1C02
        else:
            return
        return string_conversion(detailed_data)

    def device_type_productid():
        type_productid = devicecode  #'0000C46E00070E01'德赛    #修改产品大小类   产品ID号
        _type_productid = string_conversion(type_productid)
        return _type_productid

    def device_mac():
        _mac = mac          #'ACCF23D92FD2'德赛                  #修改设备的MAC地址
        _mac = string_conversion(_mac)
        return _mac


def het_CRC(dat):
    crc = 0xFFFF
    for j in dat[1::]:
        crc = crc ^ j
        for i in range(8):
            if (crc & 0x01) == 1:
                crc = (crc >> 0x01) ^ 0X8408
            else:
                crc = crc >> 0x01
    return ~crc & 0xFFFF


def encryption():  # 加密数据帧处理
    n2 = iter(range(0, pow(2, 16)))
    P1 = data_frame.device_protocol_header()  # 5A协议（不变）
    P3 = data_frame.device_protocol_data()  # 协议类型（不变）00 00 C4 C5 00 0F 01 01
    P4 = data_frame.device_type_productid()  # 设备大小类，产品号  00 00 C4 23 00 13 01 01
    P5 = data_frame.device_mac()  # 5C CF 7F 27 5E 9B # mac地址 b'\xAC\xCF\x23\xDB\xFE\xEE'
    P6 = struct.pack('>HH', 0, next(n2))  # 数据帧
    P7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    P8 = data_frame.device_control_data(self=None, data=1)  # 控制数据
    P9 = data_frame.device_detailed_data(self=None, data=1)  # 数据的内容
    q = len(P3 + P4 + P5 + P6 + P7 + P8 + P9) + 4
    P2 = struct.pack('>H', q)  # 两个字节的数据长度
    data0 = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
    t = data0[0][::] + data0[1][::] + data0[2][::] + data0[3][::] + data0[4][::] + data0[5][::] \
        + data0[6][::] + data0[7][::] + data0[8][::]
    ret = het_CRC(t)
    a = hex(ret)[2:6]
    if len(a) == 4:
        a = a
    elif len(a) == 3:
        a = '0' + a
    elif len(a) == 2:
        a = '00' + a
    else:
        a = '000' + a
    P10 = binascii.a2b_hex(a.encode('ascii'))
    list_data1 = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
    w = list_data1[0][::] + list_data1[1][::] + list_data1[2][::] + list_data1[3][::] + list_data1[4][::] + list_data1[
                                                                                                                5][::] + \
        list_data1[6][::] + list_data1[7][::] + list_data1[8][::] + list_data1[9][::]
    print(binascii.b2a_hex(w))
    sock.send(w)
    recv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(recv_data1))
    time.sleep(2)


def synchronous_data():  # 加密数据帧处理
    n1 = iter(range(0, pow(2, 16)))
    P1 = data_frame.device_protocol_header()  # 5A协议（不变）
    P3 = data_frame.device_protocol_data()  # 协议类型（不变）00 00 C4 C5 00 0F 01 01
    P4 = data_frame.device_type_productid()  # 设备大小类，产品号  00 00 C4 23 00 13 01 01
    P5 = data_frame.device_mac()  # 5C CF 7F 27 5E 9B # mac地址 b'\xAC\xCF\x23\xDB\xFE\xEE'
    P6 = struct.pack('>HH', 0, next(n1))  # 数据帧
    P7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    P8 = data_frame.device_control_data(self=None, data=2)  # 控制数据
    P9 = data_frame.device_detailed_data(self=None, data=2)  # 数据的内容
    q = len(P3 + P4 + P5 + P6 + P7 + P8 + P9) + 4
    P2 = struct.pack('>H', q)  # 两个字节的数据长度
    data0 = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
    t = data0[0][::] + data0[1][::] + data0[2][::] + data0[3][::] + data0[4][::] + data0[5][::] \
        + data0[6][::] + data0[7][::] + data0[8][::]
    ret = het_CRC(t)
    a = hex(ret)[2:6]
    if len(a) == 4:
        a = a
    elif len(a) == 3:
        a = '0' + a
    elif len(a) == 2:
        a = '00' + a
    else:
        a = '000' + a
    P10 = binascii.a2b_hex(a.encode('ascii'))
    list_data1 = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]
    w = list_data1[0][::] + list_data1[1][::] + list_data1[2][::] + list_data1[3][::] + list_data1[4][::] + list_data1[
                                                                                                                5][::] + \
        list_data1[6][::] + list_data1[7][::] + list_data1[8][::] + list_data1[9][::]
    print(binascii.b2a_hex(w))
    sock.send(w)
    recv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(recv_data1))
    time.sleep(2)


def string_conversion(data):  # 字符串转化为字节串
    data_bin = binascii.a2b_hex(data.encode('ascii'))
    return data_bin


def main():
    global sock, mac, devicecode
    sql = 'select parameter_name,parameter_value,environment_variable from tb_case_independence where case_id = %s'%2
    _result = connect_sqldb.select_db(sql)
    result = _result[0]
    try:
        result_name = result[0]
        _result_name = result_name.split('|')
        result_value = result[1]
        _result_value = result_value.split('|')
        ev = result[2]
    except:
        pass
    index_count = _result_name.index('mac')
    mac = _result_value[index_count]
    index_count1 = _result_name.index('productId')
    productid = _result_value[index_count1]
    sql1 = "select device_code from open_device where product_id = %s"%productid
    rs = connect_sqldb.select_db(sql1)
    devicecode = rs[0][0]
    if ev == 1:
        host = '203.195.139.139'
        #'200.200.200.52'
        port = 9001
    elif ev == 2:
        host = '119.29.116.47'
        port = 9001
    else:
        host = '61.141.158.190'
        port = 9000

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(host)
        sock.connect((host, port))
    except socket.error as e:
        print(e)
    encryption()
    synchronous_data()
    sock.close()
    time.sleep(1)
    subprocess.call(["python","E:\\python所有项目\company\company\All_interface_test/Generic_script.py"])

if __name__ == '__main__':
    main()