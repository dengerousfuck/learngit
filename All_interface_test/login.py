import requests
from datetime import datetime
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import json
from selenium.webdriver.common.action_chains import ActionChains
from company.All_interface_test import connect_sqldb
import time
from selenium import webdriver
def protocol():
    driver.find_element_by_xpath("//*[@id = 'page']/div/div/div[2]/div/div[3]/ul/li/a/span").click()
    time.sleep(3)
    s0 = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li")  #[2]/span
    lenth = len(s0)
    control_protocol = []
    for i in range(1,lenth):
        s = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li[%s]/span"%i)
        s1 = str(s[1].get_attribute('title'))
        s2 = str(s[2].get_attribute('title'))
        s3 = str(s[3].text)
        s4 = str(s[4].text)
        s5 = str(s[5].text)
        s6 = str(s[6].get_attribute('title'))
        name1 = [s1,s2,s3,s4,s5,s6]
        name1 = '|'.join(name1)
        control_protocol.append(name1)
        print(control_protocol)
    s = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul[2]/li/span")
    s1 = str(s[1].get_attribute('title'))
    s2 = str(s[2].get_attribute('title'))
    s3 = str(s[3].text)
    s4 = str(s[4].text)
    s5 = str(s[5].text)
    s6 = str(s[6].get_attribute('title'))
    name1 = [s1,s2,s3,s4,s5,s6]
    name1 = '|'.join(name1)
    control_protocol.append(name1)
    print(control_protocol)
    driver.find_element_by_xpath("//*[@class='protocolpage comm-cntnt']/div/ul/li[2]").click()
    time.sleep(3)

    ss0 = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li")
    lenth = len(ss0)
    run_protocol = []
    print(lenth)
    for i in range(1,lenth+1):
        ss = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li[%s]/span"%i)
        s1 = str(ss[1].get_attribute('title'))
        s2 = str(ss[2].get_attribute('title'))
        s3 = str(ss[3].text)
        s4 = str(ss[4].text)
        s5 = str(ss[5].text)
        s6 = str(ss[6].get_attribute('title'))
        name1 = [s1,s2,s3,s4,s5,s6]
        name1 = '|'.join(name1)
        run_protocol.append(name1)
        print(run_protocol)
        print(len(run_protocol))
    print('成功运行数据')


    driver.find_element_by_xpath("//*[@class='protocolpage comm-cntnt']/div/ul/li[3]").click()
    time.sleep(3)
    sss0 = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li")
    lenth = len(sss0)
    error_protocol = []
    for i in range(1,lenth+1):
        ss = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li[%s]/span"%i)
        s1 = str(ss[1].get_attribute('title'))
        s2 = str(ss[2].get_attribute('title'))
        s3 = str(ss[3].text)
        s4 = str(ss[4].text)
        s5 = str(ss[5].text)
        s6 = str(ss[6].get_attribute('title'))
        name1 = [s1,s2,s3,s4,s5,s6]
        name1 = '|'.join(name1)
        error_protocol.append(name1)
        print(error_protocol)
        print(len(error_protocol))
    print('故障数据成功')

    driver.find_element_by_xpath("//*[@class='protocolpage comm-cntnt']/div/ul/li[4]").click()
    time.sleep(3)
    ssss0 = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li")
    lenth = len(ssss0)
    print(lenth)
    configuration_protocol = []
    for i in range(1,lenth+1):
        ss = driver.find_elements_by_xpath("//*[@class='tc protocoltable']/div[2]/ul/li[%s]/span"%i)
        s1 = str(ss[1].get_attribute('title'))
        s2 = str(ss[2].get_attribute('title'))
        s3 = str(ss[3].text)
        s4 = str(ss[4].text)
        s5 = str(ss[5].text)
        s6 = str(ss[6].get_attribute('title'))
        name1 = [s1,s2,s3,s4,s5,s6]
        name1 = '|'.join(name1)
        configuration_protocol.append(name1)
        print(configuration_protocol)
        print(len(configuration_protocol))
    print('配置数据成功')
    driver.find_element_by_xpath("//*[@class = 'login-in']/div[2]/div/div[2]/ul/li/a/span").click()
    time.sleep(3)
    product_id = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p/span[2]").text
    device_code = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[4]/span[2]").text
    print(product_id)

    control_data = []
    run_data = []
    error_data = []
    configuration_data = []
    control_lenth = []
    run_lenth = []
    error_lenth = []
    configuration_lenth = []
    control_data_name = []
    control_value_options = []
    run_data_name = []
    run_value_options = []
    error_data_name = []
    error_value_options = []
    configuration_data_name = []
    configuration_value_options = []
    for i in control_protocol:
        j = i.split("|")
        control = j[1]
        _control_lenth = int(j[4])
        _data_name = j[0]
        _value_options = j[5]
        control_data_name.append(_data_name)
        control_value_options.append(_value_options)
        control_lenth.append(_control_lenth)
        control_data.append(control)
    control_data = str(control_data).strip('[]')
    print(control_data)
    print(control_lenth)
    control_count = sum(control_lenth)

    for i in run_protocol:
        j = i.split("|")
        _run_data_name = j[0]
        _run_value_options = j[5]
        run = j[1]
        _run_lenth = int(j[4])
        run_data_name.append(_run_data_name)
        run_value_options.append(_run_value_options)
        run_lenth.append(_run_lenth)
        run_data.append(run)
    run_data = str(run_data).strip('[]')
    print(run_data)
    print(run_lenth)
    run_count = sum(run_lenth)
    for i in error_protocol:
        j = i.split("|")
        error = j[1]
        _error_data_name = j[0]
        _error_value_options = j[5]
        _error_lenth = int(j[4])
        error_data_name.append(_error_data_name)
        error_value_options.append(_error_value_options)
        error_lenth.append(_error_lenth)
        error_data.append(error)
    error_data = str(error_data).strip('[]')
    print(error_data)
    print(error_lenth)
    error_count = sum(error_lenth)
    for i in configuration_protocol:
        j = i.split("|")
        configuration = j[1]
        _configuration_data_name = j[0]
        _configuration_value_options = j[5]
        _configuration_lenth = int(j[4])
        configuration_data_name.append(_configuration_data_name)
        configuration_value_options.append(_configuration_value_options)
        configuration_lenth.append(_configuration_lenth)
        configuration_data.append(configuration)
    configuration_data = str(configuration_data).strip('[]')
    print(configuration_data)
    print(configuration_lenth)
    configuration_count = sum(configuration_lenth)
    control_data_name = str(control_data_name).strip('[]')
    control_value_options = str(control_value_options).strip('[]')
    run_data_name = str(run_data_name).strip('[]')
    run_value_options = str(run_value_options).strip('[]')
    error_data_name = str(error_data_name).strip('[]')
    error_value_options = str(error_value_options).strip('[]')
    configuration_data_name = str(configuration_data_name).strip('[]')
    configuration_value_options = str(configuration_value_options).strip('[]')


    __sql = 'select * from  device_data_option where product_id = %s'%product_id
    __rs = connect_sqldb.select_db(__sql)

    _set_control_data = []
    for i in range(control_count*2):
        _set_control_data.append('0')

    set_control_data = ''
    for i in _set_control_data:
        set_control_data += i
    print(set_control_data)

    _set_run_data = []
    for i in range(run_count*2):
        _set_run_data.append('0')

    set_run_data = ''
    for i in _set_run_data:
        set_run_data += i
    print(set_run_data)

    _set_error_data = []
    for i in range(error_count*2):
        _set_error_data.append('0')

    set_error_data = ''
    for i in _set_error_data:
        set_error_data += i
    print(set_error_data)

    _set_configuration_data = []
    for i in range(configuration_count*2):
        _set_configuration_data.append('0')

    set_configuration_data = ''
    for i in _set_configuration_data:
        set_configuration_data += i
    print(set_configuration_data)

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
    mac_index = _result_name.index('mac')
    mac = _result_value[mac_index]
    if len(__rs) == 0:
        connect_sqldb.insert_into("device_data_option",product_id,product_name,control_data_name,control_value_options,run_data_name,
                                  run_value_options,error_data_name,error_value_options,configuration_data_name,configuration_value_options,
                                  set_control_data,set_run_data,set_error_data,set_configuration_data,'create_time',mac,'','','')
    else:
        sql = "delete from device_data_option where product_id = %s" % product_id
        connect_sqldb.delete_db(sql)
        connect_sqldb.insert_into("device_data_option", product_id, product_name, control_data_name,
                                  control_value_options, run_data_name,
                                  run_value_options, error_data_name, error_value_options, configuration_data_name,
                                  configuration_value_options,
                                  set_control_data,set_run_data, set_error_data, set_configuration_data, 'create_time',mac,'','','')
    _sql = "select * from device_start_data where product_id = %s" % product_id
    _rs = connect_sqldb.select_db(_sql)
    if len(_rs) == 0:
        connect_sqldb.insert_into("device_start_data",product_id,control_data,run_data,error_data,configuration_data,
                                  'create_time',device_code,control_count,run_count,error_count,configuration_count)
    else:
        sql = "delete from device_start_data where product_id = %s" % product_id
        connect_sqldb.delete_db(sql)
        connect_sqldb.insert_into("device_start_data", product_id, control_data, run_data, error_data,
                                  configuration_data,
                                  'create_time', device_code, control_count, run_count, error_count,
                                  configuration_count)
    time.sleep(0.1)
    dict_key = re.findall(r"'(.*?)'", configuration_data)
    if 'Reserved' in dict_key:
        dict_key.pop(-1)
    dict_value = []
    for i in range(len(dict_key)):
        dict_value.append(0)
    __json = dict(map(lambda x, y: [x, y], dict_key, dict_value))
    __json = json.dumps(__json)
    _sqlsql = "select * from conf_device_json where product_id = %s" % product_id
    rsrs = connect_sqldb.select_db(_sqlsql)
    if len(rsrs) == 0:
        connect_sqldb.insert_into("conf_device_json", product_id, __json, 'create_time',product_name)
    else:
        sql = "delete from conf_device_json where product_id = %s" % product_id
        connect_sqldb.delete_db(sql)
        connect_sqldb.insert_into("conf_device_json", product_id, __json, 'create_time',product_name)

    time.sleep(0.1)
    _dict_key = re.findall(r"'(.*?)'",control_data)
    _dict_key.pop(-2)
    _dict_value = []
    for i in range(len(_dict_key)-1):
        _dict_value.append(0)
    _count = control_count //8
    upflg = '00' * _count
    _dict_value.append(upflg)
    _json = dict(map(lambda x,y:[x,y],_dict_key,_dict_value))
    _json = json.dumps(_json)
    sqlsql = "select * from device_json where product_id = %s"%product_id
    rsrs = connect_sqldb.select_db(sqlsql)
    if len(rsrs) == 0:
        connect_sqldb.insert_into("device_json",product_id,_json,'create_time',product_name)
    else:
        sql = "delete from device_json where product_id = %s" % product_id
        connect_sqldb.delete_db(sql)
        connect_sqldb.insert_into("device_json", product_id, _json, 'create_time',product_name)

    sql = "select * from open_protocol where product_id = %s" % product_id
    rs = connect_sqldb.select_db(sql)
    control_protocol = str(control_protocol).strip('[]')
    run_protocol = str(run_protocol).strip('[]')
    error_protocol = str(error_protocol).strip('[]')
    configuration_protocol = str(configuration_protocol).strip('[]')
    if len(rs) == 0:
        connect_sqldb.insert_into('open_protocol', product_id, control_protocol, run_protocol, error_protocol,
                                  configuration_protocol)
    else:
        sql = "delete from open_protocol where product_id = %s" % product_id
        connect_sqldb.delete_db(sql)
        connect_sqldb.insert_into('open_protocol', product_id, control_protocol, run_protocol, error_protocol,
                                  configuration_protocol)
    time.sleep(2)


