from rest_framework import serializers

class CalculationSerializer(serializers.Serializer):
    OPERATION_CHOICES = [
        ('add', 'Addition'),
        ('subtract', 'Subtraction'),
        ('multiply', 'Multiplication'),
        ('divide', 'Division'),
        ('power', 'Power'),
        ('sqrt', 'Square Root'),
    ]

    operation = serializers.ChoiceField(choices=OPERATION_CHOICES)
    a = serializers.FloatField()
    b = serializers.FloatField(required=False)

    def validate(self, data):
        operation = data.get('operation')
        b = data.get('b')

        if operation != 'sqrt' and b is None:
            raise serializers.ValidationError({"b": "This field is required for the chosen operation."})
        
        return data
