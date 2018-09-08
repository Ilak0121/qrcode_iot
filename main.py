import qrscan

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


if __name__ == "__main__":

    option_print()
    option = input("select option>> ")

    if choice == '1':
        qrscan.qr_scanning()

