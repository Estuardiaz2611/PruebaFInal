from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, PasswordResetView, logout_then_login,\
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth.decorators import login_required


urlpatterns = [
    path('admin/', admin.site.urls),
    path('encargado/', include (('apps.encargado.urls', 'encargado'), namespace='encargado')),
    path('task/', include (('apps.task.urls', 'task'), namespace='task')),
    path('accounts/login/', LoginView.as_view(template_name='inde.html'), name="login"),
]
