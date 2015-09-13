from django.shortcuts import render
from django.forms import ModelForm, DateTimeInput, HiddenInput, ValidationError
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from main.models import *
from django.db.models import Sum
from django.core import serializers
import datetime
import json

class DateTimeWidget(DateTimeInput):
    class Media:
        js = ('js/jquery.js',
              'js/jquery-ui.js',
              'jqtp/jquery-ui-timepicker-addon.js',
 
            )
        css = {
            'all': (
                'css/jquery-ui/smoothness/jquery-ui.css',
                'jqtp/jquery-ui-timepicker-addon.css',
                )
            }
 
    def __init__(self, attrs=None, format=None):
        super(DateTimeWidget, self).__init__(attrs, format)
        if attrs is not None:
            self.attrs = attrs.copy()
        else:
            self.attrs = {'class': 'datetimepicker'}


class ApplicationForm(ModelForm):
    def clean(self):
        cleaned_data = super(ApplicationForm, self).clean()
        doctor = cleaned_data.get("doctor", False)
        applicant = cleaned_data.get("applicant", False)
        date = cleaned_data.get("date", False)
        time = cleaned_data.get("time", False)
        if not (doctor and applicant and date and time):
            raise ValidationError("Please fill all fields")
        existsdata =  Application.objects.filter(doctor=doctor, date=date, time=time)
        if existsdata:
            raise ValidationError("Appointment with this data already exists")
        if date.weekday() in [5,6]:
            raise ValidationError("How did U send this form??")
        if time not in [1,2,4,8,16,32,64,128,256]:
            raise ValidationError("How did U send this form??")
        
    class Meta:
        model = Application
        fields = ['doctor', 'applicant', 'date', 'time']
        widgets = {'date':DateTimeWidget(), 'time':HiddenInput(attrs={'class': 'timefield'})}
        


class MainView(View):
        def get(self, request):
            busydates = list(Application.objects.filter(date__gte=datetime.date.today()).order_by("date").values("date", "doctor").annotate(busydate=Sum('time')))
            busydates = dict((key['date']+str(key["doctor"]), key['busydate']) for (key) in busydates)
            busydates = json.dumps(busydates)
            form = ApplicationForm
            
            return HttpResponse(render(request, 'main.html', {"busydates":busydates, "form":form}))
        def post(self, request):
            form = ApplicationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('Your application is sent')
            else:
                return HttpResponse('Something is wrong')
	      

