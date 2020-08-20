from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import generic

from .forms import ChoiceForm, QuestionForm
from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results',
                                            args=(question.id,)))


class AddQuestionView(LoginRequiredMixin, generic.CreateView):
    model = Question
    template_name = 'polls/add_questions.html'
    fields = '__all__'
    success_url = reverse_lazy('polls:index')


class AddChoicesView(LoginRequiredMixin, generic.CreateView):
    template_name = 'polls/add_choices.html'
    model = Choice
    fields = ('choice_text',)
    success_url = reverse_lazy('polls:index')

    def form_valid(self, form):
        qsn_id = self.kwargs.get('pk')
        question = Question.objects.get(pk=qsn_id)
        choice = form.save(commit=False)
        choice.question = question
        choice.save()
        return super().form_valid(form)


def add_questions_choices_view(request):
    question_form = QuestionForm()
    choice_form = ChoiceForm()
    if request.method == 'POST':
        question_form = QuestionForm(request.POST)
        choice_form = ChoiceForm(request.POST)
        if question_form.is_valid() and choice_form.is_valid():
            question = question_form.save(commit=False)
            choice = choice_form.save(commit=False)
            choice.question = question
            question.save()
            choice.save()
            return redirect('polls:index')
        else:
            return render(
                request, 'polls/new_question.html',
                {'choice_form': choice_form, 'question_form': question_form}
            )
    else:
        # Request method is GET
        return render(
            request, 'polls/new_question.html',
            {'choice_form': choice_form, 'question_form': question_form}
        )