def product_info():
    print('进入产品详细页面内')
    try:
        driver.find_element_by_xpath("//*[@class = 'login-in']/div[2]/div/div[2]/ul/li/a/span").click() #点击产品资料
        time.sleep(3)
        product_id = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p/span[2]").text  #单个产品的产品ID
        print(product_id)
        size_class = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[2]/span[2]").text  #大小分类
        print(size_class)
        _device_key = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[3]/a")
        _device_key = _device_key.get_attribute('class')
        print(_device_key)
        if _device_key == 'comm-eyeshowhide hide':
            device_key = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[3]/span[2]").text
        else:
            driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[3]/a").click()
            time.sleep(3)
            device_key = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[3]/span[2]").text
        print(device_key)
        device_code = driver.find_element_by_xpath("//*[@id='updateProForm']/div[3]/p[4]/span[2]").text
        print(device_code)

        driver.find_element_by_class_name('active').click()
        print('已点击产品接入')
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id = 'page']/div/div/div[2]/div/div[2]/ul/li/a/span").click()
        print('已点击应用管理')
        time.sleep(3)
        try:

            driver.find_element_by_xpath("//*[@class='comm-tablelist appmanagelist']/tbody/tr/td[6]/a").click() #点进查看
            time.sleep(3)
            appid = driver.find_element_by_xpath("//*[@class = 'base_info comm-cntnt']/div/ul/li[4]/p").text
            ap = driver.find_element_by_xpath("//*[@class = 'base_info comm-cntnt']/div/ul/li[5]/a")
            ap = ap.get_attribute('class')
            print(appid)
            print(ap)
            if ap == 'comm-eyeshowhide hide':
                appsecret = driver.find_element_by_xpath("//*[@class = 'base_info comm-cntnt']/div/ul/li[5]/p").text
            else:
                driver.find_element_by_xpath("//*[@class = 'base_info comm-cntnt']/div/ul/li[5]/a").click()
                time.sleep(2)
                appsecret = driver.find_element_by_xpath("//*[@class = 'base_info comm-cntnt']/div/ul/li[5]/p").text
            print(appid)
            print(appsecret)
        except:
            print('没有产品')
            appsecret = ''
            appid  = ''
        sql = "select * from open_device where product_id = %s" % product_id
        rs = connect_sqldb.select_db(sql)
        if len(rs) == 0:
            connect_sqldb.insert_into('open_device',product_id,size_class,device_key,device_code,appid,appsecret)
        else:
            sql = "delete from open_device where product_id = %s"%product_id
            connect_sqldb.delete_db(sql)
            connect_sqldb.insert_into('open_device', product_id, size_class, device_key, device_code, appid, appsecret)

    except:
        print('没有应用管理2')
    driver.find_element_by_class_name('active').click()
    time.sleep(3)

