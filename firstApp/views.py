from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("Hello World")
def home(request):
  return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def por1(request):
    return render(request, 'portfolio-1-col.html')
def por2(request):
    return render(request, 'portfolio-2-col.html')
def por3(request):
    return render(request, 'portfolio-3-col.html')
def por4(request):
    return render(request, 'portfolio-4-col.html')
def porItem(request):
    return render(request, 'portfolio-item.html')
def blog1(request):
    return render(request, 'blog-home-1.html')
def blog2(request):
    return render(request, 'blog-home-2.html')
def blogPost(request):
    return render(request, 'blog-post.html')
def fullWidth(request):
    return render(request, 'full-width.html')
def sidebar(request):
    return render(request, 'sidebar.html')
def faq(request):
    return render(request, 'faq.html')
def pageNotFound(request):
    return render(request, '404.html')
def pricing(request):
    return render(request, 'pricing.html')
#搜尋頁面
def search_view(request):
    return render(request, 'search.html')
#登入頁面
def login_view(request):
    return render(request, 'login.html')
#課程資訊
def courseDetail_view(request):
    return render(request, 'courseDetail.html')