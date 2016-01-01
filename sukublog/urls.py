#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-01 19:27:32
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-01 19:40:13

from django.conf.urls import url, include, patterns

from sukublog.views import (PostDetailView)

from . import views

app_name = 'sukublog'
urlpatterns = [
	# ex: /blog/
	url(r'^$', PostDetailView.as_view(), name='post'),
]
