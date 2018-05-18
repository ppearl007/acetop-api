from django.contrib import admin
from .models import Course, Listcontent, Sublistcontent

# Register your models here.
admin.site.register(Course)
admin.site.register(Listcontent)
admin.site.register(Sublistcontent)