from django.db import models

from .utils import code_generator, create_shortcode
from django.conf import settings
from .validators import validate_url
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

class arnURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs_main = super(arnURLManager, self).all(*args, **kwargs)
        qs = qs_main.filter(active=True)
        return qs
    
    def refresh_shortcodes(self, items=None):
        qs = arnURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.id)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)
        



class arnURL(models.Model):
    url = models.CharField(max_length=220, validators=[validate_url])
    shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = arnURLManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        if not "http" in self.url:
            self.url = "http://" + self.url
        super(arnURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)



#arn
#arnav123



        
    