from django.shortcuts import render
from topFive.models import TopFive

# Create your views here.
def novelSeriesIndex(request):
    lotrs = TopFive.objects.filter(seriesTitle="The Lord of The Rings")
    sots = TopFive.objects.filter(seriesTitle="The Sword of Truth")
    hps = TopFive.objects.filter(seriesTitle="Harry Potter")
    tdfs = TopFive.objects.filter(seriesTitle="The Dresden Files")
    otherlands = TopFive.objects.filter(seriesTitle="Otherland")
    context = {
        'lotrs': lotrs,
        'sots': sots,
        'hps': hps,
        'tdfs': tdfs,
        'otherlands': otherlands
    }
    return render(request, 'novelSeriesIndex.html', context)

def novelSeriesDetail(request, pk):
    novel = TopFive.objects.get(pk=pk)
    context = {
        'novel': novel
    }
    return render(request, 'novelSeriesDetail.html', context)
