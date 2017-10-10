# coding:utf-8
from selenium import webdriver
import time,os,random,sys,logging,MySQLdb

#logging.basicConfig(level=logging.DEBUG)

base_url="http://192.168.8.44:8085"

def queryData(sql):
    db=MySQLdb.connect("192.168.8.51","root","EC52F^71107$7d4","newerp",charset="utf8")
    cursor=db.cursor()
    #sql="select sku from yks_stock where quantity>10 order by quantity asc limit 1000"
    cursor.execute(sql)
    read=cursor.fetchall()
    return read
def updateData(sql):
    db=MySQLdb.connect("192.168.8.51","root","EC52F^71107$7d4","haitun_v2",charset="utf8")
    cursor=db.cursor()
    #sql="select sku from yks_stock where quantity>10 order by quantity asc limit 1000"
    try:
       # 执行sql语句
       cursor.execute(sql)
       # 提交到数据库执行
       db.commit()
    except:
       # Rollback in case there is any error
       db.rollback()

        # 关闭数据库连接
    db.close()
    

def chromeDriver():
    return webdriver.Chrome()
    
def login(driver,name,password):
    driver.get(base_url)
    driver.find_element_by_name("name").clear()
    driver.find_element_by_name("name").send_keys(name)
    driver.find_element_by_name("password").clear()
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_name("login").click()

def purchases(driver,warehouse,sku):
    driver.get(base_url+"/purchase/index")
    driver.find_element_by_id("supplier_name").send_keys("HUX Wind GmbH")
    time.sleep(1)
    driver.find_element_by_xpath(".//a[contains(.,'HUX Wind GmbH')]").click()
    driver.find_element_by_xpath(".//*[@id='company_id']/option[contains(.,'海豚跨境科技（香港）有限公司')]").click()
    driver.find_element_by_id("6.8750").click()
    driver.find_element_by_xpath(".//*[@id='warehouse_id']/option[contains(.,'%s')]"%warehouse).click()
    driver.find_element_by_xpath(".//*[@id='1']/td[2]/input").send_keys(sku)
    driver.find_element_by_xpath(".//*[@id='1']/td[7]/input").send_keys("10")
    driver.find_element_by_xpath(".//*[@id='1']/td[8]/input").send_keys("100")
    driver.find_element_by_id("add_plan").click()
    driver.find_element_by_xpath(".//*[@id='purchase-delivery-plans']/tr[1]/td[8]/input").send_keys("2017/09/29")
    driver.find_element_by_id("tijiao").click()

def checkPurchase(driver,purchases_id):
    driver.get(base_url+"/purchases/selectpurchase/singledetail?p_id=%d"%purchases_id)
    driver.find_element_by_id("pass_check").click()
    time.sleep(2)
    driver.switch_to_alert().accept()
    driver.find_element_by_id("finance_pass_check").click()
    time.sleep(2)
    driver.switch_to_alert().accept()
    
    
def createPurchases():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    
    login(driver,"admin","admin321")
    sql="SELECT `name` FROM warehouses WHERE international=0 AND company_id=1 AND isuse=1"
    warehouse=queryData(sql)
    sku=["DEAP005"]
    for i in warehouse:
        purchases(driver,i,sku[0])
    driver.close()
def checkPurchases():
    driver=webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window() 
    login(driver,"test_m","admin321")
    sql="SELECT id FROM purchaseorders WHERE `status`=10 ORDER BY id DESC LIMIT 10"
    purchases_id=queryData(sql)
    for i in purchases_id:
        try:
            checkPurchase(driver,i)
        except:
            print "已审核"
    driver.close()
            
    
if __name__=="__main__":
    #createPurchases()
    checkPurchases()