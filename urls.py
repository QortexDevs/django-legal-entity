from django.urls import path
from django.apps import apps

from .views import GetLegalEntityInfoByInnView, GetBankInfoByBikView

app_name = 'legal_entity'

api_urlpatterns = [
    path(app_name + '/get_legal_entity_info_by_inn',
         GetLegalEntityInfoByInnView.as_view()),
    path(app_name + '/get_bank_info_by_bik',
         GetBankInfoByBikView.as_view()),
]
