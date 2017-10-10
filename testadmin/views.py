# coding=utf-8
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,StreamingHttpResponse
from django.contrib import  auth
from django.contrib.auth.decorators import login_required
from forms import LoginForm,UploadFileForm,CreateDatabaseInfoForm,CreateSystemInfoForm,CreateTestCaseForm
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
import os,time
from django.contrib.auth.models import User
from models import DatabaseInfo,SystemInfo,TestCase
from script import erp_purchase
from django.db import connection,transaction

#试验浏览器运行脚本的可行性

def csErpPurchase(request):
    erp_purchase.createPurchases()
    erp_purchase.checkPurchases()
    return HttpResponse("ok")
#登入后进入主界面
@login_required
def index(request):
    username = request.session.get('username','nobody')
    return render(request,'testadmin/index.html',{"username":username})

@login_required
def index_v1(request):
    return render(request,'H/userList.html')

#进入首页用户信息界面
@login_required
def userInfo(request):
    username = request.session.get('username', 'admin')
    user = User.objects.filter(username=username).values()[0]
    info = {}
    info["id"]=user["id"]
    info["name"]=user["username"]
    info["email"]=user["email"]
    info["create_time"]=user["date_joined"]
    info["last_login"]=user["last_login"]
    info["ip"]=request.META.get("REMOTE_ADDR",None)
    return render(request,'testadmin/userinfo.html',{"info":info})

#进入数据库信息界面
@login_required
def databaseInfo(request):
    return render(request,'testadmin/databaseinfo.html')

#进入创建数据库信息界面
@login_required
def createDatabaseInfo(request):

    if request.method == 'POST':
        form = CreateDatabaseInfoForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将数据保存到数据库
            DatabaseInfo(name=request.POST["name"],
                         account=request.POST["account"],
                         password=request.POST["password"],
                         address=request.POST["address"],
                         create_user=request.session.get("username"),
                         modify_user=request.session.get("username")).save()
            # 创建数据库信息成功，跳转回首页
            return HttpResponseRedirect('/testadmin/databaseInfo')
    else:
        form = CreateDatabaseInfoForm()
    return render(request, "testadmin/create_databaseinfo.html",{'form':form,'post':request.POST})

#搜索创建数据库信息
@login_required
def searchDatabaseInfo(request):
    name = request.POST["name"]
    account = request.POST["account"]
    address = request.POST["address"]
    table_info =  DatabaseInfo.objects.values().filter(name__contains=name,account__contains=account,address__contains=address)
    display=True
    return render(request, 'testadmin/databaseinfo.html',{'tableinfos':table_info,'display':display})

#进入系统测试地址信息界面
@login_required
def systemInfo(request):
    databaseInfo_selects = DatabaseInfo.objects.values()
    return render(request,'testadmin/systeminfo.html',{'databaseInfo_selects':databaseInfo_selects})

#进入创建系统测试地址信息界面
@login_required
def createSystemInfo(request):

    if request.method == 'POST':
        #databaseInfo_selects = DatabaseInfo.objects.values().filter(id=request.POST["database_name"])
        form = CreateSystemInfoForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将数据保存到数据库
            SystemInfo(name=request.POST["name"],
                         account=request.POST["account"],
                         password=request.POST["password"],
                         address=request.POST["address"],
                         remark=request.POST["remark"],
                         create_user=request.session.get("username"),
                         modify_user=request.session.get("username")).save()
            database_name = DatabaseInfo.objects.get(name=request.POST["database_name"])
            SystemInfo.objects.get(name=request.POST["name"]).database_name.add(database_name)
            # 创建成功，跳转回首页
            return HttpResponseRedirect('/testadmin/systemInfo')
    else:
        form = CreateDatabaseInfoForm()
    databaseInfo_selects = DatabaseInfo.objects.values()
    return render(request, "testadmin/create_systeminfo.html",{'form':form,'databaseInfo_selects':databaseInfo_selects,'post':request.POST})

