#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":

    try:
        import sequence_field
        # Nice, the import worked. It must be installed somewhere else.
        del sequence_field
    except ImportError:
        # Let's try adding the parent directory
        PARENT_DIR = os.path.realpath(
            os.path.join(os.path.dirname(__file__), '..')
        )
        sys.path.insert(1, PARENT_DIR)
        import sequence_field


    #print "It all works"
    #print sys.path
    #sys.exit()

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
