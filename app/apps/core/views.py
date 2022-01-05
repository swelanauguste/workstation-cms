import io

from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from reportlab.pdfgen import canvas

from .forms import OwnerCreateForm, ReportCreateForm, WorkStationCreateForm
from .models import Owner, Report, Workstation


def pdf_gen(request, slug):
    obj = Report.objects.get(slug=slug)
     # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='hello.pdf')


class OwnerCreateView(CreateView):
    model = Owner
    form_class = OwnerCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class OwnerDetailView(DetailView):
    model = Owner


class OwnerListSearchView(ListView):
    model = Owner
    paginate_by = 9

    def get_queryset(self):
        queryset = Owner.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) | Q(dept__icontains=q) | Q(phone__icontains=q)
            ).distinct()
        return queryset


class WorkstationCreateView(CreateView):
    model = Workstation
    form_class = WorkStationCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class WorkstationDetailView(DetailView):
    model = Workstation


class WorkstationListSearchView(ListView):
    model = Workstation
    paginate_by = 9

    def get_queryset(self):
        queryset = Workstation.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(serial_number__icontains=q)
                | Q(status__icontains=q)
                | Q(owner__name__icontains=q)
                | Q(owner__dept__icontains=q)
            ).distinct()
        return queryset

    # def get_queryset(self):
    #     return Workstation.objects.filter(
    #         Q(owner__user=self.request.user) | Q(owner__group__user=self.request.user)
    #     )


# class ReportListView(ListView):
#     model = Report


class ReportListSearchView(ListView):
    model = Report
    paginate_by = 9

    def get_queryset(self):
        queryset = Report.objects.all()
        q = self.request.GET.get("q")
        if q:
            queryset = queryset.filter(
                Q(ticket_no__icontains=q)
                | Q(workstation__serial_number__icontains=q)
                | Q(workstation__owner__name__icontains=q)
                | Q(workstation__owner__dept__icontains=q)
                | Q(workstation__owner__phone__icontains=q)
            ).distinct()
        return queryset


class ReportDetailView(DetailView):
    model = Report


class ReportCreateView(CreateView):
    model = Report
    form_class = ReportCreateForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.updated_by = self.request.user
        return super().form_valid(form)
