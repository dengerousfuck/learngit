import socket
import time
import struct
import binascii
from company.All_interface_test import connect_sqldb
class data_frame():

    def __init__(self):
        pass
    def device_protocol_header():
        protocol_header = '5A'
        _protocol_header = string_conversion(protocol_header)
        return _protocol_header
    def device_protocol_data():
        protocol_data = '4001'
        _protocol_data = string_conversion(protocol_data)
        return _protocol_data
    def device_protocol_reserved():       #保留字节
        protocol_reserved = '0000000000000000'
        _protocol_reserved = string_conversion(protocol_reserved)
        return _protocol_reserved
    def device_control_data(self,data):     #控制字的选择
        if data == 1:
            control_data = '0402'
        elif data == 2:
            control_data = '0408'
        elif data == 3:
            control_data = '0105'
        elif data == 4:
            control_data = '0104'
        elif data == 5:
            control_data = '010E'
        else:
            return
        return string_conversion(control_data)
    def device_detailed_data(self,data):    #控制内容选择（加密、心跳、故障）
        if data == 1:
            detailed_data = '00000000'
        elif data == 2:
            detailed_data = '00000000000000000000000000000000'
        elif data == 5:
            print(rs1)
            detailed_data = rs1 #'00000000000000000000000000000000'  #选择故障数据内容
        else:
            return
        return  string_conversion(detailed_data)

    def device_type_productid():
        print(rs2)
        type_productid = rs2#'0000C51100070F01'#  #修改产品大小类   产品ID号
        _type_productid = string_conversion(type_productid)
        return _type_productid
    def device_mac():
        print(rs3)
        mac = rs3 #'000EC608A9C3'#           #修改设备的MAC地址
        print(mac)
        _mac= string_conversion(mac)
        return _mac
    def device_startdata():
        print(rs4)
        startdata = rs4#'00000000640000000000000000000000'    #运行数据的初始化值
        _startdata = string_conversion(startdata)
        return _startdata
    def device_control_startdata():
        print(rs5)
        startdata = rs5 #'010202FA021401010101080000000000'   # 控制数据的初始化值
        _startdata = string_conversion(startdata)
        return _startdata
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

def encryption():        #加密数据帧处理
    P1 = data_frame.device_protocol_header()  # 5A协议（不变）
    P3 = data_frame.device_protocol_data()  # 协议类型（不变）00 00 C4 C5 00 0F 01 01
    P4 = data_frame.device_type_productid()  # 设备大小类，产品号  00 00 C4 23 00 13 01 01
    P5 = data_frame.device_mac()#5C CF 7F 27 5E 9B # mac地址 b'\xAC\xCF\x23\xDB\xFE\xEE'
    P6 = struct.pack('>HH', 0, next(n1))  # 数据帧
    P7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    P8 = data_frame.device_control_data(self = None,data = 1)  # 控制数据
    P9 = data_frame.device_detailed_data(self = None,data = 1)  # 数据的内容
    q = len(P3 + P4 + P5 + P6 + P7 + P8 + P9) + 4
    P2 = struct.pack('>H', q)  # 两个字节的数据长度
    data0 = [P1, P2, P3, P4, P5, P6, P7, P8, P9]
    t = data0[0][::] + data0[1][::] + data0[2][::] + data0[3][::] + data0[4][::] + data0[5][::]\
        + data0[6][::] + data0[ 7][::] + data0[8][::]
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
    time.sleep(5)

