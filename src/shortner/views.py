from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import arnURL
from .forms import submitUrlForm
# Create your views here.

# def arn_redirect_view(request, shortcode=None ,*args, **kwargs):
#     obj = get_object_or_404(arnURL, shortcode=shortcode)
#     return HttpResponseRedirect(obj.url)


def home_view_fbv(request, *args, **kwargs):
    if request.method == "POST":
        print(request.POST)
    return render(request, "shortner/home.html", {})


class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = submitUrlForm()
        context = {
            "title": "ARNPH",
            "form": the_form
        }
        return render(request, "shortner/home.html", context)
    
    def post(self, request, *args, **kwargs):
        form = submitUrlForm(request.POST)
        context = {
            "title": "ARNPH",
            "form": form
        }
        template = "shortner/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = arnURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }

            if created:
                template = "shortner/success.html"
            else:
                template = "shortner/exists.html"
        
        return render(request, template, context)



class ArnCBView(View):
    def get(self, request, shortcode=None ,*args, **kwargs):
        obj = get_object_or_404(arnURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
    









    # def post(self, request, *args, **kwargs):
    #     return HttpResponse()