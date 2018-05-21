from django import forms

from .models import *

class GroupsForm(forms.ModelForm):

    class Meta:
        model = Groups
        fields = ('group_cipher', 'students_count','direction','course')


class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = (
        'personal_number', 'name', 'surname', 'middle_name', 'rank', 'academic_degree', 'position', 'election_date',
        'department')

class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = ('subject_cipher','lesson_type','lecture_hall','subject_name','fk_teacher')

class DayGroupsSubjectForm(forms.ModelForm):

    class Meta:
        model = DayGroupsSubject
        fields = ('fk_day_number','fk_group_cipher','fk_lesson_number','fk_parity_odd','fk_subject_cipher','date')

