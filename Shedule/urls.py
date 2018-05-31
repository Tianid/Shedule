from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^query/', views.query, name ='query', ),
    re_path(r'^sql1/',views.get_sql1,name = 'get_sql1'),
    re_path(r'^sql2/',views.get_sql2,name = 'get_sql2'),
    re_path(r'^sql3/',views.get_sql3,name = 'get_sql3'),
    path('',views.main,name = 'main'),

    path('groups/new/', views.groups_news, name='groups_new'),
    re_path(r'^groups/detail',views.groups_detail,name='groups_detail'),

    re_path(r'^groups/(?P<pk>\d+)/edit/$', views.groups_edit, name='groups_edit'),

    re_path(r'groups/(?P<pk>\d+)/detail/$',views.groups_del,name='groups_del'),

    path('teacher/new/', views.teacher_news, name='teacher_new'),
    re_path(r'^teacher/detail',views.teacher_detail,name='teacher_detail'),
    re_path(r'^teacher/(?P<pk>\d+)/edit/$', views.teacher_edit, name='teacher_edit'),
    re_path(r'teacher/(?P<pk>\d+)/detail/$',views.teacher_del,name='teacher_del'),

    path('subject/new/', views.subject_news, name='subject_new'),
    re_path(r'^subject/detail',views.subject_detail,name='subject_detail'),
    re_path(r'^subject/(?P<pk>\d+)/edit/$', views.subject_edit, name='subject_edit'),
    re_path(r'subject/(?P<pk>\d+)/detail/$',views.subject_del,name='subject_del'),

    path('dgs/new/', views.dgs_news, name='dgs_new'),
    re_path(r'^dgs/detail',views.dgs_detail,name='dgs_detail'),
    re_path(r'^dgs/(?P<pk>\d+)/edit/$', views.dgs_edit, name='dgs_edit'),
    re_path(r'dgs/(?P<pk>\d+)/detail/$',views.dgs_del,name='dgs_del'),
]