import os
import traceback
import requests

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from threading import Thread, Lock
import pandas as pd
import importlib.util
import json

from django.views.decorators.csrf import csrf_exempt

from Tester.backtest import Backtest

BASE_SERVER_URL = 'http://127.0.0.1:8000/'


class BacktestThread(Thread):
    def __init__(self, backtest, counter_lock, sim_id):
        super().__init__()
        self.sim_id = sim_id
        self.backtest = backtest
        self.counter_lock = counter_lock

    def run(self):
        result = {}
        try:
            result = self.backtest.run()
            result['status'] = 'success'
        except:
            result['status'] = 'failure'
            result['msg'] = traceback.format_exc()
        finally:
            print(result)

            response = requests.post(url=BASE_SERVER_URL + 'set-sim-status/', data={
                'id': self.sim_id,
                'status': json.dumps(result)
            })

            with self.counter_lock:
                BacktestView.thread_counter -= 1


@method_decorator(csrf_exempt, name='dispatch')
class BacktestView(View):
    thread_counter = 0
    counter_lock = Lock()

    # Moze da se zada iz okruzenja, vrednost 5 je fallback
    try:
        max_threads = int(os.environ['MAX_SIMULACIJE'])
    except (KeyError, ValueError):
        max_threads = 5

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        sim_id = data['id']
        csv_path = data['csv_path']
        module_path = data['module_path']

        if not csv_path or not module_path or not sim_id:
            return JsonResponse({'msg': 'los zahtev!'}, status=400)

        with self.counter_lock:
            if self.thread_counter >= self.max_threads:
                return JsonResponse({'msg': 'sistem je preopterecen'}, status=429)

            self.thread_counter += 1

        try:
            csv_full_path = os.getcwd()[:-10] + 'Projekat\\' + csv_path.replace('/', '\\')
            print(csv_full_path)
            ticks = pd.read_csv(csv_full_path).to_dict(orient='records')

            spec = importlib.util.spec_from_file_location("strategy_module", module_path)
            strategy_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(strategy_module)
            strategy = strategy_module.Strategy()

            backtest = Backtest(ticks, strategy)
            thread = BacktestThread(backtest, self.counter_lock, sim_id)
            thread.start()

            return JsonResponse({'message': 'Backtest started'})
        except FileNotFoundError:
            return JsonResponse({'msg': 'los zahtev!'}, status=400)
