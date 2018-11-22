from django.views.generic import ListView, DeleteView
from django.shortcuts import render
from .models import Post

'''
# Create your views hereselfselfself.
def post_list(request):
    return render(request, 'blog/post_list.html')
'''

post_list=ListView.as_view(model=Post)

post_detail=DeleteView.as_view(model=Post)
