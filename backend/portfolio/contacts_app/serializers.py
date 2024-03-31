from rest_framework import serializers
from contacts_app.models import Contact, ContactInfo, Phone


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phone
        exclude = ("id", "contact")


class ContactInfoSerializer(serializers.ModelSerializer):
    phones = serializers.SerializerMethodField()

    class Meta:
        model = ContactInfo
        fields = ("country", "city", "email", "phones")

    def get_phones(self, obj):
        return (PhoneSerializer(phone).data for phone in obj.phones.all())


class ContactSerializer(serializers.ModelSerializer):
    date_recive = serializers.DateField()

    class Meta:
        model = Contact
        exclude = ("id", "is_read")
