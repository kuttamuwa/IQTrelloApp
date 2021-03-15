"""
Uygulama icin custom mongodb sutunlari. ObjectID icin gerekli.
see: https://github.com/nesdis/djongo/issues/298
"""
from django.utils.encoding import smart_text
from rest_framework import serializers
from bson import ObjectId
from bson.errors import InvalidId


class ObjectIdField(serializers.Field):
    """ Serializer field for Djongo ObjectID fields """

    def to_internal_value(self, data):
        # Serialized value -> Database value
        try:
            return ObjectId(str(data))  # Get the ID, then build an ObjectID instance using it
        except InvalidId:
            raise serializers.ValidationError(
                '`{}` gecerli bir ObjectID degil !'.format(data))

    def to_representation(self, value):
        # Database value -> Serialized value
        if not ObjectId.is_valid(value):  # User submitted ID's might not be properly structured
            raise InvalidId
        return smart_text(value)
