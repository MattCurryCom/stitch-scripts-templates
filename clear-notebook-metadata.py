#!/usr/bin/env python

# Helper script to clear `metadata` field from all template notebooks.

import json
import logging
import os
from os.path import join
import shutil
import time

TEMPLATE_BASE_PATH = './templates'

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

def clear_metadata(filename):
    logging.info("Clearing metadata from {}".format(filename))

    backup_filename = "{}.{}.bak".format(filename, time.time())
    shutil.copy(filename, backup_filename)

    with open(filename, "r") as f:
        notebook_content = json.loads(f.read())

    with open(filename, "w") as f:
        notebook_content["metadata"] = {}
        notebook_json_str = json.dumps(notebook_content, indent=2)
        notebook_json_str += "\n"
        f.write(notebook_json_str)

    os.remove(backup_filename)

counter = 0
for root, dirs, files in os.walk(TEMPLATE_BASE_PATH):
    for name in files:
        if name == 'template.ipynb':
            filename = join(root, name)
            counter += 1
            clear_metadata(filename)

logging.info("Cleared metadata for {} templates".format(counter))
