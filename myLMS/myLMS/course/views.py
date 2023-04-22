from django.shortcuts import render
from course.models import Department,Course
from django.http import HttpResponse


# Create your views here.
def vw_course_list(request):
    class course:
        def __init__(self, code, title):
            self.Code = code
            self.Title = title


    course_obj_lst = []

    lst_code_title = ["c001", "fullstack", "c002", "front-end", "c003", "data base"]
    z = 0
    for num in range(3):
        i = z
        course_obj = course(lst_code_title[i], lst_code_title[i + 1])
        z = i + 2
        course_obj_lst.append(course_obj)

    return render(request, "course_list.html", {"course_list": course_obj_lst})

def vw_course_register(request):
    class Person:
        def __init__(self, name, city):
            self.Name = name
            self.City = city

    person_obj = Person("Ali", "Tehran")
    

    return render(request, "course_register.html",{"welcome": person_obj})

def vw_department_list(request):
    db_department_lst = Department.objects.all()
    db_department_lst_filter = Department.objects.filter(location = "3rd")
    return render(request, "department_list.html", {"department_list": db_department_lst, "department_list_filter": db_department_lst_filter})

def vw_department_info(request, dept_code):
    department_code = Department.objects.get(code = dept_code)
    department_course_lst = Course.objects.filter(department = department_code.id)
    return render(request,"department_info.html",{"department_obj": department_code, "related_course_list": department_course_lst})
    #return HttpResponse("<h1>"+code+"</h1>")
    

def vw_course_dept_list(request,dept_code, dept_title):

    department_title = Department.objects.get(code = dept_code)

    department_related_course_lst = Course.objects.filter(department = department_title.id)

    return render(request,"course_list.html",{"related_course_list": department_related_course_lst, "department_title_obj":department_title})
