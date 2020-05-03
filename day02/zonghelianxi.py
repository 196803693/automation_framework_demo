memberList = []#存放会员的列表
ziduanDict = {'姓名':'name','电话':'tel','QQ':'QQ','邮箱':'email'}#用户输入汉字时要有对应字段

def show_menue():
    print('***************************************')
    print('欢迎使用[会员管理系统]')
    print()
    print('1.添加会员')
    print('2.显示全部')
    print('3.搜索会员')
    print('4.修改会员')
    print('0.退出系统')

def addmember():
    print('新增会员')
    name = input('请输入姓名: ')
    tel = input('请输入电话: ')
    QQ = input('请输入QQ: ')
    emal = input('请输入邮箱: ')
    memdict = {'name':name,
                'tel':tel,
               'QQ':QQ,
               'emal':emal}
    memberList.append(memdict)
    print(memdict,'\n添加%s的会员成功'%name)
    if input('可输入2继续添加') == '2':
        addmember()

def showall():
    print('显示全部')
    for i in memberList:
        print('姓名: %s   电话:%s   QQ:%s   邮箱:%s'
              %(i['name'],i['tel'],i['QQ'],i['emal']))
    input('输入任意键继续')

def serchmember():
    print('搜索会员')
    sername = input('请输入要搜索的用户名: ')
    for i in memberList:
        if sername == i['name']:
            print('找到该会员')
            print('姓名: %s   电话:%s   QQ:%s   邮箱:%s'
                  % (i['name'], i['tel'], i['QQ'], i['emal']))
    else:
        if input('查找结束,可输入3继续添加') == '3':
            serchmember()

def changeMember():
    print('修改会员')
    cname = input('请输入要修改的用户名')
    for i in memberList:
        if cname == i['name']:
            print('原会员信息是')
            print('姓名: %s   电话:%s   QQ:%s   邮箱:%s'
                  % (i['name'], i['tel'], i['QQ'], i['emal']))
            oldmember = i
            ziduan = input('请输入要修改的字段')
            newinfo = input('请输入要修改的内容')
            i[ziduanDict[ziduan]] = newinfo
            print('修改后')
            print('姓名: %s   电话:%s   QQ:%s   邮箱:%s'
                  % (i['name'], i['tel'], i['QQ'], i['emal']))
    else:
        if input('修改结束,可输入4继续修改') == '4':
            changeMember()


#循环语句,根据用户输入的数字调用不同的函数
while True:
    show_menue()
    print('***************************************')
    opnum = input('请选择希望执行的操作: ')
    print('你选择的操作是', opnum)
    if opnum == '0':
        print('退出系统')
        break
    elif opnum == '1':
        addmember()
    elif opnum == '2':
        showall()
    elif opnum == '3':
        serchmember()
    elif opnum == '4':
        changeMember()
    else:
        input('请输入有效数据')
