from course import views
from django.conf.urls import url
urlpatterns=[
url('^$',views.courseprofile),
url('test',views.test),
url('python',views.python),
url('java',views.java),
url('c',views.c),
url('payment',views.Payment),
url('final',views.FinalPayment),
url('profile',views.profile),
url('video',views.Video),
]
