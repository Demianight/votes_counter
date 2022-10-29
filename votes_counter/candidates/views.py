from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .models import Candidate


def index(request):

    return render(
        request,
        template_name='index.html',
        context={
            'candidates': Candidate.objects.all()
        },
    )


def vote(request, candidate_id):
    candidate = get_object_or_404(
        Candidate, id=candidate_id
    )
    candidate.votes = candidate.votes + 1
    candidate.save()
    return redirect(
        reverse(
            'candidates:index'
        )
    )
