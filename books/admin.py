#!/usr/bin/python
# -*- coding:utf-8 -*-


from django.contrib import admin

from .models import Publisher, Author, Book, Borrower, Relation


# 作者管理
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'email')
    search_fields = ('first_name', 'last_name')  # 查询作者
    list_per_page = 10


# 出版社管理显示
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'country', 'state_province', 'city', 'website')
    search_fields = ('name',)  # 查询书名
    list_per_page = 10


# 书管理显示
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'book_no', 'publisher', 'publication_date', 'create_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    list_per_page = 10
    # fields = ('title', 'authors', 'publisher', 'publication_date')  # 'publication_date' 被隐藏，以防编辑
    filter_horizontal = ("authors",)
    raw_id_fields = ('publisher',)


# 借书者管理
class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('borrower_name', 'mobile', 'email')
    search_fields = ('borrower_name',)  # 查询借书者
    list_per_page = 10


# 借书者管理
class RelationAdmin(admin.ModelAdmin):
    list_display = ('book_no', 'book_name', 'borrower_name', 'start_date', 'end_date', 'borrower_flag')
    search_fields = ('borrower_name',)  # 查询借书者
    raw_id_fields = ('book_name', 'borrower_name',)
    list_per_page = 10


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrower, BorrowerAdmin)
admin.site.register(Relation, RelationAdmin)
