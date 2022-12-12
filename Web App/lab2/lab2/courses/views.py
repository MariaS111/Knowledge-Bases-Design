from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Organization, Course, Teacher, Request, DocumentPriceCourse, DocumentTeacherCourse
from .forms import OrganizationForm, CourseForm, TeacherForm, RequestForm, DocumentPriceCourseForm
import datetime


def home1(request):
    return render(request, '1/home1.html')


class HomeOrg(ListView):
    model = Organization
    template_name = '1/home_org.html'
    context_object_name = 'item'
    extra_context = {'title': 'Organizations', 'title1': 'Organization'}


class CreateOrg(CreateView):
    form_class = OrganizationForm
    template_name = '1/add_org.html'
    extra_context = {'title': 'Organization'}


class ViewOrg(DetailView):
    model = Organization
    pk_url_kwarg = 'code'
    template_name = '1/view_org.html'
    context_object_name = 'item'


class DeleteOrg(DeleteView):
    model = Organization
    pk_url_kwarg = 'code'
    template_name = '1/confirm_delete.html'

    def get_success_url(self):
        return reverse('home_o')


class UpdateOrg(UpdateView):
    model = Organization
    fields = [
        "name",
        "address",
        "telephone",
        "email"
    ]
    success_url = ""
    template_name = '1/updating.html'
    pk_url_kwarg = 'code'


class HomeCour(ListView):
    model = Course
    context_object_name = 'item'
    template_name = '1/home_cour.html'
    extra_context = {'title': 'Courses', 'title1': 'Course'}


class CreateCour(CreateView):
    form_class = CourseForm
    template_name = '1/add_cour.html'
    extra_context = {'title': 'Course'}


class ViewCour(DetailView):
    model = Course
    template_name = '1/view_cour.html'
    pk_url_kwarg = 'code'
    context_object_name = 'item'


class DeleteCour(DeleteView):
    model = Course
    pk_url_kwarg = 'code'
    template_name = '1/confirm_delete.html'

    def get_success_url(self):
        return reverse('home_c')


class UpdateCour(UpdateView):
    model = Course
    fields = [
        "name",
        "type",
        "number_of_days",
        "number_of_students",
        "name_of_organization"
    ]
    success_url = ""
    template_name = '1/updating.html'
    pk_url_kwarg = 'code'


class HomeTeach(ListView):
    model = Teacher
    template_name = '1/home_teach.html'
    context_object_name = 'item'
    extra_context = {'title': 'Teachers', 'title1': 'Teacher'}


class CreateTeach(CreateView):
    form_class = TeacherForm
    template_name = '1/add_teach.html'
    extra_context = {'title': 'Teacher'}


class ViewTeach(DetailView):
    model = Teacher
    pk_url_kwarg = 'code'
    context_object_name = 'item'
    template_name = '1/view_teach.html'


class DeleteTeach(DeleteView):
    model = Teacher
    pk_url_kwarg = 'code'
    template_name = '1/confirm_delete.html'

    def get_success_url(self):
        return reverse('home_t')


class UpdateTeach(UpdateView):
    model = Teacher
    fields = [
        "full_name",
        "date_of_birth",
        "sex",
        "education",
        "category"
    ]
    success_url = ""
    template_name = '1/updating.html'
    pk_url_kwarg = 'code'


class HomePr(ListView):
    model = DocumentPriceCourse
    template_name = '1/home_pr.html'
    context_object_name = 'item'
    extra_context = {'title': 'Documents', 'title1': 'Document'}


class CreatePr(CreateView):
    form_class = DocumentPriceCourseForm
    template_name = '1/add_pr.html'
    extra_context = {'title': 'Price'}


def saving(request, code, name_of_course):
    c = name_of_course
    n = DocumentPriceCourse.objects.get(name_of_course__name=c, code=code)
    m = Course.objects.get(name=c)
    m.price_id = n
    m.save()
    return HttpResponseRedirect(reverse('home_pr'))


