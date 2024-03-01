from django.urls import path

from .views import TakeTestSetDetailView, TestSetsListsView

urlpatterns = [
    path("tests/", TestSetsListsView.as_view(), name="tests"),
    path("tests/<int:pk>/", TakeTestSetDetailView.as_view(), name="detail-test"),
]
