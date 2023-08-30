import csv
import os

import numpy as np
from django.shortcuts import render, redirect
from matplotlib import pyplot as plt
import pandas as pd

from StrategyPlayground.models import Podaciotrzistu


def prikaz_informacija(request):
    file_names = []
    file_contains = []

    context = {}

    moji_podaci = Podaciotrzistu.objects.filter(
        idkor=request.user.idkor
    )

    putanja = "StrategyPlayground/static/" + request.user.email.replace('@', '_') + "/PodaciOCeni/"

    for podaci in moji_podaci:
        if os.path.isfile(podaci.imefajla):
            file_names.append(str(podaci))

            csv_file_path = podaci.imefajla

            try:
                with open(csv_file_path, 'r') as file:
                    csv_data = csv.reader(file)

                    contain_string = ""

                    for row in csv_data:
                        for r in row:
                            contain_string += str(r) + ","

                    file_contains.append(contain_string[:-1])

                    print("CSV file processed successfully.")

            except Exception as e:
                print(str(e))

    # fajlovi sa istorijskim podacima

    filesWithHystoricData = file_names
    fileContainings = file_contains

    # chart
    if request.method == 'POST':
        if 'imeFajlaZaCrtanje' in request.POST:
            file_name = request.POST.get('imeFajlaZaCrtanje')
            filepath = putanja + file_name

            # Read the CSV file
            ticks = pd.read_csv(filepath).to_dict(orient='records')
            first = ticks[0]
            data = []

            if 'Price' in first:
                data = [tick['Price'] for tick in ticks]
            elif 'Bid' in first and 'Ask' in first:
                data = [(tick['Bid'] + tick['Ask']) / 2. for tick in ticks]
            elif 'Open' in first and 'High' in first and 'Low' in first and 'Close' in first:
                data = [(tick['Open'] + tick['High'] + tick['Close']) / 3. for tick in ticks]

            # print("d1: " + str(data))
            np_array = np.array(data)

            plt.clf()
            plt.plot(np_array)

            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.title('Data Visualization')

            folder_path = "StrategyPlayground/static/chart.png"
            os.remove(folder_path)
            plt.savefig(folder_path)

            print("draw file " + file_name)
            context['draw'] = True
        # else:
        #     print('draw avoided')

    # file upload
    if request.method == 'POST':
        if request.FILES:
            csv_file = request.FILES['csv_file']
            print('sucess upload')

            filename = csv_file.name

            if not os.path.exists(putanja):
                os.makedirs(putanja)
            filepath = putanja + filename

            podaci = Podaciotrzistu(
                idkor=request.user,
                imefajla=filepath
            )

            with open(filepath, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            podaci.save()

            return redirect('prikaz_informacija')
    #     else:
    #         print("upload avoided")
    # else:
    #     print('failed upload')

    # rewriting data
    if request.method == 'POST':
        if 'sadrzajInputString' in request.POST:
            string_value = request.POST.get('sadrzajInputString')

            file_name = request.POST.get('imeFajla')
            filepath = "StrategyPlayground/static/PodaciOCeni/" + file_name

            with open(filepath, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([string_value])

            print("changed file")
    #     else:
    #         print('rewrite avoided')
    #
    # else:
    #     print("not changed file")

    # deleting file
    if request.method == 'POST':
        if 'imeFajlaZaBrisanje' in request.POST:
            file_name = request.POST.get('imeFajlaZaBrisanje')
            filepath = putanja + file_name

            Podaciotrzistu.objects.filter(imefajla=filepath).first().delete()

            if os.path.exists(filepath):
                os.remove(filepath)

            # file_to_delete = Podaciotrzistu.objects.get(idkor=request.user.idkor, imefajla=filepath)
            # file_to_delete.delete()

            print("deleted file " + file_name)

            return redirect('prikaz_informacija')
    #     else:
    #         print('delete avoided')
    # else:
    #     print("not changed file")

    # context
    filesAndContainings = zip(filesWithHystoricData, fileContainings)

    context['filesAndContainings'] = filesAndContainings

    return render(request, 'prikaz_informacija.html', context)
