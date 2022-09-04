import datetime

balance = 1000
account_log = []

def validate(func):
    def wrapper(*args,**kwargs):
        amount =str(args[0])
        index = amount.index(".")
        if len(amount) - index - 1 > 2 :
            print("输入格式有误，小数点后面最多保留2位")
        else:
            func(*args,**kwargs)
    return wrapper

@validate
def deposit(amount):
    """
    存款
    :param amount:存入金额
    :return:noun
    """
    global balance
    balance += amount
    write_log(amount,"存入")

@validate
def withdraw(amount):
    """
    取款
    :param amount: 金额
    :return:
    """
    global balance
    if balance < amount:
        print(f"余额不足")
    else:
        balance-=amount
    write_log(amount,"取出")

def write_log(amount,type):
    """
    写入日志
    :param amount: 金额
    :param type:存入 或者 取出
    :return:Noun
    """
    now = datetime.datetime.now()
    creat_time = now.strftime("%y-%m-%d %H:%M:%S")
    data = [creat_time,type,amount,f"{balance:.2f}"]
    account_log.append(data)

def print_log():
    """
    查看流水
    :return:Noun
    """
    print(account_log)

def show_menu():
    menu = """
操作菜单
0：退出
1：存款
2：取款
3：打印交易信息
    """
    print(menu)

while True:
    show_menu()
    num = int(input("请根据菜单编号输入: "))
    if num == 0:
        print("您已经退出系统")
        break
    elif num == 1:
        print("存款")
        amount = float(input("请输入存款金额："))
        deposit(amount)
        print(f"当前余额{balance:.2f}")
    elif num == 2:
        print ("取款")
        amount = float(input("请输入取款金额："))
        withdraw(amount)
        print(f"当前余额{balance:.2f}")
    elif num == 3:
        print("查看记录")
        print_log()
    else:
        print("输入有误")

