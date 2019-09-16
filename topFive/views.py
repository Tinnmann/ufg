from django.shortcuts import render
from topFive.models import TopFive

# Create your views here.
def novelSeriesHome(request):
    return render(request, 'novelSeriesHome.html', {})

def novelSeriesIndex(request):
    lotrs = TopFive.objects.get(seriesTitle="The Lord of The Rings")
    sots = TopFive.objects.get(seriesTitle="The Sword of Truth")
    hps = TopFive.objects.get(seriesTitle="Harry Potter")
    tdfs = TopFive.objects.get(seriesTitle="The Dreden Files")
    otherlands = TopFive.objects.get(seriesTitle="Otherland")
    context = {
        'lotrs': lotrs,
        'sots': sots,
        'hps': hps,
        'tdfs': tdfs,
        'otherlands': otherlands
    }
    return render(request, 'novelSeriesIndex.html', context)

def novelSeriesDetail(request, pk):
    lotr = TopFive.objects.get(seriesTitle="The Lord of The Rings", pk=pk)
    sot = TopFive.objects.get(seriesTitle="The Sword of Truth", pk=pk)
    hp = TopFive.objects.get(seriesTitle="Harry Potter", pk=pk)
    tdf = TopFive.objects.get(seriesTitle="Otherland", pk=pk)
    otherland = TopFive.objects.get(seriesTitle="Otherland", pk=pk)
    context = {
        'lotr': lotr,
        'sot': sot,
        'hp': hp,
        'tdf': tdf,
        'otherland': otherland
    }
    return render(request, 'novelSeriesDetail.html', context)
