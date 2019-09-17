from django.contrib import admin
from testapp.models import BasicInfo,Opprtunity
# Register your models here.
class OpprtunityAdmin(admin.ModelAdmin):
    list_display=['Job_Type','Posting_title','Date_opened','city']
admin.site.register(Opprtunity,OpprtunityAdmin)
class BasicInfoAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','Email','Mobile','your_location','current_address','language','Nationality','qualification','year_of_passout','DOB','workingexpfrom','workingexpto','Job_Type']
admin.site.register(BasicInfo,BasicInfoAdmin)