def heart_beat():     #心跳数据帧处理
    HP1 = data_frame.device_protocol_header()  # 5A协议（不变）
    HP3 = data_frame.device_protocol_data()  # 协议类型（不变）
    HP4 = data_frame.device_type_productid() # 设备大小类，产品号
    HP5 = data_frame.device_mac()#  # mac地址
    HP6 = struct.pack('>HH', 0, next(n2))  # 数据帧
    HP7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    HP8 = data_frame.device_control_data(self = None,data = 2)  # 控制数据
    HP9 = data_frame.device_detailed_data(self = None,data = 2)  # 数据的内容
    Hq = len(HP3 + HP4 + HP5 + HP6 + HP7 + HP8 + HP9) + 4
    HP2 = struct.pack('>H', Hq)  # 两个字节的数据长度
    Hdata0 = [HP1, HP2, HP3, HP4, HP5, HP6, HP7, HP8, HP9]
    Ht = Hdata0[0][::] + Hdata0[1][::] + Hdata0[2][::] + Hdata0[3][::] + Hdata0[4][::] + Hdata0[5][::] + Hdata0[6][::] + \
         Hdata0[7][::] + Hdata0[8][::]
    Hret = het_CRC(Ht)
    Ha = hex(Hret)[2:6]
    if len(Ha) == 4:
        Ha = Ha
    elif len(Ha) == 3:
        Ha = '0' + Ha
    elif len(Ha) == 2:
        Ha = '00' + Ha
    else:
        Ha = '000' + Ha
    HP10 = binascii.a2b_hex(Ha.encode('ascii'))
    Hlist_data1 = [HP1, HP2, HP3, HP4, HP5, HP6, HP7, HP8, HP9, HP10]
    Hw = Hlist_data1[0][::] + Hlist_data1[1][::] + Hlist_data1[2][::] + Hlist_data1[3][::] + Hlist_data1[4][::] + \
         Hlist_data1[5][::] + Hlist_data1[6][::] + Hlist_data1[7][::] + Hlist_data1[8][::] + Hlist_data1[9][::]
    print(binascii.b2a_hex(Hw))
    sock.send(Hw)
    Hrecv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(Hrecv_data1))
    time.sleep(5)

def  operation_data():      #运行数据帧处理
    YP1 = data_frame.device_protocol_header()  # 5A协议（不变）
    YP3 = data_frame.device_protocol_data() # 协议类型（不变）
    YP4 = data_frame.device_type_productid() # 设备大小类，产品号
    YP5 = data_frame.device_mac()# b'\xAC\xCF\x23\xDC\x11\x24'  # mac地址
    YP6 = struct.pack('>HH', 0, next(n3))  # 数据帧
    YP7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    YP8 = data_frame.device_control_data(self = None,data = 3)  # 控制数据
    global PP99
    YP9 = PP99 # 数据的内容
    Yq = len(YP3 + YP4 + YP5 + YP6 + YP7 + YP8 + YP9) + 4
    YP2 = struct.pack('>H', Yq)  # 两个字节的数据长度
    Ydata0 = [YP1, YP2, YP3, YP4, YP5, YP6, YP7, YP8, YP9]
    Yt = Ydata0[0][::] + Ydata0[1][::] + Ydata0[2][::] + Ydata0[3][::] + Ydata0[4][::] + Ydata0[5][::] + Ydata0[6][::] + \
         Ydata0[7][::] + Ydata0[8][::]
    Yret = het_CRC(Yt)
    Ya = hex(Yret)[2:6]
    if len(Ya) == 4:
        Ya = Ya
    elif len(Ya) == 3:
        Ya = '0' + Ya
    elif len(Ya) == 2:
        Ya = '00' + Ya
    else:
        Ya = '000' + Ya
    YP10 = binascii.a2b_hex(Ya.encode('ascii'))
    Ylist_data1 = [YP1, YP2, YP3, YP4, YP5, YP6, YP7, YP8, YP9, YP10]
    Yw = Ylist_data1[0][::] + Ylist_data1[1][::] + Ylist_data1[2][::] + Ylist_data1[3][::] + Ylist_data1[4][::] + \
         Ylist_data1[5][::] + Ylist_data1[6][::] + Ylist_data1[7][::] + Ylist_data1[8][::] + Ylist_data1[9][::]
    print(binascii.b2a_hex(Yw))
    sock.send(Yw)
    Yrecv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(Yrecv_data1))
    time.sleep(5)
