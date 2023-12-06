"""
URL configuration for formation2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView,PasswordChangeDoneView
from django.urls import path
import authentication.views
import reseau.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup', authentication.views.signup_page.as_view(), name='signup'),

    # path('', authentication.views.login_page.as_view(), name='login'),

    path('logout/', authentication.views.logout_view, name='logout'),
    path('welcome/', reseau.views.welcome_view, name='welcome'),
    path('image/upload', reseau.views.photo_upload, name='image-upload'),
    path('profil/photo/upload', authentication.views.photo_upload, name='profil-photo-upload'),
    path('post/create', reseau.views.post_and_image_upload, name='post-create'),
    path('post/<int:id>', reseau.views.post_view, name='post-view'),
    path('post/<int:id>/edit', reseau.views.edit_post_view, name='edit-post'),
    path('image/multiple-upload', reseau.views.create_multiple_images_view, name='image-upload-multiple'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
