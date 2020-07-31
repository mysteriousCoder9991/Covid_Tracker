from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from covid import Covid
import requests 
import pandas as pd
import os 
import numpy as np 

# Create your views here.
def home(request):

    covid = Covid(source="worldometers")
    cases = covid.get_status_by_country_name("india")
    confirmed=cases['confirmed']
    recovered=cases['recovered']
    active=cases['active']
    new_cases=cases['new_cases']
    deaths=cases['new_deaths']
    tt=cases['total_tests']
    deceased=confirmed-active-recovered
    context={'confirmed':confirmed,'active':active,'recovered':recovered,
    'deceased':deceased,'new_cases':new_cases,'deaths':deaths,'tests':tt}
    return render(request,'index.html',context)

def error(request,slug):
    context={'slug':slug}
    return render(request,'error.html',context)

def contact(request):
    return render(request,'contact.html')

def stateCon(request):
    df1=pd.read_csv('static/c.csv',index_col="State/UnionTerritory")
    state=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh',
       'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh',
      'Uttarakhand','West Bengal']
    state1=['AndamanandNicobarIslands','AndhraPradesh','ArunachalPradesh','Assam','Bihar','Chandigarh','Chhattisgarh','DadraandNagarHaveliandDamanandDiu','Delhi','Goa','Gujarat','Haryana','HimachalPradesh',
       'JammuandKashmir','Jharkhand','Karnataka','Kerala','Ladakh','MadhyaPradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','TamilNadu','Telangana','Tripura','UttarPradesh',
      'Uttarakhand','WestBengal']
    df=df1.drop(['Sno'],axis=1)
    cd=[] 
    nl=[] 
    val=[]
    for i  in range(0,len(state)):
        cd=df.loc[state[i]]
        data=cd['Confirmed']
        nl.append(data.tail(1))
        val.append(int(nl[i]))
    data={state1[i]:val[i] for i in range(len(state))}
    return render(request,'confirmed.html',data)
    
def stateCured(request):
    df1=pd.read_csv('static/c.csv',index_col="State/UnionTerritory")
    state=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh',
       'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh',
      'Uttarakhand','West Bengal']
    state1=['AndamanandNicobarIslands','AndhraPradesh','ArunachalPradesh','Assam','Bihar','Chandigarh','Chhattisgarh','DadraandNagarHaveliandDamanandDiu','Delhi','Goa','Gujarat','Haryana','HimachalPradesh',
       'JammuandKashmir','Jharkhand','Karnataka','Kerala','Ladakh','MadhyaPradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','TamilNadu','Telangana','Tripura','UttarPradesh',
      'Uttarakhand','WestBengal']
    df=df1.drop(['Sno'],axis=1)
    cd=[] 
    nl=[] 
    val=[]
    for i  in range(0,len(state)):
        cd=df.loc[state[i]]
        data=cd['Cured']
        nl.append(data.tail(1))
        val.append(int(nl[i]))
    data={state1[i]:val[i] for i in range(len(state))}
    return render(request,'cured.html',data)

def stateDec(request):
    df1=pd.read_csv('static/c.csv',index_col="State/UnionTerritory")
    state=['Andaman and Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh','Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat','Haryana','Himachal Pradesh',
       'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Madhya Pradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh',
      'Uttarakhand','West Bengal']
    state1=['AndamanandNicobarIslands','AndhraPradesh','ArunachalPradesh','Assam','Bihar','Chandigarh','Chhattisgarh','DadraandNagarHaveliandDamanandDiu','Delhi','Goa','Gujarat','Haryana','HimachalPradesh',
       'JammuandKashmir','Jharkhand','Karnataka','Kerala','Ladakh','MadhyaPradesh','Maharashtra','Manipur','Meghalaya',
       'Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','TamilNadu','Telangana','Tripura','UttarPradesh',
      'Uttarakhand','WestBengal']
    df=df1.drop(['Sno'],axis=1)
    cd=[] 
    nl=[] 
    val=[]
    for i  in range(0,len(state)):
        cd=df.loc[state[i]]
        data=cd['Deaths']
        nl.append(data.tail(1))
        val.append(int(nl[i]))
    data={state1[i]:val[i] for i in range(len(state))}
    return render(request,'deceased.html',data)