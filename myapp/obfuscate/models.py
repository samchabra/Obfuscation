from django.db import models
import uuid

# Create your models here.

class link(models.Model):
    obf_id = models.SlugField(max_length=36,primary_key = True)
    #obf_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    target = models.URLField(max_length = 200)
    clicks = models.IntegerField(default=0)
