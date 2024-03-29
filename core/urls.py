from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from strawberry.django.views import AsyncGraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', AsyncGraphQLView.as_view(schema=schema))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
