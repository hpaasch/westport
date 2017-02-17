from django.contrib import admin

from nabes_app.models import (PublicPost, MemberPost, BoardPost,
Newsletter, Profile, Officer)

class OfficerAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'term', 'phone', 'email']
    search_fields = ['name', 'title', 'term', 'phone', 'email']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['primary_last_name', 'family_member_names']
    search_fields = ['primary_last_name', 'family_member_names']


admin.site.register(PublicPost)
admin.site.register(MemberPost)
admin.site.register(BoardPost)
admin.site.register(Newsletter)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Officer, OfficerAdmin)
