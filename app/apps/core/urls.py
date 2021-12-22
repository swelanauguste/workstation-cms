from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("reports", views.ReportListSearchView.as_view(), name="report-list-search"),
    path(
        "report-detail-<slug:slug>",
        views.ReportDetailView.as_view(),
        name="report-detail",
    ),
    path("report-new", views.ReportCreateView.as_view(), name="report-create"),
    # =====================
    path(
        "workstations",
        views.WorkstationListSearchView.as_view(),
        name="workstation-list-search",
    ),
    path(
        "workstation-detail-<slug:slug>",
        views.WorkstationDetailView.as_view(),
        name="workstation-detail",
    ),
    path(
        "workstation-new",
        views.WorkstationCreateView.as_view(),
        name="workstation-create",
    ),
    # =====================
    path(
        "owners",
        views.OwnerListSearchView.as_view(),
        name="owner-list-search",
    ),
    path(
        "owners-detail-<slug:slug>",
        views.OwnerDetailView.as_view(),
        name="owner-detail",
    ),
    path(
        "owners-new",
        views.OwnerCreateView.as_view(),
        name="owner-create",
    ),
    # =====================
    path("pdf_gen", views.pdf_gen, name="pdf_gen"),
]
