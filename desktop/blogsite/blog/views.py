from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse 
from .models import Post, Comment
from .forms import CommentForm, ContactForm, ReplyForm
from django.views.generic import ListView
# from datetime import datetime
from django.db.models import Q

# Post list display
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by= 3
    
    
    
# Post comment view
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'blog-detail.html', {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

# comment's reply views
def reply(request, slug):
    comment = get_object_or_404(Comment, slug=slug)
    replies = comment.replies.filter()
    new_reply = None
    # Comment posted
    if request.method == 'POST':
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            new_reply = reply_form(commit=False)
            new_reply.comment = comment
            new_reply.save()
    else:
        reply_form = ReplyForm()

    return render(request, 'reply.html', {'comment':comment,
                                                'replies':replies, 
                                                "new_reply":new_reply,
                                           'reply_form': reply_form})
    

#Search parameters  
class SearchResultsView(ListView):
    model = Post
    template_name = 'search.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list =Post.objects.filter(
            Q(slug__icontains=query) | Q(title__icontains=query) | Q(body__icontains=query)
        )
        return object_list
    
    

    
def home(request):
    arr = ['Optimistic', 'Determined', 'Focused', 'Trustworthy']
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context ={
        'result': arr,
        'queryset': queryset 
        }
    
    return render(request, 'base.html', context)
    



def contact(request):
    contact_form = ''
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
        else:
            contact_form = ContactForm()
    return render(request, 'contact.html', {'contact_form': contact_form})


