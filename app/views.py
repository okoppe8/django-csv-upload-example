import csv
import io

from django.http import HttpResponse
from django.views.generic import FormView

from .forms import UploadForm


# Create your views here.
class UploadView(FormView):
    form_class = UploadForm
    template_name = 'app/UploadForm.html'

    def form_valid(self, form):
        csvfile = io.TextIOWrapper(form.cleaned_data['file'])

        # ここを必要な処理に変える
        reader = csv.reader(csvfile)
        count = sum(1 for row in reader)
        result = 'データ件数は{}件です'.format(count)

        response = HttpResponse(result, content_type='text/plain')
        response['Content-Disposition'] = 'attachment; filename = "result.txt"'

        return response
