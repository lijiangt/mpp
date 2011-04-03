# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
#from django.forms import forms
#from django.utils.translation import ugettext as _

import os
import datetime
import traceback
import urllib
#import uuid


def upload_generic_file(request,allow_type,max_size,save_path,url_path):
    if request.method == 'POST':
        f = request.FILES['filedata']
        if not f:
            return HttpResponse('{"err":"%s","msg":""}'%'您必须选取文件上传。') 
        if f.size > max_size*1024*1024:
            return HttpResponse('{"err":"%s","msg":""}'%('文件大小超过了限制：%sM'%max_size)) 
        ext=os.path.splitext(f.name)[1]
        if not ext or len(ext)<=1 or ext[1:].lower() not in allow_type:
            return HttpResponse('{"err":"%s","msg":""}'%('上传文件扩展名必须为：%s'%','.join(allow_type)))
        if not save_path:
            return HttpResponse('{"err":"%s","msg":""}'%'服务器端未设置文件保存路径，请联系系统管理员。')
        path = datetime.datetime.now().strftime('/%Y/%j/%H/')
        full_save_path = save_path + path
        try:
            if not os.path.exists(full_save_path):
                os.makedirs(full_save_path)
#            file_name = str(uuid.uuid1())+ext
            file_name = f.name
            full_url_path = url_path+path+urllib.quote(file_name.encode('utf-8'))
            dest = open(full_save_path+file_name, 'wb+')
            try:
                for chunk in f.chunks():
                    dest.write(chunk)
                return HttpResponse('{"err":"","msg":"%s"}'%full_url_path) 
            finally:
                dest.close()
        except:
            return HttpResponse('{"err":"%s","msg":""}'%('处理上传文件时出现错误。错误详细信息:%s'%traceback.format_exc()))  #(sys.exc_info()[0],sys.exc_info()[1])
            
    else:
        return HttpResponse('{"err":"%s","msg":""}'%'请求方式错误，必须为POST方式。') 

@csrf_exempt
def upload_file(request):
    return upload_generic_file(request,settings.FILE_UPLOAD_FILE_TYPE,
               settings.FILE_UPLOAD_FILE_MAX_SIZE,settings.FILE_UPLOAD_FILE_SAVE_PATH,settings.FILE_UPLOAD_FILE_URL_PATH)

@csrf_exempt
def upload_image(request):
    return upload_generic_file(request,settings.FILE_UPLOAD_IMAGE_TYPE,
               settings.FILE_UPLOAD_IMAGE_MAX_SIZE,settings.FILE_UPLOAD_IMAGE_SAVE_PATH,settings.FILE_UPLOAD_IMAGE_URL_PATH)

@csrf_exempt
def upload_flash(request):
    return upload_generic_file(request,settings.FILE_UPLOAD_FLASH_TYPE,
               settings.FILE_UPLOAD_FLASH_MAX_SIZE,settings.FILE_UPLOAD_FLASH_SAVE_PATH,settings.FILE_UPLOAD_FLASH_URL_PATH)

@csrf_exempt
def upload_media(request):
    return upload_generic_file(request,settings.FILE_UPLOAD_MEDIA_TYPE,
               settings.FILE_UPLOAD_MEDIA_MAX_SIZE,settings.FILE_UPLOAD_MEDIA_SAVE_PATH,settings.FILE_UPLOAD_MEDIA_URL_PATH)