#进入修改系统测试地址信息界面
@login_required
def querySystemInfo(request,id):
    cursor = connection.cursor()
    sql = '''select
                        sys.id,
                        sys.name,
                        sys.address,
                        db.name,
                        sys.account,
                        sys.password,
                        sys.remark
                from testadmin_systeminfo as sys
                left join testadmin_systeminfo_database_name as sysdb on sys.id=sysdb.systeminfo_id
                left join testadmin_databaseinfo as db on sysdb.databaseinfo_id=db.id
                where sys.id = "{0}"
                '''.format(id)
    cursor.execute(sql)
    row = cursor.fetchone()
    line = {}
    line["id"] = row[0]
    line["name"] = row[1]
    line["address"] = row[2]
    line["database_name"] = row[3]
    line["account"] = row[4]
    line["password"] = row[5]
    line["remark"] = row[6]
    databaseInfo_selects = DatabaseInfo.objects.values()
    return render(request, 'testadmin/query_systeminfo.html',{'tableinfos': line, 'databaseInfo_selects': databaseInfo_selects})
#修改系统测试地址信息
def modifySystemInfo(request):
    if request.method == 'POST':
        form = CreateSystemInfoForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            cursor = connection.cursor()
            sql_sys = '''update testadmin_systeminfo
            set name = "%s",
            address = "%s",
            account = "%s",
            password = "%s",
            remark = "%s",
            modify_user = "%s"
            where id = "%s"
            '''%(request.POST["name"],request.POST["address"],request.POST["account"],request.POST["password"],request.POST["remark"],request.session.get("username"),request.POST["id"])
            sql_db = '''update testadmin_systeminfo_database_name
                        set databaseinfo_id = (select id from testadmin_databaseinfo where name = "%s")
                        where systeminfo_id = "%s"
                        '''%(request.POST["database_name"],request.POST["id"])
            cursor.execute(sql_db)
            cursor.execute(sql_sys)
            transaction.commit()
            return HttpResponseRedirect('/testadmin/systemInfo')
    else:
        form = CreateDatabaseInfoForm()
    databaseInfo_selects = DatabaseInfo.objects.values()
    return render(request, "testadmin/query_systeminfo.html",{'form':form,'databaseInfo_selects':databaseInfo_selects,'tableinfos':request.POST})

#搜索系统测试地址信息
@login_required
def searchSystemInfo(request):
    name = request.POST["name"].encode("utf-8")
    address = request.POST["address"].encode("utf-8")
    database_id = request.POST["database_name"].encode("utf-8")
    # if database_id=='':
    #     table_info =  SystemInfo.objects.all().filter(name__contains=name,address__contains=address)
    #     if table_info == None:
    #         database_name = table_info[0].database_name.all()[0].name
    #     else:
    #         database_name = ''
    # else:
    #     database_info = DatabaseInfo.objects.get(id=database_id)
    #     table_info = database_info.systeminfo_set.all().filter(name__contains=name, address__contains=address)
    #     if table_info == None:
    #         database_name = table_info[table_info.id-1].database_name.all()[0].name
    #     else:
    #         database_name = ''
    cursor = connection.cursor()
    sql = '''select
                    sys.id,
                    sys.name,
                    sys.address,
                    db.name,
                    sys.account,
                    sys.password,
                    sys.create_user,
                    sys.create_time,
                    sys.remark
            from testadmin_systeminfo as sys
            left join testadmin_systeminfo_database_name as sysdb on sys.id=sysdb.systeminfo_id
            left join testadmin_databaseinfo as db on sysdb.databaseinfo_id=db.id
            where sys.name like "%{0}%" and sys.address like "%{1}%" and db.id like "%{2}%"
        '''.format(name,address,database_id)
    cursor.execute(sql)
    rows = cursor.fetchall()
    table_info = []
    for row in rows:
        line = {}
        line["id"] = row[0]
        line["name"] = row[1]
        line["address"]= row[2]
        line["database_name"]= row[3]
        line["account"]= row[4]
        line["password"]= row[5]
        line["create_user"]= row[6]
        line["create_time"]= row[7]
        line["remark"]= row[8]
        table_info.append(line)
    display=True
    databaseInfo_selects = DatabaseInfo.objects.values()
    return render(request, 'testadmin/systeminfo.html',{'tableinfos':table_info,'display':display,'databaseInfo_selects':databaseInfo_selects})

#进入测试用例信息界面
@login_required
def testCase(request):
    return render(request,'testadmin/testcase.html')

#创建测试用例界面
@login_required
def createTestCase(request):
    if request.method == 'POST':
        form = CreateTestCaseForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将数据保存到数据库
            TestCase(project_name=request.POST["project_name"],
                number=request.POST["number"],
                function_model=request.POST["function_model"],
                title=request.POST["title"],
                precondition=request.POST["precondition"],
                procedure=request.POST["procedure"],
                grade=request.POST["grade"],
                test_result="未测试",
                create_user=request.session.get("username"),
                modify_user=request.session.get("username")).save()
            # 创建成功，跳转回首页
            return HttpResponseRedirect('/testadmin/testCase')
    else:
        form = CreateDatabaseInfoForm()
    return render(request, "testadmin/create_testcase.html",{'form':form,'post':request.POST})