def  accept_control():      #接受下发数据帧处理（可以自行处理，对Updateflag的位变化处理）
    _sql = "select control_lenth from device_start_data where product_id = %s"%productid
    rs_ = connect_sqldb.select_db(_sql)
    control_lenth = rs_[0][0]
    global PP0,PP1,PP2,PP3,PP4,PP5,PP6,PP7,PP8,PP9,PP99
    PP0 = buf[:1]
    PP1 = buf[1:3]
    PP2 = buf[3:5]
    PP3 = buf[5:13]
    PP4 = buf[13:19]
    PP5 = buf[19:23]
    PP6 = buf[23:31]
    PP7 = b'\x02\x04'
    PP8 = buf[33:(33+control_lenth)]
    tt = list(PP8)
    PP991 = list(PP99)
    print(tt)
    try:
        lenth_ = control_lenth//8
        tail = []
        for i in range(1,lenth_+1):
            tail.append(bin(list(PP8)[-i]).replace('0b', ''))
            print(tail)
            for j in range(8-len(tail[i-1])):
                tail[i-1] = '0' + tail[i-1]
        print(tail)
        sql = "select handle_control_data,handle_run_data,handle_configuration_data from device_data_option where product_id = %s"%productid
        rs = connect_sqldb.select_db(sql)
        rs_cont = rs[0][0]
        rs_run = rs[0][1]
        rs_conf = rs[0][2]

        if len(rs_run) != 0:
            try:
                rs_run = rs_run.split('|')
            except:
                rs_run = list(rs_run)
            control_value = []
            run_index = []
            run_value = []
            for y in range(lenth_):
                for x in range(8):
                    if tail[y][x] == '1':
                        i = rs_run[7-x].split(';')
                        for j in i:
                            r = str(j).strip("'").strip("()").split(',')
                            print(r)
                            control_value.append(r[0])
                            run_index.append(r[1])
                            run_value.append(r[2])
                        print(control_value)
                        print(run_index)
                        print(run_value)
                        if '_x' in control_value:
                            control_value = [tt[8 * y - x - 1]]
                            run_value = [tt[8 * y - x - 1]]
                            count = 0
                            run_index = int(run_index[count])
                            PP991[run_index - 1] = int(run_value[count])
                            control_value = []
                            run_index = []
                            run_value = []
                        else:
                            count = control_value.index(str(tt[8 * y - x - 1]))
                            print(count)
                            run_index = int(run_index[count])
                            PP991[run_index - 1] = int(run_value[count])
                            control_value = []
                            run_index = []
                            run_value = []

        if len(rs_cont) != 0:
            try:
                rs_cont = rs_run.split('|')
            except:
                rs_cont = list(rs_cont)
            control_value = []
            control_index = []
            _control_value = []
            for y in range(lenth_):
                for x in range(8):
                    if tail[y][x] == '1':
                        i = rs_cont[7 - x].split(';')
                        for j in i:
                            r = str(j).strip("'").strip("()").split(',')
                            control_value.append(r[0])
                            control_index.append(r[1])
                            _control_value.append(r[2])
                        if '_x' in control_value:
                            control_value = [tt[8 * y - x - 1]]
                            _control_value = [tt[8 * y - x - 1]]
                            count = 0
                            control_index = int(control_index[count])
                            tt[control_index - 1] = int(_control_value[count])
                            control_value = []
                            control_index = []
                            _control_value = []
                        else:
                            count = control_value.index(str(tt[8 * y - x - 1]))
                            control_index = int(control_index[count])
                            tt[control_index - 1] = int(_control_value[count])
                            control_value = []
                            control_index = []
                            _control_value = []
    except:
        print('走这里了')
        pass
    print(PP991)
    PP8 = bytes(tt)
    PP99 = bytes(PP991)
    t = PP0 + PP1 + PP2 + PP3 + PP4 + PP5 + PP6 + PP7 + PP8
    m = het_CRC(t)
    q = hex(m)[2:6]
    if len(q) == 4:
        q = q
    elif len(q) == 3:
        q = '0' + q
    elif len(q) == 2:
        q = '00' + q
    else:
        q = '000' + q
    PP9 = binascii.a2b_hex(q.encode('ascii'))
    c = t + PP9
    print(binascii.b2a_hex(c))
    sock.send(c)
    time.sleep(0.1)


def  control_data():      #控制数据帧处理
    KP1 = data_frame.device_protocol_header()  # 5A协议（不变）
    KP3 = data_frame.device_protocol_data()  # 协议类型（不变）
    KP4 = data_frame.device_type_productid()  # 设备大小类，产品号
    KP5 = data_frame.device_mac()             #b'\xAC\xCF\x23\xDC\x11\x24'  # mac地址
    KP6 = struct.pack('>HH', 0, next(n4))     # 数据帧
    KP7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    KP8 = data_frame.device_control_data(self = None,data = 4)  # 控制数据
    KP9 = data_frame.device_control_startdata()  # 数据的内容
    Kq = len(KP3 + KP4 + KP5 + KP6 + KP7 + KP8 + KP9) + 4
    KP2 = struct.pack('>H', Kq)  # 两个字节的数据长度
    Kdata0 = [KP1, KP2, KP3, KP4, KP5, KP6, KP7, KP8, KP9]
    Kt = Kdata0[0][::] + Kdata0[1][::] + Kdata0[2][::] + Kdata0[3][::] + Kdata0[4][::] + Kdata0[5][::] + Kdata0[6][::] + \
          Kdata0[7][::] + Kdata0[8][::]
    Kret = het_CRC(Kt)
    Ka = hex(Kret)[2:6]
    if len(Ka) == 4:
        Ka = Ka
    elif len(Ka) == 3:
        Ka = '0' + Ka
    elif len(Ka) == 2:
        Ka = '00' + Ka
    else:
        Ka = '000' + Ka
    KP10 = binascii.a2b_hex(Ka.encode('ascii'))
    Klist_data1 = [KP1, KP2, KP3, KP4, KP5, KP6, KP7, KP8, KP9, KP10]
    Kw = Klist_data1[0][::] + Klist_data1[1][::] + Klist_data1[2][::] + Klist_data1[3][::] + Klist_data1[4][::] + \
    Klist_data1[5][::] + Klist_data1[6][::] + Klist_data1[7][::] + Klist_data1[8][::] + Klist_data1[9][::]
    print(binascii.b2a_hex(Kw))
    sock.send(Kw)
    Krecv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(Krecv_data1))
    time.sleep(5)
