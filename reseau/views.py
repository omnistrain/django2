from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from . import forms, models
from django.forms import formset_factory


# Create your views here.


@login_required()
def post_view(request, id):
    post = get_object_or_404(models.Post, id=id)
    return render(request, 'reseau/post_view.html', context={'post': post})


@login_required()
def post_and_image_upload(request):
    post_form = forms.post_form()
    image_form = forms.image_form()

    if request.method == 'POST':
        post_form = forms.post_form(request.POST)
        image_form = forms.image_form(request.POST, request.FILES)
        if any([post_form.is_valid(), image_form.is_valid()]):
            image = image_form.save(commit=False)
            image.uploader = request.user
            image.save()

            post = post_form.save(commit=False)
            post.author = request.user
            post.photo = image
            post.save()
            return redirect('welcome')

    context = {
        'post_form': post_form,
        'image_form': image_form
    }

    return render(request, 'reseau/create_post.html', context=context)


@login_required()
@permission_required('reseau.add_image', raise_exception=True)
def photo_upload(request):
    form = forms.image_form()
    if request.method == 'POST':
        form = forms.image_form(request.POST, request.FILES)
        photo = form.save(commit=False)
        photo.uploader = request.user
        photo.save()
        return redirect('welcome')

    return render(request, 'reseau/photo_upload.html', context={'form': form})



>

@login_required()
def welcome_view(request):
    images = models.Image.objects.all()
    posts = models.Post.objects.all()

    return render(request, 'reseau/welcome.html', context={'images': images, 'posts': posts})


@login_required
def edit_post_view(request, id):
    post = get_object_or_404(models.Post, id=id)
    edit_form = forms.post_form(instance=post)
    delete_form = forms.delete_post_form()

    if request.method == 'POST':
        if 'edit_post' in request.POST:
            edit_form = forms.post_form(request.POST, instance=post)
            if edit_form.is_valid():
                edit_form.save()
        elif 'delete_post' in request.POST:
            delete_form = forms.delete_post_form(request.POST)
            if delete_form.is_valid():
                post.delete()
        return redirect('welcome')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
    }
    return render(request, 'reseau/edit_post.html', context=context)


def create_multiple_images_view(request):
    ImagesFormset = formset_factory(forms.image_form, extra=3)
    formset = ImagesFormset()

    if request.method == 'POST':
        formset = ImagesFormset(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:
                    image = form.save(commit=False)
                    image.uploader = request.user
                    image.save()
        return redirect('welcome')

    return render(request, 'reseau/create_multiple_images.html', {'formset': formset})
