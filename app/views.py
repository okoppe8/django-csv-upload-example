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

        # この部分をあなたのコードに差し替えます。
        reader = csv.reader(csvfile)
        count = sum(1 for row in reader)
        result = 'データ件数は{}件です'.format(count)

        # 結果をブラウザに表示させたいときはこちら
        return self.render_to_response(self.get_context_data(result=result))

        # 結果をテキストファイルでダウンロードさせたいときはこちら
        # response = HttpResponse(result, content_type='text/plain')
        # response['Content-Disposition'] = 'attachment; filename = "result.txt"'
        # return response
