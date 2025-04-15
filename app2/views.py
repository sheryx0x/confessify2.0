from django.shortcuts import render , redirect
from .models import*
import random

def share_confessions(request):
    if request.method=='POST':
        confession_text=request.POST.get('content')
        if confession_text:
            new_confession = Confession.objects.create(content=confession_text)
            seen_confessions_ids=request.session.get('seen_confessions_ids' , [])
            seen_confessions_ids.append(new_confession.id)
            request.session['seen_confessions_ids'] = seen_confessions_ids
            return redirect("view_random_confession")

    return render(request, "app2/share_confession.html")


def view_random_confession(request):
    seen_confessions_ids=request.session.get('seen_confessions_ids' , [])
    unseen_confessions = Confession.objects.exclude(id__in=seen_confessions_ids)
    if unseen_confessions.exists():
        random_confession = random.choice(list(unseen_confessions))
        seen_confessions_ids.append(random_confession.id)
        request.session['seen_confessions_ids']=seen_confessions_ids
        return render(request, "app2/view_confession.html", {
            "confession": random_confession
        })
    else:
        
        return render(request, "app2/no_more_confession.html")