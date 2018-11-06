from django.urls import path
from . import views
# from django.contrib import admin
# Django2.1中弃用了from django.contrib import views as auth_views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='user_login'),
    # 此处属于Django2.1版本改动
    # path('login/', LoginView.as_view(template_name='account/login.html'), name='user_login'),
    # 如果在此处传入login模板位置，就不用在project/settings中设置LOGIN_REDIRECT_URL = '/blog/'
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='user_login'),
    # Django2.1 正确的写法
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='user_logout'),
    path('register/', views.register, name='user_register'),
    path('password-change/', auth_views.PasswordChangeView.as_view(
        template_name='account/password_change_form.html',
        success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='account/password_change_done.html'), name='password_change_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        email_template_name='account/password_reset_email.html',
        template_name='account/password_reset_form.html',
        subject_template_name='account/password_reset_subject.txt',
        success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='account/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='account/password_reset_complete.html'), name='password_reset_complete'),
    path('my-information/', views.myself, name='my_information'),
    path('edit-my-information/', views.myself_edit, name='edit_my_information'),
    path('my-image/', views.my_image, name='my_image'),
]


