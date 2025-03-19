from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Amiibo
from .forms import AmiiboForm

def front_page(request):
    return render(request, "index.html")
    # return render(request, "index_css.html")


def add_Amiibo(request):
    success = False
    added_amiibo = None
    if request.method == "POST":
        form = AmiiboForm(request.POST)
        if form.is_valid():
            new_amiibo = form.save()
            success = True
            added_amiibo = new_amiibo
            return render(
                request,
                "add_amiibo_css.html", # "add_amiibo_css.html",
                {"form": form,
                 "added_amiibo": added_amiibo,
                 "success": success},
            )
    else:
        form = AmiiboForm()
    return render(
        request,
        "add_amiibo_css.html", # "add_amiibo_css.html",
        {"form": form,
         "added_amiibo": added_amiibo,
         "success": success},
    )


def search_Amiibo(request):
    page_number = request.GET.get("page", 1)
    name = request.GET.get("name", "").strip()
    series = request.GET.get("series", "").strip()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        series = request.POST.get("series", "").strip()
        # Reset to first page on new search
        page_number = 1

    if name or series:
        amiibos = Amiibo.objects.filter(
            name__icontains=name, series__icontains=series
        ).order_by("id")  # Order by id to ensure consistency
    else:
        amiibos = Amiibo.objects.all().order_by("id")  # Order the results

    paginator = Paginator(amiibos, 100)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "search_amiibo_css.html",
        # "search_amiibo.html",
        {"amiibos": page_obj,
         "name_query": name,
         "series_query": series},  # Align with naming convention from search_contact
    )


def edit_Amiibo(request, Amiibo_id, page_number):
    pn = request.GET.get("page", page_number)
    print(f"[DBG] edit_amiibo {Amiibo_id}, {page_number}, {pn} <<<")
    success = False

    if request.method == "POST":
        amiibo = Amiibo.objects.get(id=Amiibo_id)
        name = request.POST.get("name")
        series = request.POST.get("series")
        condition_status = request.POST.get("condition_status")
        is_owned = request.POST.get("is_owned") == 'on'
        
        if amiibo.name != name or amiibo.series != series or amiibo.condition_status != condition_status or amiibo.is_owned != is_owned:
            amiibo.name = name
            amiibo.series = series
            amiibo.condition_status = condition_status
            amiibo.is_owned = is_owned
            amiibo.save()
            success = True

    amiibo_list = Amiibo.objects.all()
    paginator = Paginator(amiibo_list, 10)
    page_number = request.POST.get("page", request.GET.get("page", page_number))
    page_obj = paginator.get_page(page_number)
    
    return render(
        request,
        # "edit_amiibo.html",
        "edit_amiibo_css.html",
        {
            "amiibos": page_obj,
            "success": success,
            "updated_Amiibo_id": Amiibo_id,
        },
    )

def delete_Amiibo(request, Amiibo_id, page_number):
    print(f"[DBG] delete_amiibo called for ID: {Amiibo_id}")
    if request.method == "POST":
        amiibo = get_object_or_404(Amiibo, id=Amiibo_id)
        amiibo.delete()
        # Redirect to the same page number after delete
        return redirect("edit_Amiibo", Amiibo_id=Amiibo_id, page_number=page_number)