def fault_data():      #故障数据帧处理
    EP1 = data_frame.device_protocol_header()  # 5A协议（不变）
    EP3 = data_frame.device_protocol_data()  # 协议类型（不变）
    EP4 = data_frame.device_type_productid()  # 设备大小类，产品号
    EP5 = data_frame.device_mac()#b'\xAC\xCF\x23\xDC\x11\x24'  # mac地址
    EP6 = struct.pack('>HH', 0, next(n5))  # 数据帧
    EP7 = data_frame.device_protocol_reserved()  # 保留字  8个字节
    EP8 = data_frame.device_control_data(self = None,data = 5)  # 控制数据
    EP9 = data_frame.device_detailed_data(self = None,data = 5)  # 数据的内容
    Eq = len(EP3 + EP4 + EP5 + EP6 + EP7 + EP8 + EP9) + 4
    EP2 = struct.pack('>H', Eq)  # 两个字节的数据长度
    Edata0 = [EP1, EP2, EP3, EP4, EP5, EP6, EP7, EP8, EP9]
    Et = Edata0[0][::] + Edata0[1][::] + Edata0[2][::] + Edata0[3][::] + Edata0[4][::] + Edata0[5][::] + Edata0[6][::] + \
         Edata0[7][::] + Edata0[8][::]
    Eret = het_CRC(Et)
    Ea = hex(Eret)[2:6]
    if len(Ea) == 4:
        Ea = Ea
    elif len(Ea) == 3:
        Ea = '0' + Ea
    elif len(Ea) == 2:
        Ea = '00' + Ea
    else:
        Ea = '000' + Ea
    EP10 = binascii.a2b_hex(Ea.encode('ascii'))
    Elist_data1 = [EP1, EP2, EP3, EP4, EP5, EP6, EP7, EP8, EP9, EP10]
    Ew = Elist_data1[0][::] + Elist_data1[1][::] + Elist_data1[2][::] + Elist_data1[3][::] + Elist_data1[4][::] + \
         Elist_data1[5][::] + Elist_data1[6][::] + Elist_data1[7][::] + Elist_data1[8][::] + Elist_data1[9][::]
    print(binascii.b2a_hex(Ew))
    sock.send(Ew)
    Erecv_data1 = sock.recv(1024)
    print(binascii.b2a_hex(Erecv_data1))
    time.sleep(5)

