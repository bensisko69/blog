from django.shortcuts import render

def post_list(request):
    return render(request, 'content/post.html', {})