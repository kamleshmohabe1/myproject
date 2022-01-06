from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.conf import settings
from . import models
from django.views.decorators.csrf import csrf_exempt
import time

curl=settings.CURRENT_URL
media_url=settings.MEDIA_URL

def home(request):
	query="select * from addcat"
	models.cursor.execute(query)
	clist=models.cursor.fetchall()
	return render(request,'index.html',{'curl':curl,'media_url':media_url,'clist':clist})

def viewsubcat(request):
	query1="select * from addcat"
	models.cursor.execute(query1)
	clist=models.cursor.fetchall()

	cnm=request.GET.get('cnm')
	query="select * from addsubcat where catnm='%s' " %(cnm)
	models.cursor.execute(query)
	sclist=models.cursor.fetchall()
	return render(request,'viewsubcat.html',{'curl':curl,'media_url':media_url,'sclist':sclist,'clist':clist,'cnm':cnm})
	
def viewfoodproduct(request):
	query1="select * from addsubcat"
	models.cursor.execute(query1)
	sclist=models.cursor.fetchall()	

	scnm=request.GET.get('scnm')
	sprice=request.GET.get('sprice')
	eprice=request.GET.get('eprice')
	
	if sprice==None: 
		query="select * from foodproduct where subcatnm='%s' " %(scnm)
	else:
		query="select * from foodproduct where subcatnm='%s' and price between %s and %s" %(scnm,int(sprice),int(eprice))	
	
	models.cursor.execute(query)
	fplist=models.cursor.fetchall()
	return render(request,'viewfoodproduct.html',{'curl':curl,'media_url':media_url,'fplist':fplist,'sclist':sclist,'scnm':scnm,'total':len(fplist)})	
	
def about(request):
	return render(request,'about.html',{'curl':curl})
	
def contact(request):
	return render(request,'contact.html',{'curl':curl})
	
def service(request):
	return render(request,'service.html',{'curl':curl})
	
def register(request):
	if request.method=="GET":
		return render(request,'register.html',{'curl':curl,'output':''})
	else:
		name=request.POST.get('name')
		email=request.POST.get('email')
		password=request.POST.get('password')
		mobile=request.POST.get('mobile')
		address=request.POST.get('address')
		city=request.POST.get('city')
		gender=request.POST.get('gender')
		dt=time.asctime(time.localtime(time.time()))
		
		query="insert into register values(NULL,'%s','%s','%s','%s','%s','%s','%s','user',0,'%s')"	%(name,email,password,mobile,address,city,gender,dt)
		
		models.cursor.execute(query)
		models.db.commit()
		
		
		
		import smtplib 
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
	
		me = "kamleshmohabe1993@gmail.com"
		you = email

		msg = MIMEMultipart('alternative')
		msg['Subject'] = "Verification Mail BookMyMeal"
		msg['From'] = me
		msg['To'] = you

		html = """<html>
  					<head></head>
  					<body>
    					<h1>Welcome to BookMyMeal</h1>
    					<p>You have successfully registered , please click on the link below to verify your account</p>
    					<h2>Username : """+email+"""</h2>
    					<h2>Password : """+str(password)+"""</h2>
<br><br>
<a href='http://localhost:8000/verifyuser/?email="""+email+"""'>Click here to verfy your account</a>    						
  					</body>
				</html>
				"""
	
		s = smtplib.SMTP('smtp.gmail.com', 587)
		s.ehlo() 
		s.starttls() 
		s.login("kamleshmohabe1993@gmail.com", "Kam#1993") 
	
		part2 = MIMEText(html, 'html')

		msg.attach(part2)
	
		s.sendmail(me,you, str(msg)) 
		s.quit() 
		print("mail send successfully....")
		
		
		
		
		return render(request,'register.html',{'curl':curl,'output':'Register successfully....'})	


def verifyuser(request):
	email=request.GET.get('email')
	query="update register set status=1 where email='%s'" %(email)
	models.cursor.execute(query)
	models.db.commit()
	print("User Account Verified Successfully")
	return redirect(curl+'login/')


@csrf_exempt	
def login(request):
	if request.method=="GET":
		return render(request,'login.html',{'curl':curl,'output':''})					
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		
		query="select * from register where email='%s' and password='%s' and status=1 " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		
		if len(userDetails)>0:
			if userDetails[0][8]=="admin":
				response=redirect(curl+'myadmin/')
			else:	
				response=redirect(curl+'user/')
			response.set_cookie('cunm',email,3600*24)
			return response		
		else:
			return render(request,'login.html',{'curl':curl,'output':'Invalid user or verify your account'})	


@csrf_exempt	
def orderlogin(request):
	if request.method=="GET":
		pid=request.GET.get('pid')
		price=request.GET.get('price')
		return render(request,"orderlogin.html",{'curl':curl,'pid':pid,'price':price})	
	else:
		email=request.POST.get('email')
		password=request.POST.get('password')
		pid=request.POST.get('pid')
		price=request.POST.get('price')
		
		query="select * from register where email='%s' and password='%s' and status=1 " %(email,password)
		models.cursor.execute(query)
		userDetails=models.cursor.fetchall()
		
		
		if len(userDetails)>0:
			response=redirect(curl+'user/placeorder/?pid='+str(pid)+"&price="+str(price))
			response.set_cookie('cunm',email,3600*24)
			return response		
		else:
			return render(request,'orderlogin.html',{'curl':curl,'output':'Invalid user or verify your account to order product'})
	
	
def payment(request):
	pid=request.GET.get('pid')
	price=request.GET.get('price')
	uid=request.GET.get('uid')
	dt=time.asctime(time.localtime(time.time()))
	
	query="insert into payment values(NULL,%s,%s,'%s','%s')" %(int(pid),int(price),uid,dt)
	
	models.cursor.execute(query)
	models.db.commit()
	
	return redirect(curl+'success/')	
	
	
def success(request):
	return render(request,'success.html',{'curl':curl})	
	
def cancel(request):
	return render(request,'cancel.html',{'curl':curl})