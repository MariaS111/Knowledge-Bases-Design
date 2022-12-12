from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class Organization(models.Model):
    code = models.CharField(max_length=30, primary_key=True, verbose_name='Code number of the organization')
    name = models.CharField(max_length=30, verbose_name='Name of the organization', unique=True)
    address = models.CharField(max_length=50, verbose_name='Address of the organization')
    telephone = models.CharField(max_length=30, verbose_name='Telephone of the organization')
    email = models.EmailField(max_length=40, verbose_name='Email of the organization')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_org', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'
        ordering = ['code']


class Course(models.Model):
    code = models.CharField(max_length=30, primary_key=True, verbose_name='Code number of the course')
    name = models.CharField(max_length=30, verbose_name='Name of the course', unique=True)
    type = models.CharField(max_length=30, verbose_name='Type of the course')
    number_of_days = models.IntegerField(verbose_name='Number of days of the course')
    number_of_students = models.IntegerField(verbose_name='Number of students of the course')
    price = models.ForeignKey('DocumentPriceCourse', on_delete=models.SET_NULL, verbose_name='Price of the course',
                              blank=True, null=True)
    name_of_organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True,
                                             verbose_name='Name of the parent organization')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('view_cour', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        ordering = ['code']


class DocumentPriceCourse(models.Model):
    code = models.CharField(max_length=30, primary_key=True, verbose_name='Code number of document')
    name_of_course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, verbose_name='Name of the course')
    date = models.DateField(verbose_name='Date of establishment')
    price = models.IntegerField(verbose_name='Established price')
    final_price = models.IntegerField(verbose_name='Final price of the course', default=0)

    def __str__(self):
        return self.code + ' ' + Course.objects.get(name=self.name_of_course).name

    def save(self, *args, **kwargs):
        self.final_price = self.price - (0.2 * self.price)
        super(DocumentPriceCourse, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_pr', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Document with new price'
        verbose_name_plural = 'Documents with new prices'
        ordering = ['code']


class Teacher(models.Model):
    code = models.CharField(max_length=30, primary_key=True, verbose_name='Code number of teacher')
    full_name = models.CharField(max_length=100, verbose_name='Full name of teacher')
    date_of_birth = models.DateField(verbose_name='Date of birth')
    sex = models.CharField(max_length=10, choices=[('Male', 'male'), ('Female', 'female')], verbose_name='Sex')
    education = models.TextField(verbose_name='Education')
    category = models.CharField(max_length=10,
                                choices=[('Higher', 'Higher'), ('First', 'First',), ('Second', 'Second',)],
                                verbose_name='Category')

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('view_teach', kwargs={'code': self.code})

    class Meta:
        verbose_name = 'Teacher'
        verbose_name_plural = 'Teachers'
        ordering = ['code']


class DocumentTeacherCourse(models.Model):
    name_of_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, verbose_name='Name of teacher')
    course = models.ForeignKey('Request', on_delete=models.SET_NULL, null=True, verbose_name='Number of Request')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Document with relation of teacher and course'
        verbose_name_plural = 'Documents with relations of teachers and courses'
        ordering = ['pk']


class Request(models.Model):
    name_of_requesting_organization = models.ForeignKey('Organization', on_delete=models.SET_NULL, null=True,
                                                        verbose_name='Name of the requesting organization')
    name_of_course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True, verbose_name='Name of course')
    number_of_staff = models.IntegerField(verbose_name='Number of staff')
    start_date = models.DateField(verbose_name='Start date of the course')
    end_date = models.DateField(verbose_name='End date of the course')

    def clean(self):
        st = self.number_of_staff
        c = self.name_of_course
        if st <= 0 or st > Course.objects.get(name=c).number_of_students:
            raise ValidationError('We cant accept this amount of people')
        elif self.start_date.weekday() in (5, 6) or self.end_date in (5, 6):
            raise ValidationError('We cant accept this dates, as it is weekends')

    def __str__(self):
        return Organization.objects.get(name=self.name_of_requesting_organization ).name + ' ' + Course.objects.get(name=self.name_of_course).name

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + timedelta(
            days=(list(Course.objects.filter(name=self.name_of_course).values())[0]['number_of_days']))
        super(Request, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('view_req', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['pk']


class Staff(models.Model):
    request = models.ForeignKey('Request', on_delete=models.SET_NULL, null=True, verbose_name='Name of request')
    full_name = models.CharField(max_length=100, verbose_name='Full name of employee')
    post = models.CharField(max_length=100, verbose_name='Post of employee')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'
        ordering = ['pk']
