from django.shortcuts import render
from calculate.models import csv_file_upload
from django.http import HttpResponseRedirect,HttpResponse
import pandas as pd
from django.conf import settings
from django.contrib import messages
# Create your views here.
def homepage(request):
    context = csv_file_upload.objects.all()
    data = {
        "context" : context
    }
    return render(request,'index.html',data)

def import_csv_file(request):
    
    if request.method == 'POST':
        file = request.FILES['csv_file']
        obj = csv_file_upload.objects.create(csv_file = file)
        df = pd.read_csv(f"{settings.BASE_DIR}/{obj.csv_file}")
        datalist =[]
        for list in df.values.tolist():
            datalist.append(list) 
        context = csv_file_upload.objects.all()
        data = {
        "context" : context,
        'datalist':datalist
        }    
    return render(request,'index.html',data)

def get_diplay_filedata(request):
    if request.method == "GET":
        selected_file = request.GET.get('obj')

    messages.success(request,"Dataset is selected")    
    df = pd.read_csv(f"{settings.BASE_DIR}/{selected_file}")
    data_list = []
    for list in df.values.tolist():
        data_list.append(list)
    request.session['data_list'] = data_list
    #k represents dataframe
    k= pd.DataFrame(df)
    context = csv_file_upload.objects.all()
    
    summation = sum(k.iloc[:,0])
    minvalue = min(k.iloc[:,0])
    maxvalue = max(k.iloc[:,0])
    no_of_columns = k.iloc[0]


    data = {
        'context' : context,
        'summation':summation,
        'minvalue' : minvalue,
        'maxvalue' : maxvalue,
        'no_of_columns' : no_of_columns
        
        }    
    return render(request,'index.html',data)

def get_result(request):
    if request.method == 'POST':
        ans = request.POST.get('option')
    context = csv_file_upload.objects.all()
    data = {
        'context' : context,
        'ans': ans,
    }
    return render(request,'index.html',data)


def plot(request):
    if request.method=="GET":
        column_choise = request.GET.getlist("plot_col")
        if len(column_choise) != 2:
            
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        #unpacking selected columns
        x_col, y_col = tuple(column_choise)
        data_list = request.session['data_list']
        x_axis_values = []
        y_axis_values = []

        #to get selected column values to plot
        for list in data_list:
            x_axis_values.append(list[int(x_col)])
            y_axis_values.append(list[int(y_col)])
        
        zipped_list = tuple(zip(x_axis_values,y_axis_values))
        
        
        context = csv_file_upload.objects.all()
        plot_data = {
        'context' : context,
        'zipped_list' : zipped_list,
        }

        
    return render(request,'index.html',plot_data)