def task1(request):
    global r
    r = []
    if request.method == 'POST':
        if request.POST.get('name_field', False) and request.POST.get('date_field', False):
            p = Organization.objects.get(name=request.POST.get('name_field', False))
            d = p.course_set.all()
            for i in d:
                for j in i.request_set.all():
                    if j.start_date <= datetime.datetime.strptime(request.POST.get('date_field', False),
                                                                  "%Y-%m-%d").date() and j.end_date >= datetime.datetime.strptime(
                        request.POST.get('date_field', False), "%Y-%m-%d").date():
                        b = Course.objects.get(name=j.name_of_course)
                        e = DocumentPriceCourse.objects.get(pk=b.price_id)
                        p = [b.name, b.number_of_days, e.price, e.final_price]
                        r.append(p)
            return redirect('task12')
        else:
            raise ValidationError("Enter information")
    return render(request, '1/task1.html')


def task12(request):
    return render(request, '1/searchrez1.html', context={'r': r})


def task2(request):
    global rez
    rez = []
    if request.method == 'POST':
        if request.POST.get('full_name_field', False) and request.POST.get('date_field1', False) and request.POST.get(
                'date_field2', False):
            f = DocumentTeacherCourse.objects.filter(
                name_of_teacher__full_name=request.POST.get('full_name_field', False))
            for i in f:
                g = i.course
                if g.start_date <= datetime.datetime.strptime(request.POST.get('date_field1', False),
                                                              "%Y-%m-%d").date() or g.end_date >= datetime.datetime.strptime(
                    request.POST.get('date_field2', False), "%Y-%m-%d").date():
                    n = g.name_of_course
                    ez = [n.name, g.start_date, g.end_date]
                    rez.append(ez)
            return redirect('task22')
        else:
            raise ValidationError("Enter information")
    return render(request, '1/task2.html')


def task22(request):
    return render(request, '1/searchrez2.html', {'r': rez})


def task3(request):
    global k
    k = []
    if request.method == 'POST':
        if request.POST.get('name_field', False) and request.POST.get('date_field1', False) and request.POST.get(
                'date_field2', False):
            g = Request.objects.filter(name_of_course__name=request.POST.get('name_field', False),
                                       start_date__lte=datetime.datetime.strptime(
                                           request.POST.get('date_field1', False),
                                           "%Y-%m-%d").date(),
                                       end_date__lte=datetime.datetime.strptime(request.POST.get('date_field2', False),
                                                                                "%Y-%m-%d").date())
            c = Course.objects.get(name=request.POST.get('name_field', False))
            for i in g:
                if c.number_of_students == i.number_of_staff:
                    m = f"{i.pk} The group is recruited"
                elif c.number_of_students > i.number_of_staff:
                    m = f"{i.pk} The group is not recruited"
                k.append(m)
            return redirect('task32')
        else:
            raise ValidationError("Enter information")
    return render(request, '1/task3.html')


def task32(request):
    return render(request, '1/searchrez3.html', {'r': k})


class ViewPr(DetailView):
    model = DocumentPriceCourse
    pk_url_kwarg = 'code'
    context_object_name = 'item'
    template_name = '1/view_pr.html'


class HomeReq(ListView):
    model = Request
    template_name = '1/home_req.html'
    context_object_name = 'item'
    extra_context = {'title': 'Requests', 'title1': 'Request'}


class CreateReq(CreateView):
    form_class = RequestForm
    template_name = '1/add_req.html'
    extra_context = {'title': 'Request'}


class ViewReq(DetailView):
    model = Request
    context_object_name = 'item'
    template_name = '1/view_req.html'


class UpdateReq(UpdateView):
    model = Request
    fields = [
        "address",
        "telephone",
        "email",
        "name_of_course",
        "number_of_staff",
        "start_date",
        "end_date"
    ]
    success_url = ""
    template_name = '1/updating.html'
    pk_url_kwarg = 'code'

# def delete(request, code):
#     org = Organization.objects.get(code=code)
#     org.delete()
#     return HttpResponseRedirect(reverse('home'))


# def add_org(request):
#     if request.method == 'POST':
#         form = OrganizationForm(request.POST)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             # news = News.objects.create(**form.cleaned_data)
#             #return redirect('home')
#             org = form.save()
#             return redirect(org)
#     else:
#         form = OrganizationForm()
#     return render(request, '1/add_org.html', {'form': form})


# def view_org(request, code):
#     item = get_object_or_404(Organization, code = code)
#     return render(request, '1/view_org.html', {"item":item})

# def home(request):
#      org = Organization.objects.all()
#      return render(request, '1/home_org.html', {'organization': org})
