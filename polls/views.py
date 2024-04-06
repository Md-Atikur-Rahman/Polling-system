from django.shortcuts import get_object_or_404, render
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Question , Choice
# Create your views here.

def home(request):
    return render(request, "home.html")

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:3]
    context = {"latest_question_list": latest_question_list}
    return render(request, "index.html", context)

def detail(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, "detail.html", {"question": question})

def result(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    return render(request, "result.html", {"question": question})

def vote(request, q_id):
    question = get_object_or_404(Question, pk=q_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:result", args=(question.id,)))