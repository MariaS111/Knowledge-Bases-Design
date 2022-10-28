from django.urls import path
from .views import *

urlpatterns = [
    path('', home1, name="home1"),
    path('task1/', task1, name='task1'),
    path('task12/', task12, name='task12'),
    path('task2/', task2, name='task2'),
    path('task22/', task22, name='task22'),
    path('task3/', task3, name='task3'),
    path('task32/', task32, name='task32'),
    path('org/', HomeOrg.as_view(), name="home_o"),
    path('cour/', HomeCour.as_view(), name="home_c"),
    path('teach/', HomeTeach.as_view(), name="home_t"),
    path('req/', HomeReq.as_view(), name="home_r"),
    path('price/', HomePr.as_view(), name="home_pr"),
    path('org/adding/', CreateOrg.as_view(), name="add_org"),
    path('cour/adding/', CreateCour.as_view(), name="add_cour"),
    path('teach/adding/', CreateTeach.as_view(), name="add_teach"),
    path('req/adding/', CreateReq.as_view(), name="add_req"),
    path('price/adding/', CreatePr.as_view(), name="add_pr"),
    path('org/<str:code>/delete', DeleteOrg.as_view(), name='delete_org'),
    path('org/<str:code>/update', UpdateOrg.as_view(), name='update_org'),
    path('cour/<str:code>/delete', DeleteCour.as_view(), name='delete_cour'),
    path('cour/<str:code>/update', UpdateCour.as_view(), name='update_cour'),
    path('teach/<str:code>/delete', DeleteTeach.as_view(), name='delete_teach'),
    path('teach/<str:code>/update', UpdateTeach.as_view(), name='update_teach'),
    path('req/<int:pk>/update', UpdateReq.as_view(), name='update_req'),
    path('org/<str:code>', ViewOrg.as_view(), name='view_org'),
    path('cour/<str:code>', ViewCour.as_view(), name='view_cour'),
    path('teach/<str:code>', ViewTeach.as_view(), name='view_teach'),
    path('req/<int:pk>', ViewReq.as_view(), name='view_req'),
    path('price/<str:code>', ViewPr.as_view(), name='view_pr'),
    path('price/<str:code>/<str:name_of_course>', saving, name='save'),

]