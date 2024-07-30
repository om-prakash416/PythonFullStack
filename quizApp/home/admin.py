# # from django.contrib import admin
# # from .models import Question, Category, Answer
# # # Register your models here.


# # from .models import *

# # admin.site.register(Category)

# # class AnswerAdmin(admin.StackedInline):
# #     model=Answer
    
# # class Question(admin.ModelAdmin):
# #     inlines =[AnswerAdmin]
    
    
# # admin.site.register(Question)
# # admin.site.register(Answer)


# from django.contrib import admin
# from .models import Question, Category, Answer

# admin.site.register(Category)

# class AnswerAdmin(admin.StackedInline):
#     model = Answer

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerAdmin]

# admin.site.register(Question, QuestionAdmin)
# # admin.site.register(Question)
# admin.site.register(Answer)

from django.contrib import admin
from .models import Question, Category, Answer

admin.site.register(Category)

# class AnswerInline(admin.StackedInline):
#     model = Answer

# class QuestionAdmin(admin.ModelAdmin):
#     inlines = [AnswerInline]

admin.site.register(Question)
admin.site.register(Answer)

