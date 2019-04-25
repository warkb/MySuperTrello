from django.contrib.auth.decorators import login_required
from django.urls import path, include
from tastypie.api import Api
from .api import JobResource

from django.conf.urls import url

from .views import JobFormView, JobForm, IndexView

v1_api = Api(api_name='v1')
v1_api.register(JobResource())

urlpatterns = [
    path('api/', include(v1_api.urls)),
    url(r'job-form/', login_required(JobFormView.as_view()), name='job_form'),
    url(r'/', IndexView.as_view(), name='index_job'),
]
