import qrscan
import pymysql
import os
import sys

def readpasswd():
    f = open("./pass.txt",'r')
    passwd = f.readlines()
    f.close()
    return passwd

def option_print():
    print("---this is the qr code scanning IOT program---")
    print("----------------------------------------------")
    print("| 0.To exist this Program                    |")
    print("| 1.Start the scanning                       |")
    print("| 2.List of stocks                           |")
    print("| 3.Adjust the quantity                      |")
    print("-------------still developing-----------------")
    print("| 4.Options of recipe                        |")
    print("| 5.check the balance of user                |")
    print("----------------------------------------------")

def initializing():


def sql_test():
    #sql="select {},{},{},{} from qr_data;".format('Id','Name','Date_limit','Weight')
    sql="select * from qr_data;"
    curs.execute(sql)

    #Data Fetch
    rows = curs.fetchall()
    for row in rows:
        print(row)
    conn.close()

def sql_insert(name, date_limit, weight, company=None):

    sql =  "insert into qr_data(Name, Date_limit,Weight,Company) values(%s,%s,%s,%s)"
    curs.execute(sql,(name,date_limit,weight,company))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #connecting to mysql
    passwd = readpasswd()

    conn = pymysql.connect(host='localhost',user=passwd[0][:-1],password=passwd[1][:-1],db='qr_data',charset='utf8')
    curs = conn.cursor()
    
    os.system('clear')
    option_print()
    option = input("select option>> ")

    if option == '1':
        qrscan.qr_scanning()
    elif option == '2':
        sql_test()
    elif option == '3':
        sql_insert("chocopi","2019-09-09",14)
    else:
        exit()
