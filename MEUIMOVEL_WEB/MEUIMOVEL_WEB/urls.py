from django.contrib import admin
from django.urls import include, path
from core import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
      
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.index, name='index'),
  path('new-todo', views.new_todo, name="new_todo"),
  path('mark-as-done/<int:id>', views.mark_as_done, name="mark_as_done"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
      
urlpatterns += staticfiles_urlpatterns()