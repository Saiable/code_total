from django.shortcuts import render
from web.forms.wiki import WikiModelForm
def wiki(request, project_id):
    '''wiki的首页'''
    return render(request, 'web/wiki.html')

def wiki_add(request,project_id):
    '''添加文章'''
    form = WikiModelForm()
    return render(request,'web/wiki_add.html',{'form':form})