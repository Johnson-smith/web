from django.http import JsonResponse
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
from django.views.decorators.csrf import  csrf_exempt


def history(req):
    return JsonResponse({'status': 0, 'msg': 'success'})


from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from deply.models import Fabu
from deply.serializers import DeplySerializer



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def deply_list(request):
    """
    列出所有的实例，或创建一个新的实例.
    """
    if request.method == 'GET':
        deplys = Fabu.objects.all()
        serializer = DeplySerializer(deplys, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeplySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
    #post 如果存在put方法
    #elif request.method == 'POST':
    #    data = JSONParser().parse(request)
    #    print(data)
    #    postservername = data['servername'].strip()
    #    postproduct = data['product'].strip()
    #    postversion = data['version'].strip()
    #    postip = data['ip'].strip()
    #    status = Fabunew.objects.filter(product=postproduct, servername=postservername, ip=postip)
    #    if status:
    #        Fabunew.objects.filter(product=postproduct, servername=postservername, ip=postip).update(product=postproduct, servername=postservername, ip=postip, version=postversion)
    #        return JSONResponse('201 update sucess')
    #    else:
    #        Fabunew.objects.create(product=postproduct, servername=postservername, ip=postip, version=postversion)
    #        return JSONResponse('201 create sucess')
    #    return JSONResponse('bad body 400')


@csrf_exempt
def deply_detail(request, pk):
    """
    Retrieve, update or delete a code deplys.
    """
    try:
        deplys = Fabu.objects.get(pk=pk)
    except Fabu.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DeplySerializer(deplys)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DeplySerializer(deplys, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        deplys.delete()
        return HttpResponse(status=204)


