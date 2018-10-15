#!/usr/bin/python
# -*- coding:utf-8 -*-

import datetime

import pymysql
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Question, Choice


# Create polls views default index here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """ Return the last  five published questions."""
        return Question.objects.order_by('-pub_date')[:10]


# Create detail page here.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


# Create results page here.
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


# 当前时间
def current_time(request):
    now = datetime.datetime.now()
    print now.strftime("%Y-%m-%d %H:%M:%S %w")
    return render(request, 'polls/current_time.html', {'current_date': now})


# 查询数据库数据并显示
def book_list(request):
    db = pymysql.connect(host='ngaribata.mysql.rds.aliyuncs.com',
                         user='houxr',
                         password='HxrOpDev2016_',
                         db='eh_base_feature4',
                         charset='utf8',
                         cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    sql = "select bankname from base_bank"
    cursor.execute(sql)
    names = cursor.fetchall()
    print "SQL:"+sql
    for row in names:
        print(row)
    db.close()
    return render(request, 'polls/books.html', {'names': names})
