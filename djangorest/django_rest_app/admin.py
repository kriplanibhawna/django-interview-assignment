from django.contrib import admin


# Now register the new UserAdmin...
from .models import *
admin.site.register(Members)
admin.site.register(Books)
