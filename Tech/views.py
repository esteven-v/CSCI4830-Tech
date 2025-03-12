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
    added_Amiibo = None
    if request.method == "POST":
        form = AmiiboForm(request.POST)
        if form.is_valid():
            new_Amiibo = form.save()
            success = True
            added_Amiibo = new_Amiibo
            return render(
                request,
                "add_Amiibo_css.html", # "add_Amiibo_css.html",
                {"form": form,
                 "added_Amiibo": added_Amiibo,
                 "success": success},
            )
    else:
        form = ContactForm()
    return render(
        request,
        "add_contact_css.html", # "add_contact_css.html",
        {"form": form,
         "added_contact": added_contact,
         "success": success},
    )


def search_contact(request):
    page_number = request.GET.get("page", 1)
    name = request.GET.get("name", "").strip()
    email = request.GET.get("email", "").strip()

    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        # Reset to first page on new search
        page_number = 1

    if name or email:
        contacts = Contact.objects.filter(
            name__icontains=name, email__icontains=email
        ).order_by("id")  # Order by name to ensure consistency
    else:
        contacts = Contact.objects.all().order_by("id")  # Order the results

    paginator = Paginator(contacts, 100)
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "search_contact_css.html",
        # "search_contact.html",
        {"contacts": page_obj,
         "name_query": name,
         "email_query": email},
    )

def edit_contact(request, contact_id, page_number):
    pn = request.GET.get("page", page_number)
    print(f"[DBG] edit_contact {contact_id}, {page_number}, {pn} <<<")
    success = False

    if request.method == "POST":
        contact = Contact.objects.get(id=contact_id)
        name = request.POST.get("name")
        email = request.POST.get("email")
        if contact.name != name or contact.email != email:
            contact.name = name
            contact.email = email
            contact.save()
            success = True

    contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 10)
    page_number = request.POST.get(
        "page", request.GET.get("page", page_number)
    )
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        # "edit_contact.html",
        "edit_contact_css.html",
        {
            "contacts": page_obj,
            "success": success,
            "updated_contact_id": contact_id,
        },
    )


def delete_Amiibo(request, contact_id, page_number):
    print("[DBG] delete_contact called for ID:", contact_id)
    if request.method == "POST":
        Amiibo = get_object_or_404(Amiibo, id=contact_id)
        Amiibo.delete()
        # Redirect to the same page number after delete
        return redirect("edit_contact", contact_id=contact_id, page_number=page_number)
