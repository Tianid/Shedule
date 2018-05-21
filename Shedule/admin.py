from django.contrib import admin

# Register your models here.
from Shedule.models import*


admin.site.register(LessonNumber)
admin.site.register(ParityOdd)
admin.site.register(Teacher)
admin.site.register(Subject)
admin.site.register(DayOfTheWeek)
admin.site.register(Groups)
admin.site.register(DayGroupsSubject)