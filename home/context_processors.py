from home.models import Me


def me_context(request):
    # Ensure that `Me` exists to prevent errors if no instance is available.
    try:
        me_instance = Me.objects.get()
    except Me.DoesNotExist:
        me_instance = None  # Handle no `Me` instance case

    # Return it in a dictionary so it's available as 'me' in templates
    return {'me': me_instance}
