from django.urls import path
from . import views
from articles.views import index

app_name = "pages"

urlpatterns = [
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("pricing/", views.pricing, name="pricing"),
    path("", index, name="home"),
    path("test/", views.test, name="test"),
]
