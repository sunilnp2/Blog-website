from django.shortcuts import render, redirect
from django.views import View
from post.models import *
from post.forms import CommentForm
from django.contrib import messages
# Create your views here.

class BaseView(View):
    views = {}
    views['category'] = Category.objects.filter(status = 'active')

     # top posts----------------------------------------------------------
    views['firstblog'] = Blog.objects.filter(slug = 'firstblog')      
    views['secondblog'] = Blog.objects.filter(slug = 'secondblog')      
    views['thirdblog'] = Blog.objects.filter(slug = 'thirdblog')      
    views['fourthblog'] = Blog.objects.filter(slug = 'fourthblog')      
    views['fifthblog'] = Blog.objects.filter(slug = 'fifthblog')      

class HomeView(BaseView):
    def get(self, request):

       

        # recent posts--------------------------------------------------------
        self.views['blogs'] = Blog.objects.all()
        return render(request, 'index.html', self.views)


class CategoryView(BaseView):
    def get(self,request,slug):
        category_id = Category.objects.get(slug = slug).id
        self.views['catviews'] = Blog.objects.filter(category = category_id)
        return render(request, 'category.html', self.views)

class BlogDetailView(BaseView):
    def get(self, request, slug):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            comment = request.POST['message']
            date = request.POST['date']

            if not name:
                messages.error(request, "name is required")
                return redirect('post:detail')
            elif not email:
                messages.error(request, "email is required")
                return redirect('post:detail')
            elif not comment:
                messages.error(request, "message is required")
                return redirect('post:detail')

    
            else:
                comm = Comment.objects.create(
                    name = name, 
                    email = email, 
                    comment = comment, 
                    slug = slug,
                    date = date
                    # blog = Blog.objects.get(slug = slug)[0]
                )
                comm.save()
                messages.success(request, "You have Comment here successfully")
                return redirect('post:detail')
        else:
            self.views['blog_details'] = Blog.objects.filter(slug = slug)

            blog_category = Blog.objects.get(slug = slug).category
            self.views['blog_view'] = Blog.objects.filter(category = blog_category)

        return render(request, 'blog_detail.html', self.views)


        

