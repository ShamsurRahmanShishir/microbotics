from django.shortcuts import render

# Create your views here.
def app1(request):
    return render(request,'f1/variable.html',{'shishir':5,'train':9})
def bigdata(request):
    return render(request,'f1/bdata.html')
def dataanalysis(request):
    return render(request,'f1/dataanalysis.html')
def deep_learning(request):
    return render(request,'f1/dl.html')