#搜索测试用例
@login_required
def searchTestCase(request):
    project_name = request.POST["project_name"]
    function_model = request.POST["function_model"]
    title = request.POST["title"]
    test_result = request.POST["test_result"]
    grade = request.POST["grade"]
    table_info =  TestCase.objects.values().filter(project_name__contains=project_name,
                                                   function_model__contains=function_model,
                                                   title__contains=title,
                                                   test_result__contains=test_result,
                                                   grade__contains=grade,
                                                   status=1)
    display=True
    return render(request, 'testadmin/testCase.html',{'tableinfos':table_info,'display':display})
#进入测试用例详情页面
@login_required
def queryTestCase(request,id):
    table_info = TestCase.objects.values().filter(id=id)
    return render(request,'testadmin/query_testcase.html',{'post':table_info[0]})
#修改测试用例
@login_required
def modifyTestCase(request):
    form = CreateTestCaseForm(request.POST)
    if form.is_valid():
        TestCase.objects.filter(id=request.POST["id"]).update(project_name=request.POST["project_name"],
                                                              number=request.POST["number"],
                                                              function_model=request.POST["function_model"],
                                                              title=request.POST["title"],
                                                              precondition=request.POST["precondition"],
                                                              procedure=request.POST["procedure"],
                                                              ex_result=request.POST["ex_result"],
                                                              pr_result=request.POST["pr_result"],
                                                              test_result=request.POST["test_result"],
                                                              grade=request.POST["grade"],
                                                              modify_user=request.session.get('username','')
                                                              )

        info = True
    else:
        info = False
    return render(request, "testadmin/query_testcase.html", {'form': form, 'post': request.POST,'info':info})

#删除测试用例
@login_required
def deleteTestCase(request,id):
    TestCase.objects.filter(id=id).update(status=0,modify_user=request.session.get('username',''))
    return HttpResponseRedirect('/testadmin/testCase')

#下载文件功能
@login_required
def testCaseFileDownload(request):
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,"rb") as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
            f.close()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    the_file_name = os.path.join(base_dir,"upload//template//testcase.xls")
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format("testcase.xls")
    return response
#上传文件功能
import xlrd,time
@login_required
def testCaseUpload(request):
    # 按行读取文件中的数据
    def readRowsData(file_path, sheet=0):
        # 打开文件中的sheet
        def openBook(file_path, sheet=0):
            try:
                open_file = openFile(file_path)
                open_sheet = open_file.sheet_by_index(sheet)
            except AttributeError, e:
                print u"打开工作表失败，报错内容为%s" % e
            else:
                return open_sheet
        # 打开excel文档
        def openFile(file_path):
            try:
                open_file = xlrd.open_workbook(file_path)
            except IOError, e:
                print u"打开文件失败，报错内容为%s" % e
            else:
                return open_file
        open_sheet = openBook(file_path)
        rows_data = []
        for i in range(open_sheet.nrows):
          rows_data.append(open_sheet.row_values(i))
        return rows_data
    #往数据库中存储数据
    def writeData(request,file_path):
        project_name = readRowsData(file_path)[0][1]
        for test_case in readRowsData(file_path)[2:]:
            TestCase(project_name=project_name,
                     number=test_case[0],
                     function_model=test_case[1],
                     title=test_case[2],
                     precondition=test_case[3],
                     procedure=test_case[4],
                     ex_result=test_case[5],
                     #pr_result=test_case[6],
                     #test_result=test_case[7],
                     grade=test_case[8],
                     create_user=request.session.get("username"),
                     modify_user=request.session.get("username")).save()

    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            upload_file = request.FILES["uploadfile"]
            if upload_file.name.split('.')[1] == 'xls':
                try:
                    base_dir = os.path.dirname(os.path.abspath(__file__))
                    #注意upload前面不能加//
                    #upload_file.name 读取上传文件的文件名（包括扩展名），
                    #upload_file.read():从文件中读取整个上传的数据，这种方法只适合小文件
                    #upload_file.chunks():按块返回文件，通过在for循环中进行迭代，可以将大文件按块写入到服务器中
                    #upload_file.multiple_chunks():这个方法根据upload_file的大小，返回True或者False,当upload_file文件大于2.5M（默认为2.5M，可以调整）时，返回True，否则返回False
                    #upload_file.size 获取上传文件的大小
                    destination = open(os.path.join(base_dir,"upload\\%s"%upload_file.name),'wb+')
                    if upload_file.multiple_chunks() == False:
                        destination.write(upload_file.read())
                        #print "2.5<"
                    else:
                        for chunk in upload_file.chunks():
                            destination.write(chunk)
                        #print ">2.5"
                    destination.close()
                    writeData(request,os.path.join(base_dir,"upload\\%s"%upload_file.name))
                    return render(request,'testadmin/create_testcase.html',{"info":"上传文件成功"})
                except Exception,e:
                    print "%s"%e
                    return render(request,'testadmin/create_testcase.html',{"info":"上传文件失败，请重新上传"})
            else:
                return render(request,'testadmin/create_testcase.html',{"info":"请上传(.xls)文件"})
        else:
            return render(request,'testadmin/create_testcase.html',{"info":"请上传文件"})
    else:
        return HttpResponseRedirect('/testadmin/createTestCase')


