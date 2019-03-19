from django.urls import path
from .apiviews import PollList, PollDetail, ChoiceList, CreateVote, UserCreate
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, LoginView
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls

router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls')
schema_view = get_swagger_view(title='Polls API')

urlpatterns = [
    path("polls/", PollList.as_view(), name="polls_list"),
    path("polls/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="polls_list"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
    path(r'swagger-docs/', schema_view),
    path(r'docs/', include_docs_urls(title="Polls API")),
]

urlpatterns += router.urls
