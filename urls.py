from django.urls import path
from .views import GetLegalEntityInfoByInnView, GetBankInfoByBikView

urlpatterns = [
    path('2.0/get_legal_entity_info_by_inn',
         GetLegalEntityInfoByInnView.as_view()),
    path('2.0/get_bank_info_by_bik',
         GetBankInfoByBikView.as_view()),
]
