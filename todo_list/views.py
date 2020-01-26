from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from todo_list.models import Todo
from django.http import HttpResponseRedirect
# Create your views here.
    # 7:05:00


def home(request):
    todo_item = Todo.objects.all().order_by("added_date")
    return render(request,'main/index.html',{
        "todo_items" : todo_item
    })

@csrf_exempt
def add_todo(request):
    current_added_date =  timezone.now()
    content = request.POST['todo']
    result = Todo.objects.create(added_date = current_added_date,text = content)
    return HttpResponseRedirect("/")

@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")    
    
    
