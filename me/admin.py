from django.contrib import admin

from me.models import About, PersonalInfo, Language, IELTS, GRE, PersonalSkill, Education, JOBS

# Register your models here.

admin.site.register(About)
admin.site.register(PersonalInfo)
admin.site.register(Language)
admin.site.register(IELTS)
admin.site.register(GRE)
admin.site.register(PersonalSkill)
admin.site.register(Education)
admin.site.register(JOBS)
