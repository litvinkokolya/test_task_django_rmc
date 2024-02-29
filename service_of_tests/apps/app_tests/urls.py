from django.urls import path

from .views import TestSetsListsView, TakeTestSetDetailView

urlpatterns = [
    path("tests/", TestSetsListsView.as_view(), name="tests"),
    path("test/<int:pk>/", TakeTestSetDetailView.as_view(), name="test"),
]
