from django.shortcuts import render, redirect

def index1(request):
    return render(request,'form_page.html')

def index2(request):
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['language']=request.POST['language']
    request.session['comment']=request.POST['comment']
    request.session['gender']=request.POST['gender']
    request.session['education']=request.POST['education']
    return redirect('/redirect')  ###THIS MIGHT BE WRONG

def index3(request):
    # context = {
    #     'name':request.POST['name'],
    #     'location':request.POST['location'],
    #     'language':request.POST['language'],
    #     'comment':request.POST['comment'],
    #     'gender':request.POST['gender'],
    #     'education':request.POST['education'],
    # }
    return render(request,'result_page.html')

