from django.urls import path
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
# from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('$', PasswordResetView.as_view(),
        {'post_reset_redirect': reverse_lazy('password_reset_done')}, name='password_reset'),
    path('done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('^(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        {'post_reset_redirect': reverse_lazy('password_reset_complete')}, name='password_reset_confirm'),
    path('complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]