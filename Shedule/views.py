from django.core import exceptions
from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse
# from django.shortcuts import render_to_response
# from django.http import Http404
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.

def query (request):
    if request.method == "POST":
        print("yeah!!!!")
    from django.db import connection,transaction
    # posts = LessonNumber.objects.raw('select * from lesson_number')
    # posts = LessonNumber.objects.raw('select * from lesson_number')
    # posts1 = DayOfTheWeek.objects.raw('select * from day_of_the_week')
    # posts2 = DayGroupsSubject.objects.raw('select * from day_groups_subject')

    # posts = DayOfTheWeek.objects.all()
    # print(posts.query)
    # posts = LessonNumbers.objects.filter(lesson_number=3)
    # print(posts)
    # return render(request,'Shedule/query.html',{'posts':posts,'kek':posts1,'kek2':posts2})
    groups = Groups.objects.raw('select id,group_cipher from groups ')
    day_number = DayOfTheWeek.objects.raw('select day_number,name from day_of_the_week')
    subject = Subject.objects.raw('select id,subject_name from subject')
    # subjects = Subject.objects.raw('select id,subject_name,lesson_type from subject')



    return render(request, 'Shedule/query.html', {'groups':groups, 'day_number':day_number, 'subject':subject})


def get_sql1(request):
    str = 'where'

    list=[]
    keys=["date","fk_day_number","fk_lesson_number","fk_group_cipher"]
    dict={}

    print(request.POST)
    for i in request.POST:
        if i == 'csrfmiddlewaretoken':
            continue
        list.append(request.POST[i])


    for i in range(len(keys)):
        dict.update({keys[i]:list[i]})

    for i in dict:
        if dict.get(i) != "":

            if len(str)==5:
                str+="\t"+i+" "+"="+" "+"'{}'".format(dict.get(i))


            else:
                str+=" and "+i+" "+"="+" "+"'{}'".format( dict.get(i))

    # str2 = "and fk_subject_cipher = (select teacher.id,teacher.name,teacher.surname,teacher.middle_name from teacher where id = fk_subject_cipher )"
    str2 = "and fk_subject_cipher = subject.id and teacher.id = subject.fk_teacher  "


    if len(str) > 5:
        query = DayGroupsSubject.objects.raw('select day_groups_subject.id,teacher.id,fk_subject_cipher,name,surname,middle_name from day_groups_subject,teacher,subject  {} {} order by fk_day_number,fk_lesson_number'.format(
                str, str2))

        return render(request, 'Shedule/SQL-answer.html', {'query1_1': query})
    else:
        # query = DayGroupsSubject.objects.all().order_by('fk_day_number','fk_lesson_number')
        str1 = "where fk_subject_cipher = subject.id and teacher.id = subject.fk_teacher "
        query = DayGroupsSubject.objects.raw('select day_groups_subject.id,fk_subject_cipher,fk_lesson_number,fk_day_number,fk_group_cipher,name,surname,middle_name from day_groups_subject,subject,teacher {}'.format(str1))

        return render(request,'Shedule/SQL-answer.html',{'query1_2':query})


    # {'query': query}
    # return render(request,'Shedule/test.html',{'query4':query4})

def get_sql2(request):


    list = []
    # keys = ["fk_subject_cipher", "fk_group_cipher"]
    # dict = {}

    for i in request.POST:
        if i == 'csrfmiddlewaretoken':
            continue
        list.append(request.POST[i])
    if list[0]=="" or list[1]=="":
        error = "Wrong query!"
        return render(request,'Shedule/SQL-answer.html',{'error_for_query2':error})
    else:
        str1 = "fk_subject_cipher = (select id from subject where id = {}) and fk_group_cipher = {}".format(list[0], list[1])
        str2 = "and fk_subject_cipher = subject.id and teacher.id = subject.fk_teacher "
        query = DayGroupsSubject.objects.raw('select day_groups_subject.id,date,fk_subject_cipher,fk_lesson_number,name,surname,middle_name from day_groups_subject,subject,teacher where {} {}order by fk_lesson_number'.format(str1,str2))
        return render(request,'Shedule/SQL-answer.html',{'query2':query})

def get_sql3(request):
    list = []
    dict = {}
    keys = ["surname","name", "middle_name"]

    str = "where"
    for i in request.POST:
        if i == 'csrfmiddlewaretoken':
            continue
        list.append(deff(request.POST[i]))
    for i in list:
        if i == "Invalid input data":
            error = "Invalid query!"
            return render(request, 'Shedule/SQL-answer.html', {'error_for_query3': error})


    for i in range(len(keys)):
        dict.update({keys[i]:list[i]})


    for i in dict:
        if dict.get(i) != "":
            if len(str)==5:
                str += "\t" + i + " " + "=" + " " + "'{}'".format(dict.get(i))
            else:
                str+=" and "+i+" "+"="+" "+"'{}'".format( dict.get(i))

    print(str)
    if len(str) > 5:
        query = Subject.objects.raw('select subject.id,name,surname,middle_name,position,rank,academic_degree,department,election_date,personal_number from teacher,subject {} and teacher.id = subject.fk_teacher'.format(str))
        print(query.query)
        return render(request,'Shedule/SQL-answer.html',{'query3':query})
    else:
        error = "Invalid query!"
        return render(request,'Shedule/SQL-answer.html',{'error_for_query3':error})



