from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render

from core.models import Post


@login_required
def index(request):
    # TODO: Fix for friends posts
    posts = (Post.objects
             .filter(Q(visibility="public") | Q(author__friends__user=request.user), active=True)
             .order_by('-created_at'))

    context = {
        'posts': posts
    }

    return render(request, 'core/index.html', context)
