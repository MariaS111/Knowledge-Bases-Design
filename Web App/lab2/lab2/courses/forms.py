from django import forms
import datetime
from .models import Organization, Course, Teacher, Request, DocumentPriceCourse
import re
from django.core.exceptions import ValidationError


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['code', 'name', 'address', 'telephone', 'email']
        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'address': forms.TextInput(attrs={"class": "form-control"}),
            'telephone': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('The name cannot start with a digit')
        return name


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name', 'type', 'number_of_days', 'number_of_students', 'price', 'name_of_organization']
        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control"}),
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'type': forms.TextInput(attrs={"class": "form-control"}),
            'number_of_days': forms.NumberInput(attrs={"class": "form-control"}),
            'number_of_students': forms.NumberInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"}),
            'name_of_organization': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.match(r'\d', name):
            raise ValidationError('The name cannot start with a digit')
        return name

    def clean_number_of_days(self):
        d = self.cleaned_data['number_of_days']
        if d <= 0:
            raise ValidationError('Number of days cant have such value')
        return d

    def clean_number_of_students(self):
        d = self.cleaned_data['number_of_students']
        if d <= 0:
            raise ValidationError('Number of students cant have such value')
        return d


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['code', 'full_name', 'date_of_birth', 'sex', 'education', 'category']
        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control"}),
            'full_name': forms.TextInput(attrs={"class": "form-control"}),
            'date_of_birth': forms.DateInput(attrs={"class": "form-control"}),
            'sex': forms.Select(attrs={"class": "form-control"}),
            'education': forms.TextInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"})
        }

    def clean_full_name(self):
        name = self.cleaned_data['full_name']
        if re.match(r'\d', name):
            raise ValidationError('The full name cannot start with a digit')
        return name

    def clean_date_of_birth(self):
        date = self.cleaned_data['date_of_birth']
        date_now = datetime.date.today()
        if date_now - date < datetime.timedelta(days=6570):
            raise ValidationError('The age cant be under 18')
        return date


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['name_of_requesting_organization', 'name_of_course',
                  'number_of_staff', 'start_date']
        widgets = {
            'name_of_requesting_organization': forms.Select(attrs={"class": "form-control"}),
            'name_of_course': forms.Select(attrs={"class": "form-control"}),
            'number_of_staff': forms.NumberInput(attrs={"class": "form-control"}),
            'start_date': forms.DateInput(attrs={"class": "form-control"}),
        }


class DocumentPriceCourseForm(forms.ModelForm):
    class Meta:
        model = DocumentPriceCourse
        fields = ['code', 'name_of_course', 'date', 'price']
        widgets = {
            'code': forms.TextInput(attrs={"class": "form-control"}),
            'name_of_course': forms.Select(attrs={"class": "form-control"}),
            'date': forms.DateInput(attrs={"class": "form-control"}),
            'price': forms.NumberInput(attrs={"class": "form-control"})
        }

    def clean_price(self):
        st = self.cleaned_data['price']
        if st <= 0:
            raise ValidationError('We cant accept this price')
        return st
