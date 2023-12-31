from django.contrib import admin
from django.urls import path
from .views import *

app_name = "tutos"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path("listone", ListOneView.as_view(), name="listone"),
    path("listtwo", ListTwoView.as_view(), name="listtwo"),
    path("listthree", ListThreeView.as_view(), name="listthree"),
    
    path("html/detail", HtmlDetailView.as_view(), name="html_detail"),
    path('vscode/introduction', VSCodeIntroductionView.as_view(), name="vscode_introduction"),
    path("vscode/extension", VSCodeExtensionView.as_view(), name="vscode_extension"),
    
    path('html/introduction', HtmlIntroductionView.as_view(), name="html_introduction"),
    path('html/structure', HtmlStructureView.as_view(), name="html_structure"),
    path("html/text_formating", HtmlTextFormatingView.as_view(), name="html_textformating"),
    path("html/media", HtmlMediaView.as_view(), name="html_media"),
    path("html/listandtable", HtmlListandTableView.as_view(), name="html_listandtables"),
    path("html/formsanddivs", HtmlFormsandDivsView.as_view(), name="html_formsanddivs"),
    path("html/advance", HtmlAdvanceView.as_view(), name="html_advance"),
    
]