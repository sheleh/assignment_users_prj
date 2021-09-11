from django.urls import path
from . import views
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('all_groups', views.AllGroups)

urlpatterns = [
    path('all_users', views.AllUsers.as_view()),
    path('all_users/<int:pk>', views.RetrieveUpdateDestroy.as_view()),
    path('', include(router.urls)),

    # Auth
    path('auth/', obtain_auth_token),
    #path('login', views),

]