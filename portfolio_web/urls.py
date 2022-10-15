from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from blog.views import BlogListView
from me.views import AboutView, HomeView
from portfolio.views import PortfolioListView
from resume.views import ResumeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('portfolio/', PortfolioListView.as_view(), name='portfolio'),
    path('resume/', ResumeListView.as_view(), name='resume'),
    path('blog/', BlogListView.as_view(), name='blog'),
    # path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
