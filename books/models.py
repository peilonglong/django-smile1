#!/usr/bin/python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
# 出版社
@python_2_unicode_compatible
class Publisher(models.Model):
    name = models.CharField(max_length=50, verbose_name='出版社名称')
    address = models.CharField(max_length=50, verbose_name='详细地址')
    city = models.CharField(max_length=70, verbose_name='市')
    state_province = models.CharField(max_length=80, verbose_name='省')
    country = models.CharField(max_length=50, verbose_name='所属国家')
    website = models.URLField(verbose_name='网站')

    def __str__(self):
        return self.name

    # 默认排序方式
    class Meta:
        verbose_name = '出版社'
        verbose_name_plural = '出版社'
        ordering = ['name']


# 书作者
@python_2_unicode_compatible
class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='FirstName')
    last_name = models.CharField(max_length=40, verbose_name='LastName')
    mobile = models.CharField(max_length=20, verbose_name='联系电话')
    email = models.EmailField(blank=False, verbose_name='邮箱')

    def __str__(self):
        return u'%s%s' % (self.first_name, self.last_name)

    class Meta:
        verbose_name='作者'
        verbose_name_plural='作者'

# 借书作者
@python_2_unicode_compatible
class Borrower(models.Model):
    borrower_name = models.CharField(max_length=40, verbose_name='借书人姓名')
    mobile = models.CharField(max_length=20, blank=False, verbose_name='联系电话')
    email = models.EmailField(blank=False, verbose_name='邮箱')
    create_date = models.DateField(blank=True, verbose_name='创建日期')

    def __str__(self):
        return self.borrower_name

    class Meta:
        verbose_name='借书人'
        verbose_name_plural='借书人'


# 书
@python_2_unicode_compatible
class Book(models.Model):
    book_no = models.CharField(max_length=200, blank=True, verbose_name='编号')
    title = models.CharField(max_length=200, verbose_name='书名')
    authors = models.ManyToManyField(Author, verbose_name='作者')
    publisher = models.ForeignKey(Publisher, verbose_name='出版社')
    publication_date = models.DateField(blank=True, verbose_name='出版日期')
    create_date = models.DateField(blank=True, verbose_name='创建日期')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='书'
        verbose_name_plural='书'

# 书和借书者关系
@python_2_unicode_compatible
class Relation(models.Model):
    book_no = models.CharField(max_length=200, blank=True, verbose_name='编号')
    book_name = models.ForeignKey(Book, verbose_name='书名')
    borrower_name = models.ForeignKey(Borrower, verbose_name='借书人')
    start_date = models.DateField(blank=True, verbose_name='借书日期')
    end_date = models.DateField(blank=True, verbose_name='还书日期')
    borrower_flag = models.CharField(max_length=100, blank=True, verbose_name='备注')

    def __str__(self):
        return u'%s,借书人:%s' % (self.book_name, self.borrower_name)

    class Meta:
        verbose_name='所借图书'
        verbose_name_plural='所借图书'