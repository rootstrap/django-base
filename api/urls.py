from django.urls import include, path

urlpatterns = [
    path('session/', include('rest_auth.urls')),
    path('session/registration', include('rest_auth.registration.urls')),
]
