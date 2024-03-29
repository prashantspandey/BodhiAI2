from django.conf.urls import url
from basicinformation import views

app_name = 'basic'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^teacher/(?P<grade>\d+)/$', views.current_analysis,
        name='current_analysis'),
    url(r'teach/$',views.teacher_home_page, name= 'teacherHomePage'),
    url(r'teacher/update/$',views.teacher_update_page,name='teacher_update_page'),
    url(r'student_analysis/$',views.student_self_analysis, name= 'studentAnalysis'),
    url(r'student_subject_analysis/$',views.student_subject_analysis, name='studentSubjectAnalysis'),

]
