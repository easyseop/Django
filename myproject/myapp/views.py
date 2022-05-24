from django.shortcuts import render


def home(request):
    return render(request,'index.html')

#어떤 요청이 들어오면 index.html을 보여줄지 ? 
# Create your views here.
def test(request):
    return render(request,'test.html')

def first(request):
    return render(request,'first.html')