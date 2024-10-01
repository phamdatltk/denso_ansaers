import time
import random
import requests
from datetime import datetime

# URL của VictoriaMetrics Push API
victoria_metrics_url = 'http://localhost:37275/api/v1/import/prometheus'

# Hàm generate tải trọng chu kỳ
def generate_load_cycle(min_load, max_load, cycle_duration=5, step=1):
    """
    Tạo tải trọng chu kỳ tăng giảm theo thời gian.
    - min_load: tải trọng thấp nhất.
    - max_load: tải trọng cao nhất.
    - cycle_duration: thời gian hoàn thành một chu kỳ (giây).
    - step: số giây mỗi bước tăng hoặc giảm.
    """
    while True:
        # Tăng dần đến max_load
        for load in range(min_load, max_load, step):
            yield load
        # Giảm dần về min_load
        for load in range(max_load, min_load, -step):
            yield load

# Hàm gửi dữ liệu đến VictoriaMetrics
def send_to_victoriametrics(metric_name, load_value, timestamp):
    """
    Gửi dữ liệu tải trọng và timestamp đến VictoriaMetrics.
    """
    data = f'{metric_name} {load_value} {int(timestamp.timestamp())}\n'
    
    try:
        response = requests.post(victoria_metrics_url, data=data)
        if response.status_code == 200 or response.status_code == 204:
            print(f"Dữ liệu đã được gửi: {data.strip()}")
        else:
            print(f"Lỗi khi gửi dữ liệu: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Lỗi kết nối tới VictoriaMetrics: {e}")

# Cấu hình các tham số chu kỳ
min_load = 1000  # Đơn vị N
max_load = 5000  # Đơn vị N
cycle_duration = 5  # Một chu kỳ là 60 giây (tăng và giảm)
step = 1000  # Tăng/giảm tải trọng mỗi 5 giây

# Tạo generator cho chu kỳ tải trọng
load_generator = generate_load_cycle(min_load, max_load, cycle_duration, step)

# Bắt đầu sinh và gửi dữ liệu theo thời gian thực
while True:
    # Lấy tải trọng từ generator
    load = next(load_generator)
    
    # Lấy thời gian hiện tại
    timestamp = datetime.now()
    
    # Gửi dữ liệu tới VictoriaMetrics
    send_to_victoriametrics('machine_load', load, timestamp)
    
    # Chờ một khoảng thời gian trước khi sinh dữ liệu tiếp theo (giả lập chu kỳ)
    time.sleep(step)
