

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.models import HoverTool
from .forms import InputForm

def home(request):
    first_graph="my first bokeh graph will be rendered on this page"
    return HttpResponse(first_graph)

def formtest(request):
    #This form was  built to test that a value can be submitted and passed to the backend
    
    if request.method=="POST": 
        form=InputForm(request.POST)
        if form.is_valid():
            scalar=form.cleaned_data['scalar']
            print("This is the scalar:" )
            print(scalar)

    return render(request,'formtest.html',{'form':form})

def starter(request):
    #setting up form
    form=InputForm(request.POST)
    if request.method=="POST": 
        
        if form.is_valid():
            scalar=form.cleaned_data['scalar']
            print("This is the scalar:" )
            print(scalar)
    else:
        form=None
     
   
    #Creating the plots
    x=[0,1,0.5,1,1.5,2,2.5,3]
    y0=[2**i for i in x]
    y1=[2.1*i for i in x]
    y2=[3*i for i in x]
    y3=[i**2 for i in x]

    plot0=figure()#All plots are an instance of the figure class.

    #pylint: disable=too-many-function-args
    plot0.circle(x,y0, size=20, color="blue")
    #Defines the data as x being [1,10,35,27] and [0,0,0,0]
    #Defines the data points to be blue circles of size 20
    
    #Trying out a combo plot
    plot0.line(x,y1,legend="Plotting y1")
    plot0.circle(x,y2,legend="Plotting y2",fill_color="red", size=20)

    #Trying out multiple plots
    plot1=figure()
    plot1.circle(x,y1, size=20, color="red")

    plot2=figure()
    plot2.circle(x,y2, size=20, color="green")

    plot3=figure()
    plot3.circle(x,y3, size=20, color="yellow")

    plots=[plot0,plot1,plot2,plot3]

    script,div=components(plots)
    #Generating a js script and a html div to be rendered, out of the assigned data

    return render(request,'starter.html',{'script': script, 'div': div,'form':form})