def configuration_data():
    _sql = "select configuration_lenth from device_start_data where product_id = %s" % productid
    rs_ = connect_sqldb.select_db(_sql)
    configuration_lenth = rs_[0][0]
    print(configuration_lenth)
    global PP0, PP1, PP2, PP3, PP4, PP5, PP6, PP7, PP8, PP9, PP10, PP99
    print(len(buf))
    PP0 = buf[:1]
    PP2 = buf[3:5]
    PP3 = buf[5:13]
    PP4 = buf[13:19]
    PP5 = buf[19:23]
    PP6 = buf[23:31]
    PP7 = b'\x02\x07'
    PP8 = data_frame.device_detailed_data(None, 2)
    w = len(PP2 + PP3 + PP4 + PP5 + PP6 + PP7 + PP8) + 4
    PP1 = struct.pack('>H', w)
    t = PP0 + PP1 + PP2 + PP3 + PP4 + PP5 + PP6 + PP7 + PP8
    m = het_CRC(t)
    q = hex(m)[2:6]
    if len(q) == 4:
        q = q
    elif len(q) == 3:
        q = '0' + q
    elif len(q) == 2:
        q = '00' + q
    else:
        q = '000' + q
    PP9 = binascii.a2b_hex(q.encode('ascii'))
    c = t + PP9
    print(binascii.b2a_hex(c))
    PP10 = buf[33:(33+configuration_lenth)]
    tt = list(PP10)
    PP991 = list(PP99)
    try:

        sql = "select handle_configuration_data from device_data_option where product_id = %s" % productid
        rs = connect_sqldb.select_db(sql)
        rs_conf = rs[0][0]
        if len(rs_conf) != 0:
            try:
                rs_conf = rs_conf.split('|')
            except:
                rs_conf = list(rs_conf)
            run_index = []
            run_value = []
            for j in rs_conf:
                r = str(j).strip("'").strip("()").split(',')
                print(r)
                try:
                    run_index.append(r[0])
                    run_value.append(r[1])
                except:
                    pass
            print(run_index)
            print(run_value)
            if '_x' in run_value:
                b = [i for i in range(len(run_value)) if run_value[i] == '_x']
                for i in b:
                    print(tt)
                    PP991[int(run_index[i])-1] = tt[i]
                    print('成功1')
            else:
                for i in range(len(run_value)):
                    PP991[int(run_index[i]) - 1] = int(run_value[i])
    except:
        pass
    PP99 = bytes(PP991)
    sock.send(c)
    time.sleep(0.1)
    print(binascii.b2a_hex(c))

def string_conversion(data):   #字符串转化为字节串
    data_bin = binascii.a2b_hex(data.encode('ascii'))
    return data_bin

def sock_notblock():
    sock.setblocking(False)
    try:
        global buf
        buf = sock.recv(1024)
        print(binascii.b2a_hex(buf))
        if buf[31:33] == b'\x01\x04':
            accept_control()
        elif buf[31:33] == b'\x01\x07':
            configuration_data()
        else:
            pass
    except BlockingIOError:
        pass


def sock_block():     #socket的阻塞
    sock.setblocking(True)

if __name__ == '__main__' :
    global productid,rs1,rs2,rs3,rs4,rs5
    sql = 'select parameter_name, parameter_value, _mode,_type, interface_url, _sign, environment_variable, headers, app_id, parameter_flag ' \
          'from tb_case_independence where case_id = %s' % 2
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
    product_index = _result_name.index('productId')
    productid = _result_value[product_index]
    mac_index = _result_name.index('mac')
    rs3 = _result_value[mac_index]

    sql5 = "select set_control_data from device_data_option where product_id = %s" % productid
    rs5 = connect_sqldb.select_db(sql5)
    rs5 = rs5[0][0]
    sql4 = "select set_run_data from device_data_option where product_id = %s" % productid
    rs4 = connect_sqldb.select_db(sql4)
    rs4 = rs4[0][0]

    # sql3 = "select set_mac from device_data_option where product_id = %s" % productid
    # rs3 = connect_sqldb.select_db(sql3)
    # rs3 = rs3[0][0]

    sql2 = "select device_code from open_device where product_id = %s" % productid
    rs2 = connect_sqldb.select_db(sql2)
    rs2 = rs2[0][0]
    sql1 = "select set_error_data from device_data_option where product_id = %s" % productid
    rs1 = connect_sqldb.select_db(sql1)
    rs1 = rs1[0][0]
    sql = 'select environment_variable from tb_case_independence where case_id = 2'
    _result = connect_sqldb.select_db(sql)
    result = _result[0]
    ev = result[0]

    if ev == 1:
        host = '203.195.139.126'
        port = 9000
    elif ev == 2:
        host = '119.29.112.71'
        port = 9000
    else:
        host = '61.141.158.190'
        port = 9000
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        print(host)
        sock.connect((host, port))
    except socket.error as e:
        print(e)
    run_data = data_frame.device_startdata()
    PP99 = run_data
    n1 = iter(range(0, pow(2, 16)))
    n2 = iter(range(0, pow(2, 16)))
    n3 = iter(range(0, pow(2, 16)))
    n4 = iter(range(0, pow(2, 16)))
    n5 = iter(range(0, pow(2, 16)))
    sock_block()
    encryption()
    sock_notblock()
    sock_block()
    heart_beat()
    sock_notblock()
    sock_block()
    control_data()
    sock_notblock()
    if len(rs1) == 0:
        pass
    else:
        sock_block()
        fault_data()
    sock_notblock()
    while  True:
        sock_block()
        heart_beat()
        sock_notblock()
        sock_block()
        operation_data()
        sock_notblock()

    sock.close()