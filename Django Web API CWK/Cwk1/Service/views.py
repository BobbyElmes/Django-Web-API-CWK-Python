from django.shortcuts import render
from django.http import HttpResponse
from Service.models import Module
from Service.models import Users
from Service.models import Rating
from django.views.decorators.csrf import csrf_exempt
from decimal import *
# Create your views here.from decimal import *

#Called when the client accesses the /api/list api
##returns a string listing all instances of modules
def HandleListRequest(request):
    s = "Code           Name                               Year           Semester       Taught by"
    module_list = Module.objects.all();
    idList = []
    s += '\n'
    for e in module_list:
        if([e.moduleID,e.year,e.semester] not in idList):
            x = Module.objects.filter(moduleID = e.moduleID, year = e.year, semester = e.semester)
            s += e.moduleID
            for i in range(0,(15-len(e.moduleID))):
                s+=" "
            s+= e.moduleName
            for i in range(0,(35-len(e.moduleName))):
                s+=" "
            s+= e.year
            for i in range(0,(15-len(e.year))):
                s+=" "
            s+= e.semester
            for i in range(0,(15-len(e.semester))):
                s+=" "
            count = 0
            for c in x:
                if (count > 0):
                    for i in range(0,80):
                        s+= " "
                s+= c.professorID + " , " + c.professorName
                s += '\n'
                count +=1

            for i in range(0,110):
                s+= "-"
            s += '\n'
            idList.append([e.moduleID, e.year, e.semester])
    return HttpResponse("%s" %s)

#Allows the user to register
@csrf_exempt
def HandleRegisterRequest(request):
    s = ""
    if request.method == 'POST':
        print("HI")
        print(request.POST['username'])
        if 'username' in request.POST:
            if 'userPassword' in request.POST:
                if 'userEmail' in request.POST:
                    #newUser = Users(userName = 'bob', email = 'bob', password = 'bob')
                    newUser = Users(userName = request.POST['username'], email = request.POST['userEmail'], password = request.POST['userPassword'])
                    newUser.save();
                    s = "New user: " + request.POST['username'] + " is registered"
                    print("HI")
    if(len(s) == 0):
        s = "invalid post request"
    return HttpResponse(s)

#Checks username and password against the database
@csrf_exempt
def HandleLoginRequest(request):
    s = ""
    try:
        user = Users.objects.get(userName =request.GET['username'], password = request.GET['password'])
        s = "User: " + user.userName + " signed in"
    except:
        s = "Incorrect username or password"
    if(len(s) == 0):
        s = 'invalid request'
    return HttpResponse(s)

#Works out professor average in selected module
def HandleAverageRequest(request):
    s = ""
    values = Module.objects.filter(professorID=request.GET['professorID'], moduleID = request.GET['moduleID'])
    total = 0
    count = 0
    for x in values:
        ratings = Rating.objects.filter(moduleID=x.moduleID, professorID=x.professorID, year=x.year,semester = x.semester)
        for rating in ratings:
            total += int(rating.rating)
            print(rating.rating)
            count += 1
        profname = x.professorName
        modulename = x.moduleName
    if(count > 0):
        print(total/count)
        average = Decimal(total/count).quantize(Decimal('1.'), rounding = ROUND_HALF_UP)
        s = "The average rating for " + profname + " (" + request.GET['professorID'] + ") in module " + modulename + " (" + request.GET['moduleID'] + ") is: " + str(average)
    else:
        s ="There are no ratings for " + profname + " (" + request.GET['professorID'] + ") in module " + modulename + " (" + request.GET['moduleID' + ")"]
    return HttpResponse(s)

#adds user rating to database
@csrf_exempt
def HandleRateRequest(request):
    s = ""
    if request.method == 'POST':
        if "userName" in request.POST:
            if 'professorID' in request.POST:
                if 'moduleID' in request.POST:
                    if 'year' in request.POST:
                        if 'semester' in request.POST:
                            if 'rating' in request.POST:
                                print("HELLO")
                                newRating = Rating(userName = request.POST["userName"],
                                moduleID = request.POST["moduleID"],
                                professorID = request.POST["professorID"], year = request.POST["year"],
                                semester = request.POST["semester"], rating = request.POST["rating"])
                                print(newRating)
                                newRating.save()
                                s = "Rating of: " + request.POST["rating"] + " added"
    if(len(s) == 0):
        s = "invalid post request"
    return HttpResponse(s)

#returns string of average ratings for each professor
def HandleViewRequest(request):
    s = ""
    values = Rating.objects.all()
    ProfList = []

    for x in values:
        if(x.professorID not in ProfList):
            ProfList.append(x.professorID)
            ratings = Rating.objects.filter(professorID = x.professorID)
            total = 0
            count = 0
            for r in ratings:
                total += int(r.rating)
                count += 1
            m = Module.objects.filter(professorID = x.professorID)
            for i in m:
                profname = i.professorName
            average = Decimal(total/count).quantize(Decimal('1.'), rounding = ROUND_HALF_UP)
            if(count != 0):
                s += "The rating of " + profname + " (" + x.professorID + ") is: " + str(average)
                s += '\n'
    return HttpResponse(s)
