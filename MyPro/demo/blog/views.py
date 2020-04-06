from django.shortcuts import render, HttpResponse
from django.urls import reverse

# Create your views here.
# render 可以返回html文件，HttpResponse只返回字符串


def timer(request):
    import time
    ctime = time.time()
    print("method", request.method)
    print(request.path)
    print(request.get_full_path())
    return render(request, 'timer.html', {'ctime': ctime})  # 模板语法 可放入任何变量 模板文件


def index(request):
    """
    模板语法：
    变量: {{ }}-渲染变量
        1.深度查询  句点符
        2.过滤器
    标签: {% %}-渲染标签
        1.url
        2.css
    """
    i = 10
    l = [111, 222, 333]
    info = {"name": "DL", "age": 22}
    b = True

    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
    alex = Person("alex", 22)
    yolanda = Person("yolanda", 22)
    user = alex
    person_list = [alex, yolanda]
    # 过滤器
    import datetime
    now = datetime.datetime.now()
    person = []
    file_size = 1234567890
    string = "1564 51618 9412 6+156 489 49+616 515 64+62 6+16 516+ 526+ 265 9+5 26+2"
    link = "<a href="">click</a>"

    return render(request, "index.html", locals())


def special_case_2003(request):
    url = reverse("blog:vsc_2003")
    print(url)
    return HttpResponse("special_case_2003")


def year_archive(request, year):

    return HttpResponse(year)


def month_archive(request, year, month):
    print(type(year))
    url = reverse("blog:y_m", args=(year, month))  # 反向解析
    print(url)
    return HttpResponse(year + "-" + month)


def article_detail(request, y, m, d):

    return HttpResponse(y + "-" + m + "-" + d)


def login(request):
    url = reverse("blog:Log")
    print(url)
    if request.method == "GET":
        return render(request, "login.html", {"username": "用户名", "password": "密码"})  # 模板语法 可放入任何变量
    else:
        print(request.GET)
        print(request.POST)
        user = request.POST.get("user")
        password = request.POST.get("password")
        if user == "123" and password == "123":
            return HttpResponse("登录成功")
        else:
            return HttpResponse("用户名或者密码错误")


def path_year(request, y, m):
    z = y + m
    print(z)
    return HttpResponse(z)


def path_month(request, month):
    print(month, type(month))
    return HttpResponse("path_month")


def orders(request):

    return render(request, "orders.html")


from dlog.models import Book


def tables(request):
    # ==============================================创建表 ==============================================#
    # 在models里创建表 然后使用
    # ==============================================添加表记录===================================================

    # 方式一 实例化对象，进行插入
    # book_obj = Book(id=1, title="python红宝书", price=100, pub_data="2012-12-12", publish="人们出版社")
    # book_obj.save()

    # 方式二 create 返回值为创建的对象Book.object 可以实例化Book类
    # book_obj = Book.objects.create(title="PHP", price=100, pub_data="2013-12-12", publish="人们出版社")
    # print(book_obj.title, book_obj.price)

    # ============================================== 查询表记录API =======================================================
    """
    1. 方法的返回值
    all -> Queryset 支持for循环，支持索引
    2. 方法的调用者
    """
    # 1 all方法： 返回Queryset对象
    # book_list = Book.objects.all()
    # print(book_list) [obj1, obj2, obj3 .....]
    # for obj in book_list:
    #     print(obj.title, obj.price)
    # 2 first last : 调用者Queryset, 返回值：model对象
    # book = Book.objects.all().first()
    # 3 filter: 返回Queryset对象
    # book_list = Book.objects.filter(price=100)
    # print(book_list)
    # print(book_list.first())

    # 4 get() 有且只有一个结果时，正确 返回值model对象
    # book_obj = Book.objects.get(title="go", price=200)
    # print(book_obj.price)

    # 5 exclude
    # ret = Book.objects.exclude(title="go") 除此之外

    # 6 order_by 调用者queryset ，返回值queryset
    # ret = Book.objects.order_by("-id")
    # ret = Book.objects.order_by("price", "id")

    # 7 count()计数
    # ret = Book.objects.all().count()

    # 8 exists 判断表中是否有值
    # ret = Book.objects.all().exists()

    # 9 values 方法 自动循环，传入参数个数=字典内键值对个数 调用对象queryset  返回值 queryset 里面放字典
    # <QuerySet [{'price': Decimal('100.00'), 'title': 'python红宝书'}, {'price': Decimal('100.00'), 'title': 'PHP'}, {'price': Decimal('200.00'), 'title': 'go'}]>
    # ret = Book.objects.all().values("price", "title")
    # print(ret, ret[0].get("price"))

    # 10 values_list 方法 自动循环，传入参数个数=字典内键值对个数 调用对象queryset  返回值 queryset里面放准确数据元组
    # <QuerySet [(Decimal('100.00'), 'python红宝书'), (Decimal('100.00'), 'PHP'), (Decimal('200.00'), 'go')]>
    # ret = Book.objects.all().values_list("price", "title")

    # 11 distinct 去重查找，寻找种类
    # ret = Book.objects.all().values("price").distinct()
    # print(ret)

    # ============================================== 查询表记录API模糊查询 =============================================

    # ret = Book.objects.filter(price__gt=10, price__lt=200)
    # ret = Book.objects.filter(title__istartswith="p")
    # ret = Book.objects.filter(title__contains="o")
    # ret = Book.objects.filter(price__in=[100, 200, 300])
    # ret = Book.objects.filter(pub_data__year=2013)
    # print(ret)
    # return HttpResponse("OK")

    # ============================================== 删除纪律和修改记录 =============================================
    # delete 调用者：queryset对象 model对象
    # Book.objects.filter(price=200).delete()
    # Book.objects.filter(price=100).first().delete()


    Book.objects.filter(title="PHP").update(title="php")

    return HttpResponse("OK")



