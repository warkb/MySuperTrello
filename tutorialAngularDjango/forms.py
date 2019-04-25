from django import forms
from djng.forms import NgFormValidationMixin, NgModelFormMixin
from crispy_forms.helper import FormHelper

from .models import Job


class JobForm(NgModelFormMixin, forms.ModelForm):
    """
    Job Form with a little crispy forms added!
    """
    def __init__(self, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        setup_bootstrap_helpers(self)

    class Meta:
        model = Job
        fields = ('name', 'description',)


def setup_bootstrap_helpers(object):
    object.helper = FormHelper()
    object.helper.form_class = 'form-horizontal'
    object.helper.label_class = 'col-lg-3'
    object.helper.field_class = 'col-lg-8'