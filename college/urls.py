
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/',include("users.urls.registration")),
    path('api/users/',include("users.urls.login")),
    path('api/users/',include("users.urls.personalDetails")),
    path('api/users/',include("users.urls.address")),
    path('api/users/',include("users.urls.qualification")),
    path('api/users/',include("users.urls.document")),

]
