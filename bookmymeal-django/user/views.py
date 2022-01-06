from django.shortcuts import render,redirect
from django.conf import settings
from . import models


curl=settings.CURRENT_URL

# Create your views here.

def userhome(request):
	return render(request,'userhome.html',{'curl':curl,'cunm':request.COOKIES.get('cunm')})
	
def placeorder(request):
	PAYPAL_URL="https://www.sandbox.paypal.com/cgi-bin/webscr"
	PAYPAL_ID="divyeshpandya2000-myseller@gmail.com"
	return render(request,'placeorder.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'pid':request.GET.get('pid'),'price':request.GET.get('price'),'PAYPAL_URL':PAYPAL_URL,'PAYPAL_ID':PAYPAL_ID})	
		
def orderpaymentlist(request):	
	cunm=request.COOKIES.get('cunm')
	query="select * from payment where uid='%s' " %(cunm)
	models.cursor.execute(query)
	orderlist=models.cursor.fetchall()
	return render(request,'orderpaymentlist.html',{'curl':curl,'cunm':cunm,'orderlist':orderlist})
	
def changepassworduser(request):
	cunm=request.COOKIES.get('cunm')
	if request.method=="GET":
		return render(request,'changepassworduser.html',{'curl':curl,'cunm':cunm,'output':''})	
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
				return render(request,'changepassworduser.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'New and Confirm New password miss match'})
		else:
			return render(request,'changepassworduser.html',{'curl':curl,'cunm':request.COOKIES.get('cunm'),'output':'Invalid old password, please try again'})

def editprofileuser(request):
	cunm=request.COOKIES.get('cunm')
	
	if request.method=="GET":
		query="select * from register where email='%s'" %(cunm)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchone()
	
		m=''
		f=''
		if userDetails[7]=='male':
			m='checked'
		if userDetails[7]=='female':
			f='checked'	
		return render(request,'editprofileuser.html',{'curl':curl,'cunm':cunm,'userDetails':userDetails,'f':f,'m':m,'output':''})		
	else:
		name=request.POST.get('name')
		email=request.POST.get('email')
		mobile=request.POST.get('mobile')
		address=request.POST.get('address')
		city=request.POST.get('city')
		gender=request.POST.get('gender')
		
		query="update register set name='%s' , mobile='%s' , address='%s' , city='%s' , gender='%s' where email='%s' "	%(name,mobile,address,city,gender,email)
		
		models.cursor.execute(query)
		models.db.commit()		
		return redirect(curl+'user/editprofileuser/')	
	
	
	
	
	
	
	
