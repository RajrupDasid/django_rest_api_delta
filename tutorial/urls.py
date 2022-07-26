from django.urls import include, path
from rest_framework import routers
from quickstart import views

router =  routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'groups',views.GroupViewSet)


urlpatterns = [
    path('snippet/',include('snippets.urls')),
    path('',include(router.urls)),
#    path('admin/', admin.site.urls),

    path('api-auth/',include('rest_framework.urls', namespace='rest_framework'))

]
