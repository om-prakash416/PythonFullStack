from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
import random
from .models import Question
# Create your views here.

def home(request):
    return HttpResponse("Hello from Django")



def get_quiz(request):
    try:
        question_objs = list(Question.objects.all())
        data = []
        random.shuffle((question_objs))
         
        print(question_objs)
        
        for question_obj in question_objs:
            data.append({
                "category": question_obj.category.category_name,
                "question": question_obj.question,
                "marks": question_obj.marks
            })
        
        payload = {"status": True, "data": data}
        return JsonResponse(payload)
    
    except Exception as e:
        print(f"Error in get_quiz view: {str(e)}")
        return HttpResponse("Something went wrong", status=500)