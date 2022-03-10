from django.shortcuts import render
import joblib
from backend.forms import PredictorForm
import numpy as np

def predictor(request):
    form = PredictorForm()
    if request.method == "POST":
        form = PredictorForm(request.POST)
        if form.is_valid():
            close = np.array(form.cleaned_data.get('close'))
            model = joblib.load('model.sav')
            prediction = model.predict(np.reshape(close,(-1,1)))
            
            return render(
                request,'predictor.html',
                {'form':form,'prediction':round(prediction[0],5)}
            )
        
    return render(request,'predictor.html',{'form':form})


def market(request):
    return render(request,'sidebar/market.html')

def talk(request):
    return render(request,'sidebar/talk.html')