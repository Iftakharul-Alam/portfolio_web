from django.contrib import admin

from resume.models import Resume, Training, SkillDetail, Skill

# Register your models here.


admin.site.register(Resume)
admin.site.register(Training)


class SkillDetailInline(admin.TabularInline):
    model = SkillDetail
    extra = 1


class SkillAdmin(admin.ModelAdmin):
    inlines = [
        SkillDetailInline,
    ]


admin.site.register(Skill, SkillAdmin)