def interfaceTest(file_path, sheet=0):
    rows_data = readRowsData(file_path, sheet)
    i = 1
    for cases in rows_data:
        # 获取URL
        url = cases[2] + cases[3]

    # 按行读取文件中的数据
    def readRowsData(file_path, sheet=0):
        open_sheet = openBook(file_path, sheet)
        rows_data = []
        for i in range(open_sheet.nrows):
            if i != 0:
                rows_data.append(open_sheet.row_values(i))
        return rows_data

    # 打开文件中的sheet
    def openBook(file_path, sheet=0):
        try:
            open_file = openFile(file_path)
            open_sheet = open_file.sheet_by_index(sheet)
        except AttributeError, e:
            print u"打开工作表失败，报错内容为%s" % e
        else:
            return open_sheet

    # 打开excel文档
    def openFile(file_path):
        try:
            open_file = xlrd.open_workbook(file_path)
        except IOError, e:
            print u"打开文件失败，报错内容为%s" % e
        else:
            return open_file



def test_case_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        print form.is_valid()
        if form.is_valid():
            upload_file = request.FILES["uploadfile"]
            try:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                #注意upload前面不能加//
                #upload_file.name 读取上传文件的文件名（包括扩展名），
                #upload_file.read():从文件中读取整个上传的数据，这种方法只适合小文件
                #upload_file.chunks():按块返回文件，通过在for循环中进行迭代，可以将大文件按块写入到服务器中
                #upload_file.multiple_chunks():这个方法根据upload_file的大小，返回True或者False,当upload_file文件大于2.5M（默认为2.5M，可以调整）时，返回True，否则返回False
                #upload_file.size 获取上传文件的大小
                destination = open(os.path.join(base_dir,"upload//%s"%upload_file.name),'wb+')                          
                if upload_file.multiple_chunks() == False:
                    destination.write(upload_file.read())
                    print "2.5<"
                else:
                    for chunk in upload_file.chunks():
                        destination.write(chunk)
                    print ">2.5"
                destination.close()
                return render(request,'H/userList.html',{"info":"上传文件成功"})
            except Exception,e:
                print "%s"%e
                return render(request,'H/userList.html',{"info":"上传文件失败，请重新上传"})
        else:
            return render(request,'H/userList.html',{"info":"请上传文件"})
    else:
        return HttpResponseRedirect('/H/index_v1')

 #登入功能
def logins(request):
    # 只有当请求为 POST 时，才表示用户提交了登入信息
    if request.method == 'POST':
        # 验证数据的合法性
        form=LoginForm(request.POST)
        if form.is_valid():
            # 如果提交用户名和密码
            usrname=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=usrname,password=password)
            if user is not None and user.is_active:
                print user
                auth.login(request,user)
                request.session['username'] = usrname
                return HttpResponseRedirect('/testadmin/index')

            else:
                return render(request,'testadmin/login.html',{"info":"用户名或密码错误"})
        else:
            return render(request, 'testadmin/login.html',{"info":"用户名和密码不能为空"})

    else:
        return render(request,'testadmin/login.html')
#退出功能
@login_required
def logouts(request):
    auth.logout(request)
    return HttpResponseRedirect('/testadmin/login')

