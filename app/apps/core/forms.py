from django import forms
from .models import Report, Workstation, Owner


class ReportCreateForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["ticket_no", "workstation", "findings", "recommendations", "file"]
        widgets = {
            "workstation": forms.Select(attrs={"class": "form-control"}),
            "findings": forms.Textarea(attrs={"rows": 3}),
            "recommendations": forms.Textarea(attrs={"rows": 3}),
        }


class WorkStationCreateForm(forms.ModelForm):
    class Meta:
        model = Workstation
        fields = "__all__"
        exclude = ["slug", "created_by", "updated_by"]
        # widgets = {
        #     "workstation": forms.Select(attrs={"class": "form-control"}),
        #     "findings": forms.Textarea(attrs={"rows": 3}),
        #     "recommendations": forms.Textarea(attrs={"rows": 3}),
        # }
class OwnerCreateForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"
        exclude = ["slug", "created_by", "updated_by"]
        # widgets = {
        #     "workstation": forms.Select(attrs={"class": "form-control"}),
        #     "findings": forms.Textarea(attrs={"rows": 3}),
        #     "recommendations": forms.Textarea(attrs={"rows": 3}),
        # }
