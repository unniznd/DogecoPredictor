from django.shortcuts import render
from django.contrib import messages

import joblib
from backend.forms import PredictorForm
import numpy as np

def predictor(request):
    form = PredictorForm()
    if request.method == "POST":
        form = PredictorForm(request.POST)
        if form.is_valid():
            close = np.array(form.cleaned_data.get('close'))
            model = joblib.load('model/model.sav')
            prediction = model.predict(np.reshape(close,(-1,1)))
            messages.success(request,"Prediction Successful")
            return render(
                request,'predictor.html',
                {'form':form,'prediction':round(prediction[0],5)}
            )
        else:
            messages.error(request,"Error : Enter a valid input")
            return render(
                request,'predictor.html',
                {'form':form}
            )

    return render(request,'predictor.html',{'form':form})


def market(request):
    return render(request,'sidebar/market.html')

def talk(request):
    return render(request,'sidebar/talk.html')

def page_not_found(request,exception):
    return render(request,"error/404.html")


def internal_error(request):
    return render(request,"error/500.html")