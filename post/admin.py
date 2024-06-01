from django.contrib import admin
from .models import Car, ExamQuestion, ExamAnswer
# Register your models here.


admin.site.register(Car)

class ExamAnswerInline(admin.TabularInline):
    model = ExamAnswer
    extra = 1

@admin.register(ExamQuestion)
class ExamQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'created_at']
    inlines = [ExamAnswerInline]
# admin.site.register(ExamQuestion)
