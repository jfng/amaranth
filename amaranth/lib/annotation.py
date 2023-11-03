import jsonschema
from abc import abstractmethod, ABCMeta


__all__ = ["Annotation"]


class Annotation(metaclass=ABCMeta):
    name   = property(abstractmethod(lambda: None))
    schema = property(abstractmethod(lambda: None))

    @abstractmethod
    def as_json(self):
        pass

    @classmethod
    def validate(cls, instance):
        return jsonschema.validate(instance, schema=cls.schema)
