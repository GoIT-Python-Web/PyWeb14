import os

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import PictureForm
from .models import Picture


# Create your views here.


def main(request):
    return render(request, "app_instagram/index.html", context={"title": "Killer Instagram"})


@login_required
def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            pic = form.save(commit=False)
            pic.user = request.user
            pic.save()
            return redirect(to="app_instagram:pictures")

    return render(request, "app_instagram/upload.html", context={"title": "Killer Instagram", "form": form})


@login_required
def pictures(request):
    pictures = Picture.objects.filter(user=request.user).all()  # noqa
    return render(request, "app_instagram/pictures.html", context={"title": "Killer Instagram", "pictures": pictures})


@login_required
def remove_picture(request, pic_id):
    pic = Picture.objects.filter(pk=pic_id, user=request.user)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(pic.first().path)))
    except OSError as e:
        print(e)
    pic.delete()
    return redirect(to="app_instagram:pictures")


@login_required
def edit_picture(request, pic_id):
    if request.method == "POST":
        description = request.POST["description"]
        Picture.objects.filter(pk=pic_id, user=request.user).update(description=description)
        return redirect(to="app_instagram:pictures")

    picture = Picture.objects.filter(pk=pic_id, user=request.user).first()
    ctx = {"title": "Killer Instagram", "picture": picture}
    return render(request, "app_instagram/edit.html", context=ctx)
