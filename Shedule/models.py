# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DayGroupsSubject(models.Model):
    fk_day_number = models.ForeignKey('DayOfTheWeek', models.DO_NOTHING, db_column='fk_day_number')
    fk_group_cipher = models.ForeignKey('Groups', models.DO_NOTHING, db_column='fk_group_cipher')
    fk_lesson_number = models.ForeignKey('LessonNumber', models.DO_NOTHING, db_column='fk_lesson_number')
    fk_parity_odd = models.ForeignKey('ParityOdd', models.DO_NOTHING, db_column='fk_parity_odd')
    fk_subject_cipher = models.ForeignKey('Subject', models.DO_NOTHING, db_column='fk_subject_cipher')
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'day_groups_subject'
        verbose_name_plural = 'Day/Groups/Subject'

    def __str__(self):
        return '|{}|    |{}|    |{}|    |{}|'.format(self.fk_day_number,self.fk_group_cipher,self.fk_lesson_number,self.fk_parity_odd,self.fk_subject_cipher,self.date)


class DayOfTheWeek(models.Model):
    day_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'day_of_the_week'
        verbose_name_plural = 'Day of the week'

    def __str__(self):
        return '{}'.format(self.name)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groups(models.Model):
    group_cipher = models.CharField(max_length=50)
    students_count = models.IntegerField()
    direction = models.CharField(max_length=100)
    course = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'
        verbose_name_plural = 'Groups'

    def __str__(self):
        return '{}'.format(self.group_cipher)


class LessonNumber(models.Model):
    lesson_number = models.AutoField(primary_key=True)
    lesson_begin = models.TimeField()
    lesson_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'lesson_number'
        verbose_name_plural = 'Leeson number'

    def __str__(self):
        return '{}'.format(self.lesson_number)


class ParityOdd(models.Model):
    id_number = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'parity_odd'
        verbose_name_plural = 'Parity - odd'

    def __str__(self):
        return '{}'.format(self.state)


class Subject(models.Model):
    subject_cipher = models.CharField(max_length=50)
    lesson_type = models.CharField(max_length=75)
    lecture_hall = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    fk_teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='fk_teacher')

    class Meta:
        managed = False
        db_table = 'subject'
        verbose_name_plural = 'Subject'

    def __str__(self):
        return '{} {}'.format(self.subject_name,self.lesson_type)


class Teacher(models.Model):
    personal_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    election_date = models.DateField()
    department = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'
        verbose_name_plural = 'Teacher'

    def __str__(self):
        return '{} {} {}'.format(self.surname,self.name,self.middle_name)




'''
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DayGroupsSubject(models.Model):
    id_day_groups_subject = models.AutoField(primary_key=True)
    fk_day_number = models.IntegerField()
    fk_groups_cipher = models.IntegerField()
    fk_subject_cipher = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_groups_subject'

    def __str__(self):
        return 'id: {}'.format(self.id_day_groups_subject)


class DayOfTheWeek(models.Model):
    day_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'day_of_the_week'

    def __str__(self):
        return 'day : {}'.format(self.name)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groups(models.Model):
    group_cipher = models.CharField(max_length=50)
    students_count = models.IntegerField()
    direction = models.CharField(max_length=100)
    course = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'

    def __str__(self):
        return 'group cipher: {}'.format(self.group_cipher)


class LessonNumber(models.Model):
    lesson_number = models.AutoField(primary_key=True)
    lesson_begin = models.TimeField()
    lesson_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'lesson_number'

    def __str__(self):
        return 'lesson number: {}'.format(self.lesson_number)


class ParityOdd(models.Model):
    id_number = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'parity_odd'

    def __str__(self):
        return 'state: {}'.format(self.state)


class Subject(models.Model):
    subject_cipher = models.CharField(max_length=50)
    lesson_type = models.CharField(max_length=75)
    lecture_hall = models.CharField(max_length=10)
    date = models.DateField()
    subject_name = models.CharField(max_length=100)
    fk_lesson_number = models.ForeignKey(LessonNumber, models.DO_NOTHING, db_column='fk_lesson_number')
    fk_parity_odd = models.ForeignKey(ParityOdd, models.DO_NOTHING, db_column='fk_parity_odd')
    fk_personal_number = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='fk_personal_number')

    class Meta:
        managed = False
        db_table = 'subject'

    def __str__(self):
        return 'subject number: {}'.format(self.subject_name)


class Teacher(models.Model):
    personal_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    election_date = models.DateField()
    department = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'

    def __str__(self):
        return 'surname: {}'.format(self.surname)
'''

