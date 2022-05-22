from django.contrib import admin
# <<<<<<< HEAD
from .models import User, UserPic
# =======
# from .models import User

# admin.site.register(User)

# >>>>>>> site-authentication-feature


admin.site.register(User)
admin.site.register(UserPic)
