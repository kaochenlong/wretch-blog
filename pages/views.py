from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lucky"] = [1, 2, 4, 8, 19]
        return context


class AboutView(TemplateView):
    template_name = "pages/about.html"


class ContactView(TemplateView):
    template_name = "pages/contact.html"


def test(request):
    return render(request, "pages/test.html")


def pricing(request):
    return render(request, "pages/pricing.html")
