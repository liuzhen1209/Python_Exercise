from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader,RequestContext
from hero.models import GloryPracice, GlorySkill
# Create your views here.


def index(request):
    # return HttpResponse('hello django！')
    h = GloryPracice.objects.all()
    return render(request, 'hero/index.html', {'h': h})


def glorydetail(request, hid):
    h = GloryPracice.objects.get(id=hid)
    h1 = GloryPracice.objects.all()
    h2 = GlorySkill.objects.get(glory_id=hid)
    return render(request, 'hero/glorydetail.html', {'h': h, 'h1': h1, 'h2': h2})


def glorydelete(request, hid):
    h = GloryPracice.objects.get(id=hid)
    h.delete()
    return redirect('/index')


def gloryadd(request):
    g = GloryPracice()
    g.name = '程咬金'
    g.dialogue = '两个字,揍他'
    g.age = 50
    g.sex = True
    g.save()
    return redirect('/index')
