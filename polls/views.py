from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question


# Create your views here.

def index(request):
    myname = "Khuong Viet Tai"
    taisan = ["Phone", "Laptop", "Money"]
    context = {"name": myname, "taisan": taisan}

    return render(request, "polls/index.html", context)


def viewlist(request):
    # list_question = get_object_or_404(Question, pk=1)
    list_question = Question.objects.all()
    context = {"dsquest": list_question}
    return render(request, "polls/question_list.html", context)