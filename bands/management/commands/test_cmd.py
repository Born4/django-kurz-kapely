from django.core.management import BaseCommand
import os


class Command(BaseCommand):
    def add_arguments(self, parser):
        """Parametrizace prikazu v souvislosti s export/import soubory"""
        # Import file redirection
        parser.add_argument('-F', '--file_name',
                            type=str,
                            help='Cesta k souboru, kde se nachazeji data pro import '
                                 '(ignoruji se implicitni adresare modulu pro import)')
        parser.add_argument('-A', '--all',
                            action='store_true',
                            help='Export/Import operation on all implemented django puzzle modules')
        # Predavam jmena jednotlivych tabulek s kategoriemi
        parser.add_argument('-M', '--modules',
                            type=str,
                            help='List of django puzzle modules, comma separated, for which we make export/import operation')

    def handle(self, *args, **kwargs):
        """Handle data file patrameter

        :param args:
        :param kwargs:
        :return: message if file exists or empty string if not
        """
        self.stdout.write("AHOJ MUJ PRVNI MANAGEMENT COMMAND")

        # manage command outputs
        output = ["----- argumenty -----",
                  f"args: {args}",
                  f"kwargs: {kwargs}",
                  "---------------------"]

        return '\n'.join(output)
