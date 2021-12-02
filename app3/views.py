from django.http import request,JsonResponse
from django.shortcuts import render
from . models import *
from random import random
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def fnOne(req):
    return render(req,'smpl.html')
def fnregistration(req):
    try:
        name=req.POST['fname']
        print(name)
        objnm=student.objects.filter(Name=name).exists()
        if objnm==False:
            age=req.POST['age']
            print(age)
            date=req.POST['date']
            print(date)
            place=req.POST['place']
            print(place)
            uname=req.POST['uname']
            print(uname)
            pword=req.POST['pw']
            print(pword)
            stdobj=student(Name=name,Age=age,DOJ=date,Place=place,Username=uname,Password=pword)
            stdobj.save()
    except Exception as e:
        print(e)
    return render(req,'Registration.html')
def fnstd(req):
    try:
        if req.method=='POST':
            uname2=req.POST['un']
            print(uname2)
            lpword=req.POST['lpw']
            print(lpword)
            lstd=student.objects.get(Username=uname2,Password=lpword)
            print(lstd.Username)
            req.session['ses']=lstd.id
            print(req.session['ses'])
            return render(req,'students.html')
    except Exception as e:
        print(e)
    return render(req,'Registration.html',{'msg':'Incorrect Username or Password'})
def pword(req):
    try:
        oldp=req.POST['opw']
        print(oldp)
        newp=req.POST['npw']
        print(newp)
        uid=req.session['ses']
        uobj=student.objects.get(id=uid)
        print(uobj.Password)
        if uobj.Password==oldp:
            uobj.Password=newp
            uobj.save()
            print("Hai")
            return render(req,'password.html',{'msg2':'Password changed successfully'})
        return render(req,'password.html',{'msg2':'Password does not match'})
    except Exception as e:
        print(e)
    return render(req,'password.html')
def fnlogout(req):
    del req.session['ses']
    return render(req,'Registration.html')
def fnfile(req):
    if req.method=='POST':
        name=req.POST['name']
        print(name)
        file=req.FILES['files']
        print(file)
        file_name=str(random())+file.name
        print(file_name)
        objfile=FileSystemStorage()
        objfile.save(file_name,file)
        obj2=up_file(Name=name,Filename=file_name)
        obj2.save()
    f_obj=up_file.objects.all()
    return render(req,'file.html',{"img":f_obj})
def fnajax(req):
    if req.method=='POST':
            uname=req.POST['name1']
            print(uname)
            uadrs=req.POST['add1']
            print(uadrs)
            umail=req.POST['mail1']
            print(umail)
            objajax=ajax(Name=uname,Address=uadrs,E_mail=umail)
            objajax.save()
            return JsonResponse({'msg':'Saved Successfully'})
    return render(req,'ajax.html')
def fnedit(req):
    try:
        if req.method=='POST':
            aj_id=req.POST['id']
            print(aj_id)
            ajobj=ajax.objects.get(id=aj_id)
            print(ajobj.id)
            ajobj2=[{'id':ajobj.id,'Name':ajobj.Name,'Address':ajobj.Address,'Email':ajobj.E_mail}]
            return JsonResponse({'get_details':ajobj2})
    except Exception as e:
        print(e)
    return render(req,'ajax.html')
@api_view(['GET'])
def fndrf(req):
    msg="Hello"
    return Response(msg)
@api_view(['POST'])
def fnpost(req):
    name=req.data['name1']
    address=req.data['add1']
    mail=req.data['mail1']
    objapi=ajax(Name=name,Address=address,E_mail=mail)
    objapi.save()
    return Response({'msg2':'Saved Successfully'})
@api_view(['DELETE'])
def delapi(req):
    apiid=req.data['id']
    ajax.objects.get(id=apiid).delete()
    return Response({'msg2':'Deleted Successfully'})
def fupdate(req):
    if req.method=='POST':
        uid=req.POST['uid1']
        print(uid)
        uname=req.POST['uname1']
        print(uname)
        uadrs=req.POST['uadrs1']
        print(uadrs)
        umail=req.POST['uemail1']
        print(umail)
        ajax.objects.filter(id=uid).update(Name=uname,Address=uadrs,E_mail=umail)
        # objupdt=ajax(Name=uname,Address=uadrs,E_mail=umail)
        # objupdt.save()
        return JsonResponse({'msg2':'Update Successfully'})
def fnprof(req):
    return render(req,'registration/profile.html')
def fndelete(req):
    if req.method=='POST':
        uid=req.POST['id']
        delobj=ajax.objects.get(id=uid)
        delobj.delete()
        return JsonResponse({'msg3':'Deleted'})
def fnajx(req):
    objtbl=ajax.objects.all()
    objx=[{'ID':i.id,'Name':i.Name,'Address':i.Address,'E_mail':i.E_mail}for i in objtbl]
    return JsonResponse({'ajx':objx})



        # print(oldp)
        # cpw=student.objects.get(Password=oldp)
        # print(cpw.Password)
        # old2=req.POST['opw']
        # print(old2)
        # if oldp==old2:
        #     npw=req.POST['npw']
        #     print(npw)
        #     rnpw=req.POST['rnpw']
        #     print(rnpw)



    # try:
    #     if req.method=='POST':
    #         mail=req.POST['mail']
    #         print(mail)
    #         lgpw=req.POST['lgpw']
    #         print(lgpw)
    #         userobj=facebook.objects.get(Mobile_Email=mail,Password=lgpw)
    #         print(userobj.Mobile_Email)
    #         req.session['ses']=userobj.id
    #         print(req.session['ses'])
    #         return render(req,'loginhome.html',{'usr':userobj})
    # except Exception as e:
    #     print(e)
