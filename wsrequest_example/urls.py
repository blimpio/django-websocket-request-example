from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers

from snippets import views


admin.autodiscover()


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns(
    # Prefix
    '',

    url(r'^admin/', include(admin.site.urls)),

    url(r'^api/', include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls',
        namespace='rest_framework')),

    (r'^$', TemplateView.as_view(template_name='index.html'))
)
