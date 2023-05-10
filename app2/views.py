
from django.shortcuts import render


# Create your views here.
def app2(request):
    study1 = '60 days of python'
    study2 = 'learn django in 30 days'
    study3 = 'learn AI in 30 days'
    study4 = 'learn ML in 30 days'
    study_plan= {'s1':study1,'s2':study2,'s3':study3,'s4':study4}
    
    return render(request,'f2/filter.html',study_plan)
def ml(request):
    ml_learn = {'data_science':['ml','AI','007','python']}
    return render(request,'f2/ml.html',ml_learn)
