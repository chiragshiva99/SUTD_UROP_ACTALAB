from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

app_name = "blog"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("material_list_upload/",
         login_required(MaterialListUploadView.as_view()),
         name="material-list-upload"),
    path("materials_list/", MaterialsListView.as_view(),
         name="materials-list"),
    path("login/", CustomerLogInView.as_view(), name="customer-log-in"),
    path("signup/",
         CustomerRegistrationView.as_view(),
         name="customer-registration"),
    path("logout/", CustomerLogoutView.as_view(), name="customerlogout"),
    path("aja_log/", AjaLogView.as_view(), name="aja-log"),
    path("upload_global_data/",
         UploadGlobalDataView.as_view(),
         name="upload-global-data"),
    path("view_global_data/",
         ViewGlobalDataView.as_view(),
         name="view-global-data"),
    path("details_of_data_collection/",
         login_required(DetailsOfDataCollectionView.as_view()),
         name="data-collection"),
    path("show_data_collection/",
         ShowDataCollectionView.as_view(),
         name="show-data-collection"),
    path("txt_upload/", TxtFileView.as_view(), name="txt-file-upload"),
    path("txt-table/", TxtTableView.as_view(), name="txt-table"),

    #path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
