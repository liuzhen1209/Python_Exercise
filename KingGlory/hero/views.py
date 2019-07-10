from django.shortcuts import render
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
    return render(request, 'hero/glorydetail.html', {'h': h, 'h1': h1})
