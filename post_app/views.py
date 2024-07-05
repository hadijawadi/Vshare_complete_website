from django.shortcuts import render
from .forms import  TextForm
from django.http import HttpResponse


#   showing which post user will crate
def home_post(request):
        return render(request, 'post_app/pages/create.html')


def create_text_post(request):
    form = TextForm()
    if request.method == 'POST':
          form = TextForm(request.POST)
          if form is not None:
                form.save()
                return HttpResponse('your post created man')
          else:
              return HttpResponse('you have an error')
    
    return render(request, 'post_app/pages/create_text.html',context = {'form':form})


from .models import Create_text_post

def show_posts(request):
       data = Create_text_post.objects.all()
       context = {
             'data':data
       }


       return render(request, 'post_app/pages/posts.html',context)


