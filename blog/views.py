from django.shortcuts import render, get_object_or_404, redirect
from .models import Konten
from django.core.paginator import Paginator, EmptyPage, \
                                    PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailKontenForm
from django.core.mail import send_mail

# List View dengan class based view:
"""
class KontenListView(ListView):
    queryset = Konten.dimuat.all()
    context_object_name = 'kontenSemua'
    paginate_by = 3
    template_name = 'blog/konten/list.html'
"""

# List View dengan function based view:
def konten_list(request):
    object_list = Konten.dimuat.all()
    paginator = Paginator(object_list, 3) # 3 kontenSemua in each page
    halaman = request.GET.get('halaman')
    try:
        kontenSemua = paginator.page(halaman)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        kontenSemua = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        kontenSemua = paginator.page(paginator.num_pages)
    return render(request,
                    'blog/konten/list.html',
                    {'halaman': halaman,
                    'kontenSemua' : kontenSemua})


def konten_detail(request, year, month, day, konten):
    konten = get_object_or_404(Konten, slug = konten,
                                    status = 'dimuat',
                                    terbit__year = year,
                                    terbit__month = month,
                                    terbit__day = day)
    return render(request,
                'blog/konten/detail.html',
                {'konten' : konten})

def konten_share(request, konten_id):
    # Retrieve konten by id
    konten = get_object_or_404(Konten, id=konten_id, status='dimuat')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailKontenForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            konten_url = request.build_absolute_uri(
                konten.get_absolute_url())
            subject = f"{cd['nama']} merekomendasikanmu untuk membaca " \
                    f"{konten.judul}"
            message = f"Baca {konten.judul} pada {konten_url}\n\n" \
                    f"Komentar dari {cd['nama']}: {cd['catatan']}"
            send_mail(subject, message, 'crazydinosaur86@gmail.com',
                    [cd['email_pengirim']])
            sent = True

    else:
        form = EmailKontenForm()
    return render(request, 'blog/konten/share.html', {'konten': konten,
                                                    'form': form,
                                                    'sent': sent})

# Ini cara pertama untuk redirect ke blog/ :
def langsung_blog(request):
    response = redirect('blog/')
    return response
