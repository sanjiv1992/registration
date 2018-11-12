from rest_framework import serializers
from testing.models import User

class UserSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=User
        fields=('firstname', 'lastname', 'email', 'location')