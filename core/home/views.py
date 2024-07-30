from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# def home(request):
#     return HttpResponse("""<h1>Hey im django</h1>
#             <p> thinsnknkjj</p>
#             <hr>
#             <h2 style="color:red">vhishdieji</h2>            
#                         """)

# def home(request):
#     return render(request,"index.html")

def home(request):
    peoples=[
        {"name":"abhshek",'age':22},
        {"name":"om","age":10},
        {"name":"bhola","age":12},
        {"name":"prakash","age":55}
    ]
    text =""" 
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Consectetur, dolor sapiente et reiciendis exercitationem sit atque saepe distinctio fugiat dolore? Nesciunt accusantium excepturi rem aliquam commodi consectetur facere doloremque aspernatur.
"""
    vegetables = ["tamato","pumpkin","potatos"]
    for people in peoples:
        print(people)
    return render (request,"index.html", context = {'page':"Django tutorial","peoples":peoples,"text":text,"vegetables":vegetables})

def about(request):
    context={"page":"About Page"}
    return render(request,"about.html",context)

def contact(request):
    context={"page":"Contact Page"}
    return render(request,"contact.html",context)

def success_page(request):
    print("*"*10)
    return HttpResponse("<h1>success to learn django</h1>")
