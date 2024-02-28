from django import forms

from .models import Choice, Question, TestSet


class BaseQuestionFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if not all(self.cleaned_data):
            raise forms.ValidationError("Заполните все поля вопросов")


class BaseChoiceFormset(forms.models.BaseInlineFormSet):
    def clean(self):
        if not all(self.cleaned_data):
            raise forms.ValidationError("Заполните все поля ответов")
        if list(map(lambda a: a["is_correct"], self.cleaned_data)).count(True) != 1:
            raise forms.ValidationError("На вопрос должен быть 1 правильный ответ")


class ChoiceForm(forms.ModelForm):
    class Meta:
        fields = ("text", "is_correct")
        model = Choice


class QuestionForm(forms.ModelForm):

    class Meta:
        fields = ["question_text"]
        model = Question


QuestionFormSet = forms.inlineformset_factory(
    TestSet,
    Question,
    form=QuestionForm,
    formset=BaseQuestionFormset,
    can_delete=False,
)
ChoiceFormSet = forms.inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    extra=4,
    can_delete=False,
    formset=BaseChoiceFormset,
)