def deff(value):
    str= value
    str2=""
    str = str.strip()


    if len(str) > 100 :
        error = "Invalid input data"
        return error

    for i in str:
        j=ord(i)
        if  (j >= 1040 and j<= 1103)  or (j == 45) or (j == 32):
            str2+=i
        else:
            error = "Invalid input data"
            return error

    return str2

# =================================== GROUPS VIEW ===================================
def groups_news(request):

    if request.method == "POST":
            form = GroupsForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)
                post.save()
                answer = "Saved!"
                # return render(request,'Shedule/groups_edit.html',{'form':form,'answer':answer})
                return redirect('groups_detail')

    else:
        form = GroupsForm()
        return render(request, 'Shedule/groups_edit.html', {'form': form})

def groups_detail(request):
    post = Groups.objects.all()
    return render(request,'Shedule/groups_detail.html',{'post':post})

def groups_edit(request, pk):
    post = get_object_or_404(Groups,pk=pk )

    if request.method == "POST":

        form = GroupsForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('groups_detail')
    else:

        form = GroupsForm(instance=post)
    return render(request, 'Shedule/groups_edit.html', {'form': form})

def groups_del(request,pk):
    Groups.objects.filter(id=pk).delete()
    # post.objects.raw('delete from groups where id = pk')

    return redirect('groups_detail')

# =================================== TEACHER VIEW ===================================

def teacher_news(request):
    if request.method == "POST":
            form = TeacherForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)
                post.save()
                answer = "Saved!"
                # return render(request,'Shedule/groups_edit.html',{'form':form,'answer':answer})
                return redirect('teacher_detail')

    else:
        form = TeacherForm()
        return render(request, 'Shedule/teacher_edit.html', {'form': form})


def teacher_detail(request):
    post = Teacher.objects.all()
    return render(request,'Shedule/teacher_detail.html',{'post':post})

def teacher_edit(request, pk):
    post = get_object_or_404(Teacher,pk=pk )

    if request.method == "POST":

        form = TeacherForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('teacher_detail')
    else:

        form = TeacherForm(instance=post)
    return render(request, 'Shedule/teacher_edit.html', {'form': form})

def teacher_del(request,pk):

    Teacher.objects.filter(id=pk).delete()

    return redirect('teacher_detail')



# =================================== SUBJECT VIEW ===================================


def subject_news(request):
    if request.method == "POST":
            form = SubjectForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)
                post.save()
                answer = "Saved!"
                # return render(request,'Shedule/groups_edit.html',{'form':form,'answer':answer})
                return redirect('subject_detail')

    else:
        form = SubjectForm()
        return render(request, 'Shedule/subject_edit.html', {'form': form})


def subject_detail(request):
    post = Subject.objects.all()
    return render(request,'Shedule/subject_detail.html',{'post':post})

def subject_edit(request, pk):
    post = get_object_or_404(Subject,pk=pk )

    if request.method == "POST":

        form = SubjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('subject_detail')
    else:

        form = SubjectForm(instance=post)
    return render(request, 'Shedule/subject_edit.html', {'form': form})

def subject_del(request,pk):
    Subject.objects.filter(id=pk).delete()

    return redirect('subject_detail')


# =================================== DAY/GROUPS/SUBJECT VIEW ===================================

def dgs_news(request):
    if request.method == "POST":
            form = DayGroupsSubjectForm(request.POST)
            if form.is_valid():

                post = form.save(commit=False)
                post.save()
                answer = "Saved!"
                # return render(request,'Shedule/groups_edit.html',{'form':form,'answer':answer})
                return redirect('dgs_detail')

    else:
        form = DayGroupsSubjectForm()
        return render(request, 'Shedule/dgs_edit.html', {'form': form})


def dgs_detail(request):
    post = DayGroupsSubject.objects.all()
    return render(request,'Shedule/dgs_detail.html',{'post':post})

def dgs_edit(request, pk):
    post = get_object_or_404(DayGroupsSubject,pk=pk )

    if request.method == "POST":

        form = DayGroupsSubjectForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('dgs_detail')
    else:

        form = DayGroupsSubjectForm(instance=post)
    return render(request, 'Shedule/dgs_edit.html', {'form': form})

def dgs_del(request,pk):
    DayGroupsSubject.objects.filter(id=pk).delete()

    return redirect('dgs_detail')

# ===============================================================================================
def main (request):
    return render(request,'Shedule/main.html',{})

