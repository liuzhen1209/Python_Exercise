from django.contrib import admin
from hero.models import GloryPracice, GlorySkill
# Register your models here.


class GloryPraciceAdmin(admin.ModelAdmin):
    list_display = ['name', 'dialogue', 'age', 'sex', 'glory_type']


class GlorySkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name', 'skill_type', 'skill_desc', 'glory']


admin.site.register(GloryPracice, GloryPraciceAdmin)
admin.site.register(GlorySkill, GlorySkillAdmin)
