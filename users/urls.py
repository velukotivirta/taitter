from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# localhost/users

app_name = 'users'

urlpatterns = [
    path("register", views.register, name="register"), # Use basepath /users made in rnr/urls.py; path is what comes next
    path("login/", views.login_view, name="login"), 
    path("logout/", views.logout_view, name="logout"), 
]

urlpatterns = urlpatterns + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
