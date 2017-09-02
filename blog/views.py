from django.shortcuts import render
# Creacion de vista
def post_list(request):
    return render(request, 'blog/post_list.html', {})
