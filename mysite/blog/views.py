from django.views import generic
from .models import Posts
 
from django.contrib import messages
from .forms import CommentForm, FeedbackForm
from django.shortcuts import render, get_object_or_404, redirect

class PostList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by= 3

# class PostDetail(generic.DetailView):
#     model = Posts
#     template_name = 'post_detail.html'


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Posts, slug=slug)
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

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def feedback(request):
    if request.method == 'POST':
        f = FeedbackForm(request.POST)
        if f.is_valid():
            f.save()
            messages.add_message(request, messages.INFO, 'Feedback Submitted.')
            return redirect('feedback')
    else:
        f = FeedbackForm()
    return render(request, 'feedback.html', {'form': f})


    