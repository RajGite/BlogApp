from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post,UsersCategories
from .forms import PostForm,CategoryForm
# Create your views here.
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance= form.save(commit=False)
        instance.save()
    #if request.method == "POST":
    #   title=request.POST.get("title")
    #   content=request.POST.get("content")
    #   Post.objects.create(title=title,content=content)
    context = {
        "form":form,
        "title": "Form",
    }
    return render(request,"post_form.html",context)

def post_detail(request,id):
    instance = get_object_or_404(Post,id=id)
    context = {
        "title":instance.title,
        "instance": instance
    }
    return render(request,"post_detail.html",context)

def post_list(request):
    if (request.user.is_authenticated):
        username = request.user.username
    obj = UsersCategories.objects.filter(user=username)
    queryset1= Post.objects.none()
    for i in obj:
        queryset2 = Post.objects.filter(category=i.category)
        queryset1=(queryset1 | queryset2)
    context = {
        "object_list": queryset1,
        "title":"List"
    }
    return render(request,"index.html",context)

def post_update(request):
    return HttpResponse("<h1>Hello</h1>")

def post_delete(request):
    return HttpResponse("<h1>Hello</h1>")

def select_category(request):
    title = "Genere"
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        Select_Options = form.cleaned_data.get('Select_Options')
        #print(Select_Options)
        if request.user.is_authenticated():
            username = request.user.username
        for i in Select_Options:
            list = UsersCategories.objects.filter(user=username,category=i)
            if(list.count()==0):
                category = UsersCategories(user=username,category=i)
                category.save()
        return post_list(request)

    return render(request,"category.html",{'form':form,'title':title})
