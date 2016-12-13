from django.contrib import admin

from nabes_app.models import (PublicPost, MemberPost, BoardPost,
Newsletter, Profile, Officer)

class OfficerAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'term', 'phone', 'email']
    search_fields = ['name', 'title', 'term', 'phone', 'email']


admin.site.register(PublicPost)
admin.site.register(MemberPost)
admin.site.register(BoardPost)
admin.site.register(Newsletter)
admin.site.register(Profile)
admin.site.register(Officer, OfficerAdmin)
