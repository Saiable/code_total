from django.shortcuts import render,redirect,HttpResponse
from web.forms.wiki import WikiModelForm
from django.urls import reverse
from web import models
from django.http import JsonResponse
def wiki(request, project_id):
    '''wiki的首页'''
    wiki_id = request.GET.get('wiki_id')
    if not wiki_id or not wiki_id.isdecimal():
        print('wiki_id is not exsits')
        return render(request,'web/wiki.html')
    print('wiki')
    wiki_object = models.Wiki.objects.filter(id=wiki_id,project_id=project_id).first()

    return render(request, 'web/wiki.html', {'wiki_object':wiki_object})

def wiki_add(request,project_id):
    '''添加文章'''
    if request.method == 'GET':
        form = WikiModelForm(request)
        return render(request,'web/wiki_add.html',{'form':form})
    form = WikiModelForm(request,data=request.POST)
    if form.is_valid():
        # 判断用户是否选择了父文章
        if form.instance.parent:
            form.instance.depth = form.instance.parent.depth + 1
        else:
            form.instance.depth = 1
        form.instance.project = request.tracer.project
        form.save()
        url = reverse('web:wiki',kwargs={'project_id':project_id})
        return redirect(url)
    return render(request, 'web/wiki_add.html', {'form': form})

def wiki_catalog(request,project_id):
    '''wiki目录'''
    # data = models.Wiki.objects.filter(project=request.tracer.project).values_list("id","title","parent_id")
    # return JsonResponse({'status':True,'data':list(data)})
    # vlaues_list输出的是元组格式，而values返回的是字典
    data = models.Wiki.objects.filter(project=request.tracer.project).values("id","title","parent_id").order_by('depth','id')
    # data = models.Wiki.objects.filter(project=request.tracer.project).values("id","title","parent_id")

    return JsonResponse({'status':True,'data':list(data)})

def wiki_delete(request, project_id, wiki_id):
    '''删除文章'''
    models.Wiki.objects.filter(project_id=project_id,id=wiki_id).delete()
    url = reverse('web:wiki', kwargs= {'project_id':project_id})
    return redirect(url)

def wiki_edit(request, project_id, wiki_id):
    '''编辑文章'''
    wiki_object = models.Wiki.objects.filter(project_id=project_id,id=wiki_id).first()
    if not wiki_object:
        url = reverse('web:wiki',kwargs={'project_id':project_id})
        return redirect(url)
    form = WikiModelForm(request,instance=wiki_object)
    return render(request,'web/wiki_add.html',{'form':form})
    