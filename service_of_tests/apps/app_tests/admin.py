from django.contrib import admin
from django.db import models
from django.forms.widgets import Textarea

from apps.app_tests.models import Choice, Question, TestSet, UserChoice

from .forms import BaseChoiceFormset


@admin.register(Choice, UserChoice)
class DefaultModelAdmin(admin.ModelAdmin):
    pass


class ChoiceInline(admin.TabularInline):
    model = Choice
    formset = BaseChoiceFormset
    formfield_overrides = {
        models.CharField: {"widget": Textarea},
    }
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    formfield_overrides = {
        models.CharField: {"widget": Textarea},
    }


@admin.register(TestSet)
class TestSetAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "description")
    list_display_links = (
        "id",
        "title",
    )
    ordering = ["id"]
