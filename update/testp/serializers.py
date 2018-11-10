
from rest_framework import serializers
from testp.models import userform

class userserializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model=userform
        fields=('username', 'password', 'discription')
