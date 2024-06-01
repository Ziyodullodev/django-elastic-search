from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Car, ExamQuestion, ExamAnswer


@registry.register_document
class CarDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'cars'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Car # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'name',
            'color',
            'description',
            'type',
        ]


@registry.register_document
class ExamQuestionDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'exam_questions'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0,
                    }

    class Django:
        model = ExamQuestion
        fields = [
            'question',
            'created_at',
        ]


@registry.register_document
class ExamAnswerDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'exam_answers'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = ExamAnswer
        fields = [
            'answer',
            'is_correct',
        ]