import os

from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from mixins.mixins import TimeStampMixin


class Owner(TimeStampMixin):
    """
    Owner model
    """

    name = models.CharField(max_length=100)
    dept = models.CharField("Department", max_length=255)
    phone = models.CharField(max_length=25)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    
    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name + "-" + self.dept)
        super(Owner, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:owner-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name


class Workstation(TimeStampMixin):
    """
    Workstation model
    """

    WORKSTATION_STATUSES = [
        ("AVAILABLE", "Available"),
        ("IN_USE", "In Use"),
        ("MAINTENANCE", "Maintenance"),
        ("DECOMMISSIONED", "Decommissioned"),
        ("UNKNOWN", "Unknown"),
    ]
    serial_number = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        max_length=20, choices=WORKSTATION_STATUSES, default="AVAILABLE"
    )
    owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)
    
    class Meta:
        ordering = ["serial_number"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.serial_number)
        super(Workstation, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:workstation-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.serial_number


def report_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "{0}/{1}".format(instance.workstation.serial_number, filename)


class Report(TimeStampMixin):
    """
    Report model
    """

    ticket_no = models.CharField("spiceworks ticket number", max_length=6, unique=True)
    workstation = models.ForeignKey(
        Workstation, on_delete=models.SET_NULL, null=True, blank=True
    )
    findings = models.CharField(max_length=100, blank=True, null=True)
    recommendations = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to=report_directory_path, blank=True, null=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.workstation.serial_number)
        super(Report, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("core:report-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.workstation.serial_number
