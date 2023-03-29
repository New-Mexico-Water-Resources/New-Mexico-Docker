import logging
import time
from typing import Dict

from .tasks import Task, update_task

logger = logging.getLogger(__name__)


def run_water_rights_task(task_ID: str, target_geometry_filename: str, working_directory: str, task: Dict):
    update_task(task_ID, task)
    logger.info(f"starting water rights task {task_ID}")
    logger.info(f"working directory for task {task_ID}: {working_directory}")
    logger.info(f"target geometry file for task {task_ID}: {target_geometry_filename}")

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
