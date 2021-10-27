from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(DistrictEntry)
admin.site.register(UpazillaEntry)

admin.site.register(user_application)
admin.site.register(Organization)
admin.site.register(Gender)
admin.site.register(Religion)
admin.site.register(Nationality)
admin.site.register(sscBoard)
admin.site.register(ssc_group)
admin.site.register(hsc_group)
admin.site.register(hscBoard)
admin.site.register(Versity)
admin.site.register(VersitySubject)
admin.site.register(VersityDuration)
admin.site.register(job_category)
admin.site.register(applicant)
admin.site.register(jobpost)
admin.site.register(Status)