def main(a,b):
    global driver, control_protocol, run_protocol, error_protocol, configuration_protocol,product_name
    driver = webdriver.PhantomJS(executable_path='E:\python所有项目\company\\venv\\phantomjs')
    #driver = webdriver.Firefox() #Firefox()    Chrome()
    ev_sql = "select _url from open_clife where environment = %d"%a
    sql = "select _name,_password from customization where id = %d"%b
    _rs = connect_sqldb.select_db(ev_sql)
    _rs = _rs[0][0]
    driver.get(_rs)
    rs = connect_sqldb.select_db(sql)
    user = rs[0][0]
    ps = rs [0][1]
    time.sleep(3)
    username =driver.find_element_by_css_selector("input[type = 'text']")
    username.clear()
    username.send_keys(user)
    password =driver.find_element_by_css_selector("input[type = 'password']")
    password.clear()
    password.send_keys(ps)
    driver.find_element_by_link_text("登录").click()
    print('登录成功')
    time.sleep(3)
    driver.find_element_by_class_name('active').click()
    time.sleep(3)
    print('已点击产品接入....')
    product_num = driver.find_elements_by_xpath("//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li")
    product_num = len(product_num)
    for i in range(1,product_num+1):
        _product_name = driver.find_element_by_xpath("//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li[%d]/div/div/p[2]"%i)
        print(_product_name.text)
        product_name = _product_name.text
        chain = ActionChains(driver)
        chain.move_to_element(_product_name).perform()
        driver.find_element_by_xpath("//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li[%d]/div/div[2]/a"%i).click()
        time.sleep(3)
        protocol()
        product_info()
