from django.contrib import admin
from django.urls import path, re_path

from blog import views

urlpatterns = [
    # 路由配置：  路径--------->视图函数
    # 分组传参 无名分组
    re_path("index/", views.index, name="index"),
    re_path(r'^articles/2003/$', views.special_case_2003, name="vsc_2003"),  # 反向解析
    re_path(r'^articles/([0-9]{4})/$', views.year_archive),
    re_path(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive, name='y_m'),  # 反向解析
    # 命名传参 有名分组
    re_path(r'^articles/(?P<y>[0-9]{4})/(?P<m>[0-9]{2})/(?P<d>[0-9]+)/$', views.article_detail),
    re_path(r'^login/$', views.login, name="Log"),
    path(r'articles/<int:y>/<int:m>/', views.path_year), # path方法。可以定义内置的type和形参
    path("orders/", views.orders)
]