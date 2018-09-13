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
    print("----------------------------------------------")
    print("---this is the qr code scanning IOT program---")
    print("----------------------------------------------")
    print("| 0.To exist this Program                    |")
    print("| 1.Start the scanning                       |")
    print("| 2.List of stocks                           |")
    print("| 3.Adjust the quantity                      |")
    print("| 4.Options of recipe                        |")
    print("-------------still developing-----------------")
    print("----------------------------------------------")
    print("| 5.check the nutrition balance of owner     |")
    print("| 6.Possible Recipes                         |")
    print("----------------------------------------------")

def sql_initing(): 
    #initializing of auto increment
    #this function must be execute after delete of sql.
    sql = "alter table qr_data auto_increment =1;"
    curs.execute(sql)
    conn.commit()

def sql_update():
    os.system('clear')
    sql_list()
    print("\n-----------------------------------------------------------")
    try:
        index = input("input index want to change >> ")
        col = input("input name want to change >> ")
        data = input("value want to change >> ")
        sql = "update qr_data set {} = {} where id={};".format(col,data,index)
        curs.execute(sql)
    except:
        print("wrong input name... exiting...")
        exit()
    else:
        conn.commit()

def sql_delete(index):
    sql = "delete from qr_data where id={};".format(index)
    curs.execute(sql)
    option = input("Are you sure?<Y/n>:")
    if option == 'n' or option == 'N':
        conn.commit()

    sql_initing()

    

def sql_list():
    os.system('clear')
    sql="select {},{},{},{},{},{} from qr_data;".format('id','Name','Date_limit','Date_enter','Company','Weight')
    #sql="select * from qr_data;"
    curs.execute(sql)

    #Data Fetch
    rows = curs.fetchall()
    rows = list(rows)
    print("\n-----------------------------------------------------------")
    print("-----------list of stocks in refrigerator------------------")
    print("-----------------------------------------------------------")
    print("|format: index| Name / Date_limit / Date_enter / Company / Weight|")
    print("-----------------------------------------------------------")
    for row in rows:
        line = " | "
        for i in range(len(row)):
            if str(row[i]) == 'None':
                line = line + "    " + "/ " 
            elif i is len(row)-1 :
                line = line + str(row[i])
            elif i is 0:
                line = str(row[i])+line
            else:
                line = line + str(row[i])+"/ "

        print(line)

def main_process(option):
    if option == '1':
        qrscan.qr_scanning()#find qr_code and insert data to db
    elif option == '2': #show the lists
        sql_list()
    elif option == '3': #adjust the quantity
        sql_update()
    elif option == '4':
        sql_initing()
    elif option == '11':
        index = input("index>>")
        sql_delete(index)
    else:
        print("[INFO] program exiting...")
        return 1
    return 0

if __name__ == "__main__":
    #connecting to mysql
    passwd = readpasswd()
    conn = pymysql.connect(host='localhost',user=passwd[0][:-1],password=passwd[1][:-1],db='qr_data',charset='utf8')
    curs = conn.cursor()

    while True:
        os.system('clear')
        option_print()
        option = input("select option('Enter' to close)>> ")
        result = main_process(option)    
        if result == 1:
            break
        input()

    conn.close()
