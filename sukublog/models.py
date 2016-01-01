#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-01-01 19:27:32
# @Last Modified by:   sahildua2305
# @Last Modified time: 2016-01-02 01:39:48

from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from mongoengine import *

import datetime

# All documents are saved in a MongoDB collection rather than a table
class User(Document):
	email = StringField(required=True)
	first_name = StringField(max_length=50)
	last_name = StringField(max_length=50)


# Embedded documents don't have any separate collection in the database
class Comment(EmbeddedDocument):
	created_at = DateTimeField(default=datetime.datetime.now, required=True)
	author = StringField(max_length=255, verbose_name="Name", required=True)
	body = StringField(verbose_name="Comment", required=True)


# Post class can be considered as a base class
class Post(Document):
	title = StringField(max_length=255, required=True)
	"""
	`ReferenceField` objects are imilar to foreign keys in traditional ORMs
	Automatically translated into references when they are saved,
	and dereferenced when they are loaded

	It takes a keyword `reverse_delete` for handling deletion rules,
	if the reference is deleted.
	Setting it to CASCADE will delete all the posts if a user is deleted
	"""
	author = ReferenceField(User, reverse_delete=CASCADE)
	created_at = DateTimeField(default=datetime.datetime.now, required=True)
	slug = StringField(max_length=255, required=True, primary_key=True)
	comments = ListField(EmbeddedDocumentField('Comment'))

	def get_absolute_url(self):
		return reverse('post', kwargs={"slug": self.slug})

	def __unicode__(self):
		return self.title

	@property
	def post_type(self):
		return self.__class__.__name__

	"""
	`allow_inheritance` has to be set to True to allow this class to act as a base class
	"""
	meta = {
		'indexes': ['-created_at', 'slug'],
		'ordering': ['-created_at'],
		'allow_inheritance': True
	}


# Subclass of Post
class BlogPost(Post):
	body = StringField(required=True)


# Subclass of Post
class ImagePost(Post):
	image = ImageField(required=True)


# Subclass of Post
class VideoPost(Post):
	embed_code = StringField(required=True)


# Subclass of Post
class QuotePost(Post):
	body = StringField(required=True)
	author = StringField(max_length=255, verbose_name="Author name", required=True)


# Subclass of Post
class LinkPost(Post):
	link_url = StringField(required=True)
