# -*- coding:utf-8 -*-

from django.http import HttpResponse
def index(request):
    from models import cache
    cache_key = 'counter'
    counter = cache().get(cache_key)
    if not counter:
        counter = 0
    counter += 1
    cache().set(cache_key, counter)
    return HttpResponse("Hello, world. count:{}".format(counter))
