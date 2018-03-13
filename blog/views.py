from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View

from .models import Post
from .forms import PostForm, StartupForm
# Create your views here.
class PostCreate(View):
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})
    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            return render(request, self.template_name, {'form':bound_form})

class PostUpdate(View):
    form_class = PostForm
    model = Post
    template_name = 'blog/post_form_update.html'

    def get_object(self, year, month, slug):
        return get_object_or_404(self.model, pub_date__year=year, pub_date__month=month, slug=slug)
    def get(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        context = {
          'form': self.form_class(instance=post),
          'post': post,
        }
        return render(request, self.template_name, context)

    def post(self, request, year, month, slug):
        post = self.get_object(year, month, slug)
        bound_form = self.form_class(request.POST, instance=post)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        else:
            context = {
              'form': bound_form,
              'post': post,
            }
            return render(request, self.template_name, context)
class PostList(View):
    template_name = 'blog/post_list.html'

    def get(self, request):
        return render(request, self.template_name, {'post_list': Post.objects.all()})

class PostDelete(View):
    def get(self, request, year, month, slug):
        post= get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})
    def post(self, request, year, month, slug):
        post= get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug__iexact=slug)
        post.delete()
        return redirect('blog_post_list')














def post_detail(request, year, month, slug):
    post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
    # post = Post.objects.filter('pub_date.year'=year|'pub_date.month'=month|'slug'=slug)
    return render(request, 'blog/post_detail.html', {'post':post})

class StartupCreate(View):
    form_class = StartupForm
    template_name = 'organizerstartup_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form':  self.form_class()})


    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name, {'form': bound_form})













def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})
def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html',{'startup':startup})


def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})
    # template = loader.get_template('organizer/tag_list.html')
    # context = {'tag_list': tag_list}
    # return HttpResponse(output)
    # return render_to_response('organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_detail(request,slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})
    # return render_to_response('organizer/tag_detail.html', {'tag': tag})
    # tag = get_object_or_404(Tag, slug__iexact=slug)
    # template = loader.get_template('organizer/tag_detail.html')
    # context = {'tag': tag}
    # return HttpResponse(template.render(context))

# def tag_create(request):
#     if request.method == "POST":
#         formm})

