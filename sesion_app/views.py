from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Page_a_form, PageBForm, Page_c_form


def page_a(request):
    if request.method == 'POST':
        the_form = Page_a_form(request.POST)
        if the_form.is_valid():
            request.session['page_a_data'] = the_form.cleaned_data
            return redirect('page_b')
    else:
        the_form = Page_a_form()
    return render(request, 'pagina_a.html', {'form': the_form})


def page_b(request):
    if request.method == 'POST':
        form = PageBForm(request.POST)
        if form.is_valid():
            request.session['page_b_data'] = form.cleaned_data
            return redirect('page_c')
    else:
        form = PageBForm()
    return render(request, 'pagina_b.html', {'form': form})


def page_c(request):
    
    if request.method == 'POST':
        form = Page_c_form(request.POST)
        if form.is_valid():
            request.session['page_c_data'] = form.cleaned_data
            return redirect('resume')
    else:
        form = Page_c_form()
    return render(request, 'pagina_c.html', {'form': form})


def summary(request):
    if  request.method == 'GET':
        page_a_data = request.session.get('page_a_data', {})
        page_b_data = request.session.get('page_b_data', {})
        page_c_data = request.session.get('page_c_data', {})

        if not (page_a_data and page_b_data and page_c_data):
            messages.error(request, 'Termina el formulario ')
            return redirect('page_a')

        return render(request, 'resume.html',
                    {'page_a_data': page_a_data, 'page_b_data': page_b_data, 'page_c_data': page_c_data})
    else:
        return HttpResponseRedirect("/page_a") 