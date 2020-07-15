 ###系统需求
#  1.程序启动，显示名片管理系统欢迎界面，并显示功能菜单
#  ************************************************
#  欢迎使用[名片管理系统] V1.0
# 1.新建名片
# 2.显示全部
# 3.查询名片
# 0.退出系统
# ***0**<*<*****<***********
# ●2. 用户用数字选择不同的功能
# ●3.根据功能选择，执行不同的功能
# ●4.用户名片需要记录用户的姓名、电话、QQ、邮件
# ●5.如果查询到指定的名片，用户可以选择修改或者删除名片###
import cards_tools
while True:
    # TODO 显示功能菜单
    cards_tools.show_menu()
    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是{}".format(action_str))


     # 1,2,3针对名片操作
    if action_str in ["1","2","3"]:
    # 1.新建名片
        if action_str == "1":
            cards_tools.new_card()
    # 2.显示全部
        elif action_str == "2":
            cards_tools.show_all()
    # 3.查询名片
        elif action_str == "3":
            cards_tools.search_card()


     # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用本系统")
        break
     # 其他内容输入错误，提醒用户
    else:
        print("您输入的不正确，请重新选择")


