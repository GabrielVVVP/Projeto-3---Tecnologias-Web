from django.contrib import admin
from .models import Feature, User, Patient, Doctor, Event, Instance, Symptom, Diagnostic, Disease, Reference

admin.site.register(User)
admin.site.register(Instance)
admin.site.register(Symptom)
admin.site.register(Diagnostic)
admin.site.register(Disease)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Event)
admin.site.register(Feature)
admin.site.register(Reference)
