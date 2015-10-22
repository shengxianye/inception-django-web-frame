#coding=utf-8
from django.shortcuts import render,render_to_response,RequestContext
from django.http import HttpResponse,HttpResponseRedirect
from forms import InceptionTableStructure
from inception import table_structure 

def index(req):
    return render_to_response('index.html',)

def messages(req):
    return render_to_response('messages.html',)

def tasks(req):
    return render_to_response('tasks.html',)
	
def ui(req):
    return render_to_response('ui.html',)

def widgets(req):
    return render_to_response('widgets.html',)

def submenu(req):
    return render_to_response('submenu.html',)

def submenu2(req):
    return render_to_response('submenu2.html',)

def submenu3(req):
    return render_to_response('submenu3.html',)

def form(req):
    return render_to_response('form.html',)

def chart(req):
    return render_to_response('chart.html',)

def typography(req):
    return render_to_response('typography.html',)

def gallery(req):
    return render_to_response('gallery.html',)

def table(req):
    return render_to_response('table.html',)
	
def calendar(req):
    return render_to_response('calendar.html',)
	
def filemanager(req):
    return render_to_response('file-manager.html',)
	
def icon(req):
    return render_to_response('icon.html',)
	
def login(req):
    return render_to_response('login.html',)

def inception(request):
    if request.method == "POST":      
	form = InceptionTableStructure(request.POST)
        if form.is_valid():
            mysql_structure = form.cleaned_data['sql']
            ip = form.cleaned_data['ip']
            port = form.cleaned_data['port']
            dbname = form.cleaned_data['dbname']
	    sql_review = table_structure(mysql_structure,ip,port,dbname)     #调用inception.py中的table_structure函数 
            if sql_review == ['None']:
		sql_review = ['Successful']
            return render_to_response('inception.html',{'form':form,'sql_review':sql_review})
    else:
        form = InceptionTableStructure()
    return render_to_response('inception.html',{'form':form})     #must fill form


