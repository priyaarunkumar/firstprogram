from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from . models import task
from . forms import TaskForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
# Create your views here.
class tasklist(ListView):

    model=task
    template_name = 'firstt.html'
    context_object_name = 'ta'

class taskdetail(DetailView):
    model=task
    template_name = 'details.html'
    context_object_name = 'task'
class taskupdate(UpdateView):
    model=task
    template_name = 'update.html'
    context_object_name = 'task'
    fields=('name','pri','date')
    success_url =reverse_lazy('todoapp:taskhome')


    def get_success_url(self):

    #
        return reverse_lazy('todoapp:taskdetailss',kwargs={'pk':self.object.id})
class taskdelete(DeleteView):
    model=task
    template_name = 'delete.html'
    success_url =reverse_lazy('todoapp:taskhome')


def fun(request):
    taskk = task.objects.all()
    if request.method=='POST':
        name=request.POST.get('name',)
        pri=request.POST.get('pri',)
        date=request.POST.get('date',)
        ta=task(name=name,pri=pri,date=date)
        ta.save()

    return render(request,"firstt.html",{'ta':taskk})
def delete(request,id):

    if request.method == 'POST':

        t=task.objects.get(id=id)

        t.delete()
        return redirect('/')
    return render(request,'delete.html')
def update(request,id):
    tu=task.objects.get(id=id)
    tform=TaskForm(request.POST or None,instance=tu)
    if tform.is_valid():
        tform.save()
        return redirect('/')
    return render(request,'edit.html',{'tuu':tu,'ttform':tform})


