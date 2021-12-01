from django.http import response
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, CreateView, FormView
from django.views.generic.edit import FormView
from .models import *
from .forms import CustomerRegistrationForm, CustomerLoginForm, DataCollectionForm, TxtFileForm, MaterialListForm
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required





# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class AboutView(TemplateView):
    template_name = "about.html"




class MaterialListUploadView(CreateView):
    template_name = "material_list_upload.html"
    form_class = MaterialListForm
    success_url = reverse_lazy('blog:material-list-upload')

    def form_valid(self, form):
        return super().form_valid(form)


class MaterialsListView(TemplateView):
    template_name = "materialslist.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['material_list'] = MaterialList.objects.all()

        return context  


class CustomerLogInView(FormView):
    template_name = "login.html"
    form_class = CustomerLoginForm
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username = uname, password=pword)
        if usr is not None and usr.customer:
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": CustomerLoginForm, "error": "Invalid credentials"})

        return super().form_valid(form)


class CustomerLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('blog:home')

class CustomerRegistrationView(CreateView):
    template_name = "customerregistration.html"
    form_class = CustomerRegistrationForm 
    success_url = reverse_lazy('blog:home')

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        login(self.request, user)

        return super().form_valid(form)


class AjaLogView(TemplateView):
    template_name = "aja_log.html"

class UploadGlobalDataView(TemplateView):
    template_name = "upload_global_data.html"

class ViewGlobalDataView(TemplateView):
    template_name = "view_global_data.html"

class DetailsOfDataCollectionView(CreateView):
    template_name = "datacollection.html"
    form_class = DataCollectionForm
    success_url = reverse_lazy('blog:show-data-collection')

    def form_valid(self, form):
        return super().form_valid(form)

    def Upload_Notes(request):
        if request.method == "POST":
            n = request.FILES['upload_data']
        return response(request, "datacollection.html", n)


class ShowDataCollectionView(TemplateView):
    template_name = "showing_data_collection.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['instru_list'] = DetailsOfDataCollection.objects.all()

        return context 

class TxtFileView(CreateView):
    template_name = "txtfileupload.html"
    form_class = TxtFileForm
    success_url = reverse_lazy('blog:txt-table')

    def form_valid(self, form):

        return super().form_valid(form)

    def Upload_TXT(request):
        if request.method == "POST":
            t = request.FILES["txtfiles_folder"]
        return response(request, "txtfileupload.html", t)

class TxtTableView(TemplateView):
    template_name = "txt_table.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['txt_list'] = TxtFile.objects.all()

        return context 







