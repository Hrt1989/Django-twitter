from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


#Unregister Groups
admin.site.unregister(Group)

# mix profile info into user info 
class ProfileInLine(admin.StackedInline):
    model = Profile



# Extend user model
class UserAdmin(admin.ModelAdmin):
    model = User
    # just display username fields on admin page 
    fields = ["username"]
    inlines = [ProfileInLine]

# unregister initial user 
admin.site.unregister(User)
# Register user  and profile
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

