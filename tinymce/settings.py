#coding=utf-8
import os
from django.conf import settings
from django.contrib.staticfiles import finders

DEFAULT_CONFIG = getattr(settings, 'TINYMCE_DEFAULT_CONFIG',
 {# // General options
'mode': 'textareas', 'theme': 'advanced',
'plugins': "pagebreak,style,layer,table,save,advhr,advimage,advlink,emotions,iespell,inlinepopups,insertdatetime,preview,media,searchreplace,print,contextmenu,paste,directionality,fullscreen,noneditable,visualchars,nonbreaking,xhtmlxtras,template,wordcount,advlist,autosave",

# // Theme  options
'theme_advanced_buttons1': "save,newdocument,|,bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,styleselect,formatselect,fontselect,fontsizeselect,fullscreen,code",
'theme_advanced_buttons2': "cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,|,insertdate,inserttime,preview,|,forecolor,backcolor",
'theme_advanced_buttons3': "tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,print,|,ltr,rtl",
'theme_advanced_toolbar_location': "top", 'theme_advanced_toolbar_align': "left",
'theme_advanced_statusbar_location': "bottom", 'theme_advanced_resizing': 'true',

# // content_css: "/css/style.css",
'template_external_list_url': "lists/template_list.js", 'external_link_list_url': "lists/link_list.js",
'external_image_list_url': "lists/image_list.js", 'media_external_list_url': "lists/media_list.js",

# // Style formats
'style_formats': [{'title': 'Bold text', 'inline': 'strong'},
    {'title': 'Red text', 'inline': 'span', 'styles': {'color': '#ff0000'}},
    {'title': 'Help', 'inline': 'strong', 'classes': 'help'}, {'title': 'Table styles'},
    {'title': 'Table row 1', 'selector': 'tr', 'classes': 'tablerow'}], 'width': 1200, 'height': 600
}
                         )

USE_SPELLCHECKER = getattr(settings, 'TINYMCE_SPELLCHECKER', False)

USE_COMPRESSOR = getattr(settings, 'TINYMCE_COMPRESSOR', False)

USE_EXTRA_MEDIA = getattr(settings, 'TINYMCE_EXTRA_MEDIA', None)

USE_FILEBROWSER = getattr(settings, 'TINYMCE_FILEBROWSER',
                          'filebrowser' in settings.INSTALLED_APPS)

if 'staticfiles' in settings.INSTALLED_APPS or 'django.contrib.staticfiles' in settings.INSTALLED_APPS:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL', os.path.join(settings.STATIC_URL, 'tiny_mce/tiny_mce.js'))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', finders.find('tiny_mce', all=False))
else:
    JS_URL = getattr(settings, 'TINYMCE_JS_URL', '{!s}js/tiny_mce/tiny_mce.js'.format(settings.MEDIA_URL))
    JS_ROOT = getattr(settings, 'TINYMCE_JS_ROOT', os.path.join(settings.MEDIA_ROOT, 'js/tiny_mce'))

JS_BASE_URL = JS_URL[:JS_URL.rfind('/')]

