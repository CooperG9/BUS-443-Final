from django.shortcuts import render
from django.http import HttpResponse
from finalapp.models import Studentdetails, Course
from django.db import connection
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
	cursor = connection.cursor()
	cursor.execute('SELECT COUNT(STUDENTID) FROM FINALAPP_STUDENTDETAILS')
	count = cursor.fetchall()
	cursor.execute('SELECT AVG(GPA) FROM FINALAPP_STUDENTDETAILS')
	avgpa = cursor.fetchall()
	cursor.execute("SELECT COUNT(YEAR) FROM FINALAPP_STUDENTDETAILS WHERE YEAR='Senior'")
	senior = cursor.fetchall()
	cursor.execute("SELECT COUNT(YEAR) FROM FINALAPP_STUDENTDETAILS WHERE YEAR='Junior'")
	junior = cursor.fetchall()
	cursor.execute("SELECT COUNT(YEAR) FROM FINALAPP_STUDENTDETAILS WHERE YEAR='Sophomore'")
	soph = cursor.fetchall()
	cursor.execute("SELECT COUNT(YEAR) FROM FINALAPP_STUDENTDETAILS WHERE YEAR='Freshman'")
	fresh = cursor.fetchall()
	cursor.execute('SELECT COUNT(COURSEID) FROM FINALAPP_COURSE')
	course = cursor.fetchall()
	context = {'count1':count, 'count2':avgpa, 'count3':senior, 'count4':junior, 'count5':soph, 'count6':fresh, 'count7':course}
	return render(request, 'finalapp/home.html', context)

def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

@login_required
def studentdetails(request):
#    cursor = connection.cursor()
#    cursor.execute('SELECT * FROM FINALAPP_STUDENTDETAILS')
#    student = dictfetchall(cursor)
    student = Studentdetails.objects.all()
    paginator = Paginator(student, 10)
    page = request.GET.get('page')
    studentdata = paginator.get_page(page)
#    print(student)
    return render(request, 'finalapp/studentdetails.html', {'data':studentdata})

@login_required
def coursedetails(request):
#    cursor = connection.cursor()
#    cursor.execute('SELECT * FROM FINALAPP_COURSE')
#    course = dictfetchall(cursor)
    course = Course.objects.all()
    paginator = Paginator(course, 10)
    page = request.GET.get('page')
    coursedata = paginator.get_page(page)
#    print(course)
    return render(request, 'finalapp/coursedetails.html', {'data':coursedata})

def enrollment(request):
	student = Studentdetails.objects.all()
	coursedata = Course.objects.all()
	if('sid' in request.GET and 'cname' not in request.GET):
		sid = request.GET.get('sid')
		return HttpResponse('Success')
	if('sid' in request.GET and 'cname' in request.GET):
		sid = request.GET.get('sid')
		cname = request.GET.get('cname')
	return render(request, 'finalapp/enrollment.html', {'studentid':student, 'coursetitle': coursedata})

