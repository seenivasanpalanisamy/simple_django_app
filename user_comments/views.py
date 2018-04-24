from django.shortcuts import render
from user_comments.models import User, Comments
import datetime
from django.http import HttpResponse

# Create your views here.
def stats(request):
    """A view of all bands."""
    total_comments = Comments.objects.count()
    total_users=User.objects.count()
    return render(request, 'user_comments/stats.html', {'total_comments': total_comments,'total_users': total_users})

def create(request):
    """A view of all bands."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user,created=User.objects.get_or_create(name=data['name'])
    comment=Comments.objects.create(name=user,comment=data['comment'],title=data['title'])
    comment.save()
    return HttpResponse(status=204)

def update(request):
    """A view of all bands."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user=User.objects.get(name=data['name'])
    comments = Comments.objects.get(name=user,comment=data['comment'],title=data['title'])
    comments.comment=data['new_comment']
    comments.save()
    return HttpResponse(status=204)

def delete(request):
    """A view of all bands."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user=User.objects.get(name=data['name'])
    comment=Comments.objects.filter(name=user,comment=data['comment'],title=data['title'])
    comment.delete()
    return HttpResponse(status=204)

def details(request):
    """A view of all bands."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST

    if data['name']:
        user=User.objects.get(name=data['name'])
        comments=Comments.objects.filter(name=user).order_by('-updated_at')[:100]
        return render(request, 'user_comments/details.html', {'comments': comments})
    else:
        comments=Comments.objects.all.order_by('-updated_at')[:100]
        return render(request, 'user_comments/details.html', {'comments': comments})