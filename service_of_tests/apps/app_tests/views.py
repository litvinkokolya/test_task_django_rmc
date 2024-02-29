from django.db.models import Count
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import TestSet, Question, Choice, UserChoice


class TestSetsListsView(LoginRequiredMixin, ListView):
    model = TestSet
    template_name = "app_tests/tests.html"
    context_object_name = "test_sets"


class TakeTestSetDetailView(LoginRequiredMixin, TemplateView):
    model = TestSet
    template_name = "app_tests/test.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        tests = TestSet.objects.get(id=self.kwargs["pk"])
        questions = tests.question_set.all()
        current_question = questions.first()

        user_choices = UserChoice.objects.filter(user=self.request.user)

        data["question"] = current_question
        data["choices"] = Choice.objects.filter(question=current_question)
        data["user_answers"] = user_choices

        return data

    def post(self, request, *args, **kwargs):
        question_id = request.POST.get("question_id")
        choice_id = request.POST.get("choice")

        question = Question.objects.get(id=question_id)
        choice = Choice.objects.get(id=choice_id)

        user_choice = UserChoice.objects.filter(
            user=request.user, question=question
        ).first()

        if user_choice:
            user_choice.choice = choice
            user_choice.save()
        else:
            UserChoice.objects.create(
                user=request.user, question=question, choice=choice
            )

        test_set = TestSet.objects.get(id=self.kwargs["pk"])
        questions = test_set.question_set.all()

        current_question_index = list(questions).index(question)
        next_question_index = current_question_index + 1
        if next_question_index < len(questions):
            next_question = questions[next_question_index]
        else:
            next_question = None

        user_answers = UserChoice.objects.filter(user=self.request.user)
        wrong_answers = user_answers.filter(choice__is_correct=False)
        correct_answers = user_answers.filter(choice__is_correct=True)

        percentage = round(correct_answers.count() / user_answers.count(), 2) * 100

        return render(
            request,
            self.template_name,
            {
                "question": next_question,
                "choices": (
                    Choice.objects.filter(question=next_question)
                    if next_question
                    else None
                ),
                "percentage": percentage,
                "correct_answers": correct_answers.count(),
                "wrong_answers": wrong_answers.count(),
            },
        )
