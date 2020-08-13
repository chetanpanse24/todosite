from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView    
from .models import TaskInfo
from django.urls import reverse


class TaskList(ListView):
    model = TaskInfo
    context_object_name = 'tasklist'
    template_name = 'index.html'


class CreateTask(CreateView):
    model = TaskInfo
    fields = ['title', 'content']
    template_name = 'create_task.html'

    def get_success_url(self):
        return reverse('todoapp:index')


class UpdateTask(UpdateView):
    model = TaskInfo
    fields = ['title', 'content']
    template_name = 'update_task.html'

    def get_success_url(self):
        return reverse('todoapp:index')


class DeleteTask(DeleteView):
    model = TaskInfo
    template_name = 'delete_task.html'

    def get_success_url(self):
        return reverse('todoapp:index')
