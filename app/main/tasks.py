# based on https://ivanyu2021.hashnode.dev/a-simple-approach-for-background-task-in-django

import threading
from enum import Enum
from logging import getLogger
from typing import Union, Dict
from django.core.cache import cache

logger = getLogger(__name__)


# class TaskStatus(Enum):
#     started = "started"
#     running = "running"
#     success = "success"


class Task:
    def __init__(self, task_ID: str, method, args):
        logger.info(f"creating task ID: {task_ID}")
        thread = threading.Thread(target=method, args=[*args, self])
        thread.setDaemon(True)
        thread.start()

        # self.thread = thread
        self.task_ID = task_ID
        self.status = "started"
        self.attributes = {}

    def set(self,
            status: str,
            attributes: Dict = None):
        self.status = status
        self.attributes.update(attributes)
        cache.set(self.task_ID, self, 3600)


# class TaskManager:
#     def __init__(self):
#         self.tasks = {}

def start_task(task_ID: str, attributes: Dict, method, args) -> Dict:
    print(f"creating task ID: {task_ID}")
    task = {"task_ID": task_ID, "status": "started", "attributes": attributes}
    thread = threading.Thread(target=method, args=[*args, task])
    thread.setDaemon(True)
    thread.start()
    cache.set(task_ID, task, 3600)
    print(f"task ID {task_ID} added")

    return task

def update_task(task_ID: str, task: Dict):
    print(f"updating task {task_ID}: {task}")
    cache.set(task_ID, task, 3600)

def get_task(task_ID: str) -> Dict:
    return cache.get(task_ID)
