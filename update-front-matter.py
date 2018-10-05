#!/usr/bin/env python

# Helper script to copy template front matter from bare template into minimal
# example templates.

import logging
import json
import os
import shutil
import time

TEMPLATE_BASE_PATH = './templates'

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

bare_template_filename = "{}/bare/template.ipynb".format(TEMPLATE_BASE_PATH)
with open(bare_template_filename, "r") as f:
    logging.info("Loading front matter from {}".format(bare_template_filename))
    notebook_content = json.loads(f.read())
    front_matter = notebook_content["cells"][0]

templates_to_update = ["minimal_postgresql", "minimal_bigquery", "minimal_snowflake"]

for template in templates_to_update:
    template_filename = "{}/{}/template.ipynb".format(TEMPLATE_BASE_PATH, template)
    logging.info("Updating front matter in {}".format(template_filename))

    backup_filename = "{}.{}.bak".format(template_filename, time.time())
    shutil.copy(template_filename, backup_filename)

    with open(template_filename, "r") as f:
        notebook_content = json.loads(f.read())

    with open(template_filename, "w") as f:
        notebook_content["cells"][0] = front_matter
        notebook_json_str = json.dumps(notebook_content, indent=2)
        notebook_json_str += "\n"
        f.write(notebook_json_str)

    os.remove(backup_filename)

logging.info("Updated front matter for {} templates".format(len(templates_to_update)))
