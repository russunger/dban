from django.shortcuts import render
from blog.models import Test


# Create your views here.
def blog_index(request):
    blog_list = Test.objects.all()  # 获取所有数据
    return render(request,'index.html', {'blog_list':blog_list})   # 返回index.html页面