def see_device(a,b,acount,mac,pro):
    #driver = webdriver.PhantomJS(executable_path='E:\python所有项目\company\\venv\\phantomjs')
    driver = webdriver.Firefox()  # Firefox()    Chrome()
    #driver.set_window_size(1280,800)
    time.sleep(3)
    ev_sql = "select _url from open_clife where environment = %d" % a
    sql = "select _name,_password from customization where id = %d" % b
    _rs = connect_sqldb.select_db(ev_sql)
    _rs = _rs[0][0]
    driver.get(_rs)
    rs = connect_sqldb.select_db(sql)
    user = rs[0][0]
    ps = rs[0][1]
    time.sleep(1)
    username = driver.find_element_by_css_selector("input[type = 'text']")
    username.clear()
    username.send_keys(user)
    password = driver.find_element_by_css_selector("input[type = 'password']")
    password.clear()
    password.send_keys(ps)
    driver.find_element_by_link_text("登录").click()
    print('登录成功')
    time.sleep(3)
    driver.find_element_by_class_name('active').click()
    time.sleep(3)
    print('已点击产品接入....')
    product_num = driver.find_elements_by_xpath("//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li")
    product_num = len(product_num)
    print(product_num)
    for i in range(1, product_num + 1):
        _product_name = driver.find_element_by_xpath(
            "//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li[%d]/div/div/p[2]" % i)
        sw = driver.find_element_by_xpath(
            "//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li[%d]/div/div[2]/a" % i)
        sw = sw.get_attribute('href')[len(sw.get_attribute('href'))-4:]
        print(sw)
        if sw == pro:
            driver.execute_script("arguments[0].scrollIntoView();", _product_name)
            time.sleep(1)
            chain = ActionChains(driver)
            chain.move_to_element(_product_name).perform()
            driver.find_element_by_xpath(
                "//*[@id = 'page']/div/div/div[2]/div[2]/div/div/div[2]/ul/li[%d]/div/div[2]/a" % i).click()
            time.sleep(3)
            driver.find_element_by_xpath("//*[@id = 'page']/div/div/div[2]/div/div[5]/ul/li/a/span").click()
            time.sleep(3)
            acounts = driver.find_elements_by_xpath("//*[@class = 'comm-cntnt']/div/div[2]/div/div/input")
            temp = driver.find_elements_by_xpath("//*[@class = 'comm-cntnt']/div[2]/div[2]/div/div/input")
            print(len(acounts))
            print(len(temp))

            acounts = len(acounts) -len(temp)
            jj = []
            for i in range(1,acounts+1):
                j = driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div/div[2]/div/div[%d]/input"%i)
                jj.append(j.get_attribute("title"))

            if acount in jj:
                pass
            else:
                driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div/div/div/a").click()
                time.sleep(0.5)
                driver.find_element_by_xpath("//*[@class = 'addDebugAccountSingle']/input").send_keys(acount)
                driver.find_element_by_xpath("//*[@class = 'addDebugAccountSingle']/a").click()
                time.sleep(3)
            print(jj)
            jjj = []

            _acounts = driver.find_elements_by_xpath("//*[@class = 'comm-cntnt']/div[2]/div[2]/div/div")
            _acounts = len(_acounts)
            for i in range(1,_acounts+1):
                j = driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[2]/div[2]/div/div[%d]/input" % i)
                jjj.append(j.get_attribute("title"))
            print(jjj)

            if mac in jjj:
                s = driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a")
                print(s.get_attribute("class"))
                time.sleep(5)
                try:
                    driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a").click()
                except:
                    driver.refresh()
                    time.sleep(2)
                    driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a").click()

            else:
                driver.find_element_by_xpath("//*[@class = 'debugFacility']/div/div/a").click()
                time.sleep(2)
                driver.find_element_by_xpath("//*[@class = 'addDebugFacilitySingle']/input").send_keys(mac)
                driver.find_element_by_xpath("//*[@class = 'addDebugFacilitySingle']/a").click()
                time.sleep(5)
                s = driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a")
                print(s.get_attribute("class"))
                try:
                    driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a").click()
                except:
                    driver.refresh()
                    time.sleep(2)
                    driver.find_element_by_xpath("//*[@class = 'comm-cntnt']/div[4]/div/div/a").click()
            time.sleep(5)
            print('完成')
            driver.find_element_by_css_selector("input[type = 'text']").send_keys(mac)
            time.sleep(1)
            driver.find_element_by_id("isFilter").click()
            time.sleep(500)

if __name__ == '__main__':
    a,b ,acount,device_mac,pro = 1,1,'13883989549','C00000000019','2347'
    #see_device(a, b, acount, device_mac, pro)
    main(a,b)

    # for i in range(1,9):
    #     main(1,i)
    # driver.quit()

