from os.path import join, dirname, abspath
import logging
import time
from typing import Dict

from water_rights_visualizer import water_rights_visualizer

from .tasks import Task, update_task

CLIENT_SECRETS_FILENAME = join(abspath(dirname(__file__)), "..", "client_secrets.json")
GOOGLE_DRIVE_KEY_FILENAME = join(abspath(dirname(__file__)), "..", "google_drive_key.txt")

logger = logging.getLogger(__name__)


def run_water_rights_task(task_ID: str, target_geometry_filename: str, working_directory: str, task: Dict):
    update_task(task_ID, task)
    logger.info(f"starting water rights task {task_ID}")
    logger.info(f"working directory for task {task_ID}: {working_directory}")
    logger.info(f"target geometry file for task {task_ID}: {target_geometry_filename}")
    task["attributes"]["progress"] = "calling water rights visualizer tool"

    google_drive_temporary_directory = join(working_directory, "google_drive")

    water_rights_visualizer(
        boundary_filename=target_geometry_filename,
        output_directory=working_directory,
        google_drive_temporary_directory=google_drive_temporary_directory,
        google_drive_key_filename = GOOGLE_DRIVE_KEY_FILENAME,
        google_drive_client_secrets_filename = CLIENT_SECRETS_FILENAME
    )

    # # FIXME insert water rights tool call here
    # for i in range(20):
    #     time.sleep(1)
    #     task["status"] = "running"
    #     task["attributes"]["progress"] = f"{5 * i}%"
    #     update_task(task_ID, task)

    task["status"] = "success"
    task["attributes"]["progress"] = "100%"
    output = f"output from task {task_ID}"
    task["attributes"]["output"] = output
    update_task(task_ID, task)

def run_water_rights_task_dummy(task_ID: str, target_geometry_filename: str, working_directory: str, task: Dict):
    update_task(task_ID, task)
    logger.info(f"starting water rights task {task_ID}")
    logger.info(f"working directory for task {task_ID}: {working_directory}")
    logger.info(f"target geometry file for task {task_ID}: {target_geometry_filename}")
    # task["attributes"]["progress"] = "calling water rights visualizer tool"

    # google_drive_temporary_directory = join(working_directory, "google_drive")

    # water_rights_visualizer(
    #     boundary_filename=target_geometry_filename,
    #     output_directory=working_directory,
    #     google_drive_temporary_directory=google_drive_temporary_directory,
    #     google_drive_key_filename = GOOGLE_DRIVE_KEY_FILENAME,
    #     google_drive_client_secrets_filename = CLIENT_SECRETS_FILENAME
    # )

    # FIXME insert water rights tool call here
    for i in range(20):
        time.sleep(1)
        task["status"] = "running"
        task["attributes"]["progress"] = f"{5 * i}%"
        update_task(task_ID, task)

    task["status"] = "success"
    task["attributes"]["progress"] = "100%"
    output = f"output from task {task_ID}"
    task["attributes"]["output"] = output
    update_task(task_ID, task)