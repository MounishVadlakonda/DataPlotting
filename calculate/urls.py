from django.urls import path
from calculate import views
urlpatterns = [
    
    path('',views.homepage),
    path('import_csv_file',views.import_csv_file),
    path('get_diplay_filedata',views.get_diplay_filedata,name='get_diplay_filedata'),
    path('get_result',views.get_result,name='get_result'),
    path('plot',views.plot,name='plot'),
]
