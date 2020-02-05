import csv
import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseForbidden

from intake.models import FormSubmission


@login_required
def email_csv(request):
    # @NOTE: check the clips app, it may need a security update
    if not request.user.has_perm('clips.change_clip'):
        return HttpResponseForbidden()
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d-%H-%M")
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = \
        'attachment; filename="cmr-emails-%s.tsv"' % now_str
    writer = csv.writer(response, delimiter='\t', quoting=csv.QUOTE_MINIMAL)

    headers = [
        'ID',
        'Submission date',
        'Email',
        'Phone number',
        'Contact preferences',
        'Counties',
        'How did you hear',
        'Anything else we should know',
        'Last Status Update At',
        'Last Status',
        'Number of applications granted'
    ]

    writer.writerow(headers)
    subs = FormSubmission.objects.all()

    for sub in subs:
        number_granted = 0
        last_status = None
        for app in sub.applications.all():
            number_granted += app.status_updates.filter(
                status_type__slug='granted').count()

            app_status = app.status_updates.\
                order_by('-updated').first()
            print(app_status)
            if (app_status and not last_status) or (
                    app_status and last_status and
                    app_status.updated > last_status.updated):
                last_status = app_status
        if last_status:
            last_status_name = last_status.status_type.display_name,
            last_status_date = last_status.updated,
        else:
            last_status_name = None
            last_status_date = None

        columns = [
            sub.id,
            sub.date_received,
            sub.email,
            sub.phone_number,
            sub.contact_preferences,
            '\n'.join(list(sub.organizations.values_list('name', flat=True))),
            sub.how_did_you_hear,
            sub.additional_information,
            last_status_date,
            last_status_name,
            number_granted
        ]

        writer.writerow(columns)
    return response
