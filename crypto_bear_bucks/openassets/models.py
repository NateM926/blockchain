from django.db import models


# create asset def url with json for open assets using this model
class Asset_Definition_File(models.Model):
    asset_ids = models.CharField(max_length=58)
    name_short = models.CharField(max_length=8)
    name = models.CharField(max_length=50)

class Output(models.Model):
    asset_ids = models.CharField(max_length=58)
    asset_quantity = models.PositiveIntegerField(null=True, blank=True)
    colored = models.BooleanField(default=True)
    marker_output = models.BinaryField(max_length=48)
