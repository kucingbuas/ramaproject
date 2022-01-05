from re import template
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Artikel

def dashboard(request):
    template_name = "back/dashboard.html"
    context = {
        'title' : 'dashboard',
    }
    return render(request, template_name, context)
    
def artikel(request):
    template_name = "back/tabel_artikel.html"
    artikel = Artikel.objects.all()
    context = {
        'title' : 'tabel artikel',
        'artikel' : artikel,
    }
    return render(request, template_name,  context)


def tambah_artikel(request):
    template_name = "back/tambah_artikel.html"
    kategory = Kategori.objects.all()
    if request.method == "POST":
        nama = request.POST.get('nama')
        judul = request.POST.get('judul')
        body = request.POST.get('body')
        kategory = request.POST.get('kategory')

        Artikel.objects.create(
            nama=nama,
            judul=judul,
            body=body,
            kat=kategory
        )
        return redirect(artikel)
    context = {
        'title' : 'tambah artikel',
    }
    return render(request, template_name, context)

@login_required
def lihat_artikel(request, id):
    template_name = "back/lihat_artikel.html"
    artikel = Artikel.objects.get(id=id)
    context = {
        'title' : 'lihat artikel',
        'artikel' : artikel
    }
    return render(request, template_name, context)

@login_required
def edit_artikel(request, id):
    template_name = "back/edit_artikel.html"
    a = Artikel.objects.get(id=id)
    if request.method == "POST":
        judul = request.POST.get("judul")
        body = request.POST.get("body")
        print(judul,body)
#simpan data
        a.judul = judul
        a.body = body
        a.save()
        return redirect(artikel)
    context = {
        'title' : 'edit artikel',
        'artikel' : artikel
    }
    return render(request, template_name, context)

@login_required
def delete_artikel(request, id):
    Artikel.objects.get(id=id).delete()
    return redirect(artikel)


def users(request):
    template_name = "back/tabel_user.html"
    context = {
        'title' : 'tabel users'
    }
    return render(request, template_name,  context)

