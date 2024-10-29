from django.db.models import Case, When, Value, IntegerField
from django.apps import apps


def get_sort(model, date_field_name, descending=True):
    desc = ''
    if descending:
        desc = '-'

    return model.objects.annotate(
        is_in_progress=Case(
            # Check if the date field is None
            When(**{date_field_name: None}, then=Value(1)),
            default=Value(0),                                 # Default case
            output_field=IntegerField(),
        )
        # Sort by in-progress first, then by date
    ).order_by('-is_in_progress', desc + date_field_name)


def get_last_update():
    # Retrieve all models in the app
    all_models = apps.get_models()

    latest_times = []

    for model in all_models:
        # Check if the model has a last_updated field
        if hasattr(model, 'last_updated'):
            # Retrieve the most recent update timestamp
            latest_instance = model.objects.order_by('-last_updated').first()
            if latest_instance:
                latest_times.append(latest_instance.last_updated)

    # Get the most recent date (or None if no objects)
    last_updated_time = max(latest_times) if latest_times else None
    return last_updated_time
