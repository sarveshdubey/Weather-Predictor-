from django.http.response import HttpResponse
import requests
from django.shortcuts import render
from requests.api import request
import pickle 
import numpy as np
from .models import weather 

import csv

def post(request):
  if request.method=="POST":
    lat = request.POST['lat']
    lon = request.POST['lon']
    apiid = ''
    url ='http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid={}'.format(lat,lon,apiid)
    r = requests.get(url)
    data = r.json()
    param={  'city' : data['name'],
            'country': data['sys']['country'],
            'description': data['weather'][0]['description'],
            'humidity':data['main']['humidity'],
            'windspeed':data['wind']['speed'],
            'visibility':data['visibility'],
          }
    data1 =weather(
                   city=data['name'],
                   country=data['sys']['country'],
                   longitude=data['coord']['lon'],
                   lattitude=data['coord']['lat'],
                   description=data['weather'][0]['description'],
                   temp=data['main']['temp'],
                   tempmax=data['main']['temp_max'],
                   tempmin=data['main']['temp_min'],
                   humidity=data['main']['humidity'],
                   sunset=data['sys']['sunset'],
                   sunrise=data['sys']['sunrise'],
                   windspeed=data['wind']['speed'],
                   timezone=data['timezone'],
                   visibility=data['visibility'],
                   
                   )    
    data1.save()                    
    print(param)        
    context = {'context':param}
    return render(request,'index.html',context)
  return render(request,'index.html')   

#making predictions
def predict(a):
  model = pickle.load(open('model.pickle','rb'))
  prediction = model.predict(a)
  if prediction == 0:
    return 'no'
  elif prediction == 1:
    return 'yes'
  else:
    return 'Opps! error 404'

def result(request):
  Temp = request.GET['Temp']      
  Max_Temp = request.GET['Max_Temp']       
  Min_Temp = request.GET['Min_Temp']       
  Humidity = request.GET['Humidity']       
  Windspeed = request.GET['Windspeed']       
  Visibility = request.GET['Visibility']  
  Description_n= request.GET['Description_n'] 
  array=[Temp,Max_Temp,Min_Temp,Humidity,Windspeed,Visibility,Description_n]
  a = np.asarray(array).reshape(1,-1)
  result = predict (a)
  return render(request,'result.html',{'result':result})    

#Exporting  Django DB to a CSV file     
def export(request):
    response = HttpResponse(content_type='text/csv')

    writer = csv.writer(response)
    writer.writerow(['City','Country','Longitude','Lattitude','Description','Temperature','Max_Temp','Min_Temp','Humidity','Sunset','Sunrise','Windspeed','Visibility'])

    for w in weather.objects.all().values_list('city','country', 'longitude', 'lattitude' ,'description' ,'temp', 'tempmax', 'tempmin' ,'humidity' ,'sunset' ,'sunrise', 'windspeed' ,'visibility'):
        writer.writerow(w)

    response['Content-Disposition'] = 'attachment; filename="weather.csv"'

    return response            

