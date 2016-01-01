#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-01 19:27:32
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-02 04:16:36

from django.conf.urls import url, include, patterns

from . import views

app_name = 'sukublog'
urlpatterns = [
	# ex: /blog/
	url(r'^$', views.IndexView.as_view(), name='index'),
	# ex: /blog/first-post/
	url(r'^(?P<slug>[-\w]+)/$', views.ViewPostView.as_view(), name='view_post'),
	# ex: /blog/delete/first-post/
	url(r'^delete/(?P<slug>[-\w]+)/$', views.delete_post, name='delete_post'),
]
