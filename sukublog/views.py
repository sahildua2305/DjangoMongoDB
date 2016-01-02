#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-01 19:27:32
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-03 01:26:00

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from mongoengine import *

from .models import User, Post, Comment, BlogPost, ImagePost, VideoPost, QuotePost, LinkPost


class IndexView(generic.ListView):
	template_name = 'sukublog/index.html'
	context_object_name = 'latest_post_list'

	def get_queryset(self):
		"""
		Return the last 10 posts
		"""
		return Post.objects(created_at__lte=timezone.now()).order_by('-created_at')[:10]


class ViewPostView(generic.DetailView):
	model = Post
	template_name = 'sukublog/view-post.html'
	context_object_name = 'post'

	def get_queryset(self):
		"""
		Excludes any posts that aren't published yet.
		"""
		return Post.objects.filter(created_at__lte=timezone.now())


def delete_post(request, slug):
	try:
		post = Post.objects.get(pk=slug)
	except (KeyError, Post.DoesNotExist):
		pass
	else:
		post.delete()
	finally:
		''' Always return an HttpResponseRedirect after successfully dealing with POST data.
		This prevents data from being posted twice if a user hits the Back button'''
		return HttpResponseRedirect(reverse('sukublog:index', args=()))
