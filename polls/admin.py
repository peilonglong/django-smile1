from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
                 ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


#
# class MemberAdmin(admin.ModelAdmin):
#     """Customize the look of the auto-generated admin for the Member model"""
#     list_display = ('name', 'instrument')
#     list_filter = ('band',)


# Register polls models here.
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
# admin.site.register(Member, MemberAdmin)
# admin.site.register(Band)
