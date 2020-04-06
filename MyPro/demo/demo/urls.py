"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include, register_converter

from blog.urlconvert import MonConvert
register_converter(MonConvert, "mm")  # 规则自定义转换器

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('timer/', views.timer),
    # 路由配置：  路径--------->视图函数
    # 分组传参 无名分组
    # re_path(r'^articles/2003/$', views.special_case_2003),
    # re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    # re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    # # 命名传参 有名分组
    # re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<d>[0-9]+)/$', views.article_detail),
    # re_path(r'^login/$', views.login)
    # ^以什么什么开头， $以什么神秘结尾
    # 全局管理 路由分发
    re_path(r"blog/", include(("blog.urls", "blog"))),  # 元组内（路由分发，命名空间）
    re_path(r"clog/", include(("clog.urls", "clog"))),  # 元组内（路由分发，命名空间）
    re_path(r"dlog/", include(("dlog.urls", "dlog")) ),
    # re_path(r"^", include("blog.urls"))
    # re_path(r"blog/", include("blog.urls"))
    path(r'articles/<int:y>/<int:m>/', views.path_year),
    path(r"articles/<mm:month>/", views.path_month),
    re_path(r"^$", views.timer)  # 根路径
]


"""
1.简单正则表达式配置
2.正常分组(re_path)：按照位置匹配传参。有名分组：按照名字匹配传参 （PS）re_path 位置内加括号才能进行参数传递--元组
3.全局url进行路由分发到分布应用里： re_path(r"clog/", include(("clog.urls", "clog"))),  # 元组内（路由分发，命名空间）-解耦
4.反向解析：给url进行命名 不会写死一个url ，re_path(r'^articles/2003/$', views.special_case_2003, name="vsc_2003")
    反向解析 from django.urls import 。。。。url = reverse("blog:Log")
    html内反向解析 <form action="{% url "blog:Log" %}" method="POST"> {# 模板语法<!--反向解析 action="{% url "Log" %}--> #}
5.命名空间：re_path(r"clog/", include(("clog.urls", "clog"))),  # 元组内（路由分发，命名空间），隔离不同应用中，相同的反向解析
    名称，视图函数接收时格式 url = reverse("blog:Log") 
6.自定义匹配规则，需要自己写匹配规则，并进行注册 urlconcert
7.render方法可以响应html网页界面。使用request.GET或者request.POST可以拿到请求中的键值对，使用get方法可以得到数据，request还有
    更多方法
8.模板语法 1.{{ }} 2{% %}
9.模板语法：
    变量: {{ }}-渲染变量
        1.深度查询  句点符
        2.过滤器
    标签: {% %}-渲染标签
        1.url
        2.css
        3....
10. 深度查询 X.Y.Z.M.N {% with person_list.1.name as name %}
11. 过滤器 <p>{{ link|safe }}</p>--渲染html标签必须加上safe views视图控制器使用return render(request, "index.html", locals())
    返回所有局部变量 
12. 跨域请求{% csrf_token %}--POST
13. if with for 标签{% %}
14. 自定义标签和过滤器 自建templatetags python包 再里面新建文件进行规则制定
15. 模块加载：将一个页面分割成不同的模块(X.html) {% include "advertise.html" %}使用include加载模块
16. 模块封装和使用： 主模块base.html中有许多钩子     
    {% block title %}
        <title>base</title>
    {% endblock title %}
    使用{% extents base.html %} 加载主模块(必须卸载第一行) 在下面使用
    {% block title %}
        <title>Order</title>
    {% endblock title %}
    覆盖base.html中的钩子
    或者使用
    {% block con %}
    {{ block.super }}
    <h1>单价</h1>
    {% endblock con %}
    再原有钩子上增加内容
"""
"""
http://127.0.0.1:8000/index/
url:协议：//IP:port/路径？get请求数据
"""