from django.core import management
from django.core.management.base import BaseCommand
from intake.models import pdfs
from intake.tests import mock


class Command(BaseCommand):
    help = str(
        "Sets up seeds based on what environment it runs in.")

    def handle(self, *args, **kwargs):
        management.call_command(
            'loaddata',
            'mock_profiles',
            'mock_2_submissions_to_a_pubdef',
            'mock_2_submissions_to_ebclc',
            'mock_2_submissions_to_cc_pubdef',
            'mock_2_submissions_to_sf_pubdef',
            'mock_2_submissions_to_monterey_pubdef',
            'mock_2_submissions_to_solano_pubdef',
            'mock_2_submissions_to_san_diego_pubdef',
            'mock_2_submissions_to_san_joaquin_pubdef',
            'mock_2_submissions_to_santa_clara_pubdef',
            'mock_2_submissions_to_santa_cruz_pubdef',
            'mock_2_submissions_to_fresno_pubdef',
            'mock_2_submissions_to_sonoma_pubdef',
            'mock_2_submissions_to_tulare_pubdef',
            'mock_1_submission_to_multiple_orgs',
            'mock_1_bundle_to_a_pubdef',
            'mock_1_bundle_to_ebclc',
            'mock_1_bundle_to_sf_pubdef',
            'mock_1_bundle_to_cc_pubdef',
            'mock_1_bundle_to_monterey_pubdef',
            'mock_1_bundle_to_solano_pubdef',
            'mock_1_bundle_to_san_diego_pubdef',
            'mock_1_bundle_to_san_joaquin_pubdef',
            'mock_1_bundle_to_santa_clara_pubdef',
            'mock_1_bundle_to_santa_cruz_pubdef',
            'mock_1_bundle_to_fresno_pubdef',
            'mock_1_bundle_to_sonoma_pubdef',
            'mock_1_bundle_to_tulare_pubdef',
            'mock_application_events')
        if pdfs.FillablePDF.objects.count() == 0:
            mock.fillable_pdf()
