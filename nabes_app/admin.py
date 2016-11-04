from django.contrib import admin

from nabes_app.models import PublicPost, MemberPost, BoardPost, Newsletter, Profile


admin.site.register(PublicPost)
admin.site.register(MemberPost)
admin.site.register(BoardPost)
admin.site.register(Newsletter)
admin.site.register(Profile)
