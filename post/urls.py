from django.urls import path
from . import views
from .models import Car
from .document import CarDocument, ExamQuestionDocument, ExamAnswerDocument
from elasticsearch_dsl.query import MultiMatch

urlpatterns = [
    # path('search/', views.search, name='search'),
]

search_text = "bombay"
# query = MultiMatch(query=search_text)
# cars = ExamQuestionDocument.search().query(query).to_queryset()
# print(cars)
# for car in cars:
#     print(car)

search_query = MultiMatch(query=search_text, fields=['question', 'name'], fuzziness='AUTO')
cars = CarDocument.search().query(search_query).to_queryset()
question = ExamQuestionDocument.search().query(search_query).to_queryset()
print(cars)
print(question)
for car in cars:
    print(car.name, car.color, car.description, car.type)

# search exam questions
# search_query = MultiMatch(query=search_text, fields=['question'], fuzziness='AUTO')
# print(search_query.to_dict())
# questions = ExamQuestionDocument.search().query(search_query).to_queryset()
# print(questions)