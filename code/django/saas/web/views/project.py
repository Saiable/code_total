from django.shortcuts import render,HttpResponse,redirect
from web.forms.project import ProjectModelForms
from django.http import JsonResponse
from web import models
def project_list(request):
    '''项目列表'''
    # print(request.tracer.user)
    print(request.tracer.price_policy)
    if request.method == 'GET':
        '''
        GET请求查看项目列表
        '''
        project_dict = {
            'star': [],
            'my': [],
            'join': [],
        }

        my_project_list = models.Project.objects.filter(creator=request.tracer.user)

        for row in my_project_list:
            if row.star:
                project_dict['star'].append({'type':'my','value':row})
            else:
                project_dict['my'].append(row)

        join_project_list = models.ProjectUser.objects.filter(user=request.tracer.user)
        for item in join_project_list:
            if item.star:
                project_dict['star'].append({'type':'join','value':item.project})
            else:
                project_dict['join'].append(item.project)

        form = ProjectModelForms(request)
        return render(request,'web/project_list.html',{'form':form,'project_dict':project_dict})

    # POST，对话框的ajax添加项目
    form = ProjectModelForms(request,data=request.POST)
    if form.is_valid():
        # 验证通过：项目名，颜色，描述，创建者
        form.instance.creator = request.tracer.user
        # 验证通过
        form.save()
        return JsonResponse({'status':True})
    return JsonResponse({'status':False,'error':form.errors})

def project_star(request,project_type,project_id):
    '''星标项目'''
    if project_type == 'my':
        models.Project.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(id=project_id,creator=request.tracer.user).update(star=True)
        return redirect('web:project_list')
    return HttpResponse('请求错误')

def project_unstar(request,project_type,project_id):
    '''取消星标项目'''
    if project_type == 'my':
        models.Project.objects.filter(id=project_id,creator=request.tracer.user).update(star=False)
        return redirect('web:project_list')
    if project_type == 'join':
        models.ProjectUser.objects.filter(id=project_id,creator=request.tracer.user).update(star=False)
        return redirect('web:project_list')
    return HttpResponse('请求错误')