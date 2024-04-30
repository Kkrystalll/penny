from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Nanny
from .forms import NannyForm
from django.views.generic import FormView, ListView


class IndexView(ListView):
    model = Nanny

    def get_queryset(self):
        queryset = super().get_queryset()
        keyword = self.request.GET.get("keyword", "").strip()

        return queryset.filter(name__icontains=keyword)


def show(request, id):
    nanny = get_object_or_404(Nanny, pk=id)

    if request.method == "POST":
        form = NannyForm(request.POST, instance=nanny)

        if form.is_valid():
            form.save()
            messages.success(request, "更新成功")

        return redirect("nannies:show", id=nanny.id)
    else:
        return render(request, "nannies/show.html", {"nanny": nanny})


class NewView(FormView):
    form_class = NannyForm
    template_name = "nannies/new.html"


def edit(request, id):
    nanny = get_object_or_404(Nanny, pk=id)

    form = NannyForm(instance=nanny)

    return render(request, "nannies/edit.html", {"nanny": nanny, "form": form})


@require_POST
def create(request):
    form = NannyForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(request, "新增成功")

    return redirect("nannies:index")


@require_POST
def delete(request, id):
    nanny = get_object_or_404(Nanny, pk=id)
    nanny.delete()

    messages.error(request, "資料已刪除！")
    return redirect("nannies:index")
