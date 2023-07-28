from django.shortcuts import render
from django.views import generic
from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.
class TaskList(generic.View):
    def get(self, request, *args, **kwargs):
        form = TaskForm()
        tasks = Task.objects.all()
        context = {
            'form':form,
            'tasks':tasks,
        }
        return render(request, 'task/task_list.html', context=context)
    
    def post(self, request, *args, **kwargs):
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status =200)
        else:
            return redirect('task_list')
    

class TaskCompleted(generic.View):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.completion  = True
        task.save(update_fields=['completion'])
        return JsonResponse({'task': model_to_dict(task)}, status =200)
    

class DeleteTask(generic.View):
    def post(self, request, id):
        task = get_object_or_404(Task, id=id)
        task.delete()
        return JsonResponse({'result':'done'}, status =200)


    
    

