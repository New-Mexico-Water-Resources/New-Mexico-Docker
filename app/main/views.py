import json
from logging import getLogger
from os import makedirs
from os.path import splitext, join

from django.core.cache import cache
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone

from .forms import CreateListForm
from .forms import DocumentForm
from .models import Document
from .models import ToDoList
from .tasks import start_task, get_task
from .water_rights_task import run_water_rights_task

logger = getLogger(__name__)


# water_rights_task_manager = TaskManager()

def index(request, id):
    ls = ToDoList.objects.get(id=id)

    if request.method == "POST":
        if request.POST.get("save"):
            for item in ls.item_set.all():
                p = request.POST

                if "clicked" == p.get("c" + str(item.id)):
                    item.complete = True
                else:
                    item.complete = False

                if "text" + str(item.id) in p:
                    item.text = p.get("text" + str(item.id))

                item.save()

        elif request.POST.get("add"):
            newItem = request.POST.get("new")
            if newItem != "":
                ls.item_set.create(text=newItem, complete=False)
            else:
                print("invalid")

    return render(request, "main/index.html", {"ls": ls})


def get_name(request):
    if request.method == "POST":
        form = CreateListForm(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n, date=timezone.now())
            t.save()

            return HttpResponseRedirect("/%i" % t.id)

    else:
        form = CreateListForm()

    return render(request, "main/water_rights_processing.html", {"form": form})


def home(request):
    return render(request, "main/home.html", {})


def view(request):
    l = ToDoList.objects.all()
    return render(request, "main/view.html", {"lists": l})


def water_rights_upload(request):
    print("view: water_rights_upload")
    # print(f"Great! You're using Python 3.6+. If you fail here, use the right version.")
    message = 'select GeoJSON file containing water right boundary'

    form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    context = {'documents': documents, 'form': form, 'message': message, "header": "Upload Water Rights Boundary"}
    print("rendering water rights upload page")
    return render(request, 'main/water_rights_upload.html', context)


def water_rights_processing(request):
    print("view: water_rights_processing")
    # print("water_rights_processing view")
    # context = {"header": "Water Rights Processing"}
    # return render(request, "main/water_rights_processing.html", context)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            filename = str(request.FILES["docfile"])
            task_ID = splitext(filename)[0]
            # geojson = json.dumps(json.loads(request.FILES["docfile"].read().decode()), indent=2)
            target_geometry = request.FILES["docfile"].read().decode()
            working_directory = join("/water_rights_tasks", task_ID)
            print(f"creating job directory: {working_directory}")
            makedirs(working_directory)

            target_geometry_filename = join(working_directory, filename)
            print(f"writing job GeoJSON: {target_geometry_filename}")

            with open(target_geometry_filename, "w") as file:
                file.write(target_geometry)

            # FIXME start water rights run here and let it run in the background
            task = start_task(
                task_ID,
                run_water_rights_task,
                [task_ID, target_geometry_filename, working_directory]
            )

            # job_status_file = join(job_directory, "status.txt")
            #
            # with open(job_status_file, "w") as file:
            #     file.write("job created")

            # Redirect to the document list after POST
            documents = Document.objects.all()

            context = {
                "documents": documents,
                "form": form,
                "filename": filename,
                "task_ID": task_ID,
                "geojson": target_geometry,
                "error": False
            }

            print("rendering water rights processing page")
            return render(request, 'main/water_rights_processing.html', context)
        # else:
        #     message = 'The form is not valid. Fix the following error:'
    else:
        form = DocumentForm()  # An empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # message = "no water rights boundary submitted"

    # Render list page with the documents and the form
    context = {
        "documents": documents,
        "form": form,
        "filename": "",
        "geojson": "",
        "error": True
    }

    print("rendering water rights processing page")
    return render(request, 'main/water_rights_processing.html', context)


def water_rights_status(request):
    print("water_rights_status view")
    body = json.loads(request.body.decode())
    task_ID = body["task_ID"]
    print(f"task ID: {task_ID}")
    job_directory = join("/water_rights_tasks", task_ID)
    print(f"job directory: {job_directory}")
    task = get_task(task_ID)
    status = task["status"]
    print(f"status: {status}")
    attributes = task["attributes"]
    print(f"attributes: {attributes}")

    response = json.dumps({
        "status": status,
        "attributes": attributes
    })

    return HttpResponse(response, content_type="application/json")
