#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-01 19:27:32
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-02 01:26:22

from django.contrib import admin

from mongoengine import *

from sukublog.models import BlogPost, ImagePost, VideoPost, QuotePost, LinkPost
