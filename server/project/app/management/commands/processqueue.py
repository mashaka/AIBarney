import signal
import time

from django.core.management.base import BaseCommand, CommandError

from app.methods import process_queue, stop_processing

class Command(BaseCommand):
    args = '[cnt]'
    help = 'Process job queue'

    def sig_handler(self, sig, frame):
        """Catch signal and init callback"""
        stop_processing()

    def handle(self, *args, **options):
        #signal.signal(signal.SIGTERM, self.sig_handler)
        #signal.signal(signal.SIGINT, self.sig_handler)
        if len(args) == 1:
            try:
                process_queue(int(args[0]))
            except ValueError:
                raise CommandError('Invalid arg')
        elif len(args) == 0:
            process_queue()
        else:
            raise CommandError('Too many args')

