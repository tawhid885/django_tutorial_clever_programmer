from django.shortcuts import render,redirect
from .models import todo

def home(request):
    to_do=todo.objects.all()

    if request.method == 'POST':
        text=request.POST['text']
        to_do=todo(text=text)
        to_do.save()
        return redirect('/')
    context={'todo':to_do}
    return render(request,'myapp/home.html',context)



def delete(request,pk):
    item=todo.objects.get(id=pk)
    item.delete()
    return redirect('/')


def update(request,pk):
    if request.method=='POST':
        item=todo.objects.get(id=pk)
        item.text = request.POST['text_update']
        item.save()
        return redirect('/')
    
    return render(request,'myapp/update.html')