'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DayGroupsSubject(models.Model):
    id_day_groups_subject = models.AutoField(primary_key=True)
    fk_day_number = models.IntegerField()
    fk_groups_cipher = models.IntegerField()
    fk_subject_cipher = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'day_groups_subject'
        verbose_name_plural = "Day/Group/Subject"

    def __str__(self):
        return 'id: {}'.format(self.id_day_groups_subject)


class DayOfTheWeek(models.Model):
    day_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'day_of_the_week'
        verbose_name_plural = "Day of the week"

    def __str__(self):
        return 'day : {}'.format(self.name)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groups(models.Model):
    group_cipher = models.CharField(max_length=50)
    students_count = models.IntegerField()
    direction = models.CharField(max_length=100)
    course = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'
        verbose_name_plural = "Groups"

    def __str__(self):
        return 'group cipher: {}'.format(self.group_cipher)


class LessonNumber(models.Model):
    lesson_number = models.AutoField(primary_key=True)
    lesson_begin = models.TimeField()
    lesson_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'lesson_number'
        verbose_name_plural = "Lesson Number"

    def __str__(self):
        return 'lesson number: {}'.format(self.lesson_number)


class ParityOdd(models.Model):
    id_number = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'parity_odd'
        verbose_name_plural = "Parity-odd"

    def __str__(self):
        return 'state: {}'.format(self.state)


class Subject(models.Model):
    subject_cipher = models.CharField(unique=True, max_length=50)
    lesson_type = models.CharField(max_length=75)
    lecture_hall = models.CharField(max_length=10)
    date = models.DateField()
    subject_name = models.CharField(max_length=100)
    fk_lesson_number = models.ForeignKey(LessonNumber, models.DO_NOTHING, db_column='fk_lesson_number')
    fk_parity_odd = models.ForeignKey(ParityOdd, models.DO_NOTHING, db_column='fk_parity_odd')
    fk_personal_number = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='fk_personal_number')

    class Meta:
        managed = False
        db_table = 'subject'
        verbose_name_plural = "Subject"

    def __str__(self):
        return 'subject number: {}'.format(self.subject_name)

class Teacher(models.Model):
    personal_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    election_date = models.DateField()
    department = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'
        verbose_name_plural = "Teacher"

    def __str__(self):
        return 'surname: {}'.format(self.surname)
'''

'''
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DayGroupsSubject(models.Model):
    id_day_groups_subject = models.AutoField(primary_key=True)
    fk_day_number = models.ForeignKey('DayOfTheWeek', models.DO_NOTHING, db_column='fk_day_number')
    fk_group_number = models.ForeignKey('Groups', models.DO_NOTHING, db_column='fk_group_number')
    fk_subject_cipher = models.ForeignKey('Subject', models.DO_NOTHING, db_column='fk_subject_cipher')

    class Meta:
        managed = False
        db_table = 'day_groups_subject'

    def __str__(self):
        return 'Day: {}'.format(self.name)


class DayOfTheWeek(models.Model):
    day_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'day_of_the_week'


    def __str__(self):
        return 'name: {} '.format(self.name)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Groups(models.Model):
    group_cipher = models.CharField(max_length=50)
    students_count = models.IntegerField()
    name = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)
    cource = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'groups'

    def __str__(self):
        return 'name: {}'.format(self.name)


class LessonNumbers(models.Model):
    lesson_number = models.AutoField(primary_key=True)
    lesson_begin = models.TimeField()
    lesson_end = models.TimeField()

    class Meta:
        managed = False
        db_table = 'lesson_numbers'

    def __str__(self):
        return 'lesson number: {}'.format(self.lesson_number)


class ParityOdd(models.Model):
    id_number = models.AutoField(primary_key=True)
    state = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'parity_odd'

    def __str__(self):
        return 'state: {}'.format(self.state)


class Subject(models.Model):
    subject_cipher = models.IntegerField(unique=True)
    lesson_type = models.CharField(max_length=10)
    lecture_hall = models.CharField(max_length=10)
    subject_name = models.CharField(max_length=100)
    fk_lesson_number = models.ForeignKey(LessonNumbers, models.DO_NOTHING, db_column='fk_lesson_number')
    fk_parity_odd = models.ForeignKey(ParityOdd, models.DO_NOTHING, db_column='fk_parity_odd')
    fk_teacher = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='fk_teacher')

    class Meta:
        managed = False
        db_table = 'subject'


class Teacher(models.Model):
    personal_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    academic_degree = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    election_date = models.DateField()
    department = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'teacher'
'''