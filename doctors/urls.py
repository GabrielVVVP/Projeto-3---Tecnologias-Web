from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.index, name='signup'),
    path('login/<login>', views.index, name='login'),
    path('about', views.about, name='about'),
    path('about/signup', views.about, name='asignup'),
    path('about/login/<login>', views.about, name='alogin'),
    path('menu/<user_id>', views.menu, name='menu'),
    path('menu/update/<user_id>/<type>', views.menu, name='userupdate'),
    path('menu/diagnostic/<user_id>', views.diagnostic, name='diagnostic'),
    path('menu/diagnostic/<user_id>/<instance_id>', views.diagnostic, name='checkdiagnostic'),
    path('menu/instances/<user_id>', views.instances, name='instances'),
    path('menu/instances/<user_id>/newinstance', views.instances, name='newinstance'),
    path('menu/instances/edit/<user_id>/<instance>', views.editinstance, name='editinstance'),
    path('menu/instances/edit/newsymptom/<user_id>/<instance>/<type>', views.editinstance, name='newsymptom'),
    path('menu/instances/edit/delete/<user_id>/<instance>/<symptom>/<type>', views.editinstance, name='delsymptom'),
    path('menu/instances/edit/delete/<user_id>/<instance>/<type>', views.editinstance, name='delinstance'),
    path('menu/history/<user_id>', views.history, name='history'),
    path('menu/history/view/<user_id>/<diag_id>/<check>', views.diagnostic, name='viewhistory'),
    path('menu/doctors/<user_id>', views.doctors, name='doctors'),
    path('menu/doctors/view/<user_id>/<diag_id>', views.doctors, name='viewdoctors'),
    path('menu/doctor/view/<user_id>/<doc_id>', views.docshow, name='thisdoctor'),
    path('menu/calendar/<user_id>', views.calendar, name='calendar'),
    path('menu/patients/<user_id>', views.patients, name='patients'),
    path('menu/patients/<user_id>/<patient_id>/<type>', views.patients, name='addrempatients'),
    path('menu/patientinst/<user_id>/<type>', views.patients, name='instpatients'),
    path('menu/patientinst/patient/<user_id>/<patient_id>', views.instances, name='instspatient'),
    path('menu/patientinst/patient/instance/<user_id>/<patient_id>/<instance>', views.editinstance, name='instpatient'),
    path('menu/patientdiag/<user_id>/<type>', views.patients, name='diagpatients'),
    path('menu/patientdiag/patient/<user_id>/<patient_id>', views.history, name='diagspatient'),
    path('menu/patientdiag/patient/diagnostic/<user_id>/<patient_id>/<diag_id>/<check>', views.diagnostic, name='diagpatient'),
    path('menu/events/<user_id>/<type>', views.patients, name='eventpatients'),
    path('menu/events/patient/<user_id>/<patient_id>', views.event, name='eventpatient'),
    path('menu/calendar/<user_id>/<type>', views.calendar, name='doccalendar')
]