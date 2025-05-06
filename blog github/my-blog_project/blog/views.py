from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from .models import Post, Category, Tag
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.utils.html import strip_tags

def index(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')  # Yayınlanan postları al
    paginator = Paginator(posts, 9)  # Her sayfada 9 kart
    page_number = request.GET.get('page')  # URL'den sayfa numarasını al
    page_obj = paginator.get_page(page_number)  # İlgili sayfayı al

    return render(request, 'blog/index.html', {
        'page_obj': page_obj,  # Sayfa objesini template'e gönder
    })

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    recent_posts = Post.objects.filter(status='published').order_by('-created_at')[:5]
    categories = Category.objects.annotate(post_count=Count('post'))  # Kategoriler ve makale sayıları

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'recent_posts': recent_posts,
        'categories': categories,  # Kategorileri template'e gönder
    })

def blog_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)  # Slug ile tag'i al
    posts = Post.objects.filter(tags=tag)  # Tag ile ilişkili gönderileri al
    return render(request, 'blog/blog_tag.html', {
        'tag': tag,
        'posts': posts
    })

def blog_create(request,slug):
    posts = Post.objects.all()  
    return render(request, 'blog/blog_create.html',{'slug': slug, 'posts': posts})

def blog_update(request, slug):
    posts = Post.objects.all()  
    return render(request, 'blog/blog_update.html', {'slug': slug, 'posts': posts})

def blog_delete(request, slug):
    posts = Post.objects.all()  
    return render(request, 'blog/blog_delete.html', {'slug': slug, 'posts': posts})

def blog_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    posts = Post.objects.filter(categories=category)

    return render(request, 'blog/blog_category.html', {
        'category': category,
        'posts': posts
    })

def about(request):
    return render(request, 'blog/about.html')
def contact(request):
    post = Post.objects.all()
    recent_posts = Post.objects.filter(status='published').order_by('-created_at')[:5]
    categories = Category.objects.annotate(post_count=Count('post'))  # Kategoriler ve makale sayıları
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject", "No Subject")
        message = request.POST.get("message")

        # E-posta gönderme işlemi
        try:
            send_mail(
                subject=f"Contact Form: {subject}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email='ortamali0031@gmail.com',
                recipient_list=['ortamali0031@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Your message has been sent successfully!")
        except Exception as e:
            messages.error(request, "An error occurred while sending your message. Please try again later.")

    return render(request, 'blog/contact.html', {
        'post': post,
        'recent_posts': recent_posts,
        'categories': categories,  # Kategorileri template'e gönder
    })

