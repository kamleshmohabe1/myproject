from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from . import models

curl=settings.CURRENT_URL

# Create your views here.

def adminhome(request):
	return render(request,'adminhome.html',{'curl':curl,'cunm':request.COOKIES.get('cunm')})
	
def viewusers(request):
	query="select * from register where role='user'"
	models.cursor.execute(query)
	userDetails=models.cursor.fetchall()
	return render(request,'viewusers.html',{'curl':curl,'userDetails':userDetails,'cunm':request.COOKIES.get('cunm')})
	
def manageuserstatus(request):
	regid=request.GET.get('regid')
	s=request.GET.get('s')
	
	if s=='block':
		query="update register set status=0 where regid=%s" %(regid)
	elif s=='unblock':
		query="update register set status=1 where regid=%s" %(regid)
	else:
		query="delete from register where regid=%s" %(regid)		

	models.cursor.execute(query)
	models.db.commit()
	return redirect(curl+'myadmin/viewusers/')

def addcat(request):
	if request.method=='GET':
		return render(request,'addcat.html',{'curl':curl,'output':'','cunm':request.COOKIES.get('cunm')})	
	else:
		catnm=request.POST.get('catnm')
		caticon=request.FILES['caticon']
		fs = FileSystemStorage()
		filename = fs.save(caticon.name,caticon)
		
		query="insert into addcat values(NULL,'%s','%s')" %(catnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addcat.html',{'curl':curl,'output':'Category Added Successfully','cunm':request.COOKIES.get('cunm')})	
		
		
def addsubcat(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()
	if request.method=='GET':
		return render(request,'addsubcat.html',{'curl':curl,'clist':clist,'output':'','cunm':request.COOKIES.get('cunm')})	
	else:
		catnm=request.POST.get('catnm')
		subcatnm=request.POST.get('subcatnm')
		subcaticon=request.FILES['subcaticon']
		fs = FileSystemStorage()
		filename = fs.save(subcaticon.name,subcaticon)
		
		query="insert into addsubcat values(NULL,'%s','%s','%s')" %(subcatnm,catnm,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addsubcat.html',{'curl':curl,'clist':clist,'output':'Sub Category Added Successfully','cunm':request.COOKIES.get('cunm')})			



def addfoodproduct(request):
	query1="select * from addsubcat"
	models.cursor.execute(query1)
	sclist=models.cursor.fetchall()
	if request.method=='GET':
		return render(request,'addfoodproduct.html',{'curl':curl,'sclist':sclist,'output':'','cunm':request.COOKIES.get('cunm')})	
	else:
		title=request.POST.get('title')
		subcatnm=request.POST.get('subcatnm')
		description=request.POST.get('description')
		price=request.POST.get('price')
		foodicon=request.FILES['foodicon']
		fs = FileSystemStorage()
		filename = fs.save(foodicon.name,foodicon)
		
		query="insert into foodproduct values(NULL,'%s','%s','%s',%s,'%s')" %(title,subcatnm,description,price,filename)
		models.cursor.execute(query)
		models.db.commit()
		return render(request,'addfoodproduct.html',{'curl':curl,'sclist':sclist,'output':'Food Product Added Successfully','cunm':request.COOKIES.get('cunm')})

def orderpaymentlistadmin(request):
	cunm=request.COOKIES.get('cunm')
	query="select * from payment"
	models.cursor.execute(query)
	orderlist=models.cursor.fetchall()
	return render(request,'orderpaymentlistadmin.html',{'curl':curl,'cunm':cunm,'orderlist':orderlist})
	
def changepasswordadmin(request):
	cunm=request.COOKIES.get('cunm')
	if request.method=="GET":
		return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':cunm,'output':''})	
	else:
		opass=request.POST.get('opass')
		npass=request.POST.get('npass')
		cnpass=request.POST.get('cnpass')	
		
		query="select * from register where email='%s' and password='%s' " %(cunm,opass)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		if len(userDetails)>0:
			if npass==cnpass:
				query1="update register set password='%s' where email='%s'" %(npass,cunm)
				models.cursor.execute(query1)
				models.db.commit()
				return redirect(curl+'login/')
			else:	
				return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'New and Confirm New password miss match'})
		else:
			return render(request,'changepasswordadmin.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'Invalid old password, please try again'})	
		




	
	
	
	
	
		
