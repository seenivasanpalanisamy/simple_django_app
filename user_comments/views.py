from django.shortcuts import render
from user_comments.models import User, Comments
import datetime
from django.http import JsonResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def stats(request):
    """A view of all stats."""
    total_comments = Comments.objects.count()
    total_users=User.objects.count()
    return render(request, 'user_comments/stats.html', {'total_comments': total_comments,'total_users': total_users})

def create(request):
    """A view of all create."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user,created=User.objects.get_or_create(name=data['name'])
    comment=Comments.objects.create(name=user,comment=data['comment'],title=data['title'])
    comment.save()
    logger.debug('Comment inserted')
    return JsonResponse({'status':'success'})

def update(request):
    """A view of all update."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user=User.objects.filter(name=data['name']).first()
    if user:
        comments = Comments.objects.get(name=user,comment=data['comment'],title=data['title'])
        comments.comment=data['new_comment']
        comments.updated_at=datetime.datetime.now()
        comments.save()
        logger.debug('Comment updated')
        status="success"
    else:
        logger.debug('User not exist')
        status="User not exist"

    return JsonResponse({'status':status})

def delete(request):
    """A view of all delete."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST
    user=User.objects.filter(name=data['name']).first()
    if user:
        comment=Comments.objects.filter(name=user,comment=data['comment'],title=data['title'])
        comment.delete()
        logger.debug('Comment Deleted')
    return JsonResponse({'status':'success'})

def details(request):
    """A view of all details."""
    if request.method == 'GET':
        data=request.GET
    elif request.method == 'POST':
        data=request.POST

    if 'name' in data:
        user=User.objects.filter(name=data['name']).first()
        if user:
            comments=Comments.objects.filter(name=user).order_by('-updated_at')[:100]
            logger.debug('Comment fetched for user')
            return render(request, 'user_comments/details.html', {'comments': comments})
        else:
            logger.debug('User does not exist')
            return JsonResponse({'status':'No Associated User'})       
    else:
        comments=Comments.objects.order_by('-updated_at')[:100]
        logger.debug('Comment fetched')
        return render(request, 'user_comments/details.html', {'comments': comments})


def about(request):
    return render(request, 'user_comments/about.html', {})

"""NOT YET COMPLETED"""

def handler404(request):
    response = render_to_response('user_comments/404.html', {},
                              context_instance=RequestContext(request))
    response.status_code = 404
    return response

def handler500(request):
    response = render_to_response('user_comments/500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response