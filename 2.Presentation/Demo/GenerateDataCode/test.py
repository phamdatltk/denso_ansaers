import random

def generate_cyclic_load_data(min_value_range, max_value_range, steps_per_cycle):
    """
    Tạo dữ liệu chu kỳ cho tải trọng máy ép.
    - min_value_range: khoảng giá trị cực tiểu (vd: [900, 1100]).
    - max_value_range: khoảng giá trị cực đại (vd: [4000, 4500]).
    - steps_per_cycle: số bước trong mỗi chu kỳ (vd: 10 bước).
    """
    min_value = random.randint(min_value_range[0], min_value_range[1])
    max_value = random.randint(max_value_range[0], max_value_range[1])
    
    print(f"Min value selected: {min_value}")
    print(f"Max value selected: {max_value}")
    
    # Sinh các giá trị tăng dần từ min_value đến max_value
    increasing_part = [int(min_value + i * (max_value - min_value) / (steps_per_cycle - 1)) for i in range(steps_per_cycle)]
    
    print(f"Increasing part: {increasing_part}")
    
    # Kết hợp hai phần thành một chu kỳ hoàn chỉnh
    full_cycle = increasing_part  # Loại bỏ phần tử trùng lặp ở giữa
    
    return full_cycle

# Khởi tạo danh sách cyclic_load_data
cyclic_load_data = []

# Tạo dữ liệu 10 lần và append từng phần tử vào mảng cyclic_load_data
for i in range(1000):
    generated_data = generate_cyclic_load_data(min_value_range=[900, 1100], max_value_range=[4000, 4500], steps_per_cycle=10)
    
    # Thêm từng phần tử của generated_data vào cyclic_load_data
    cyclic_load_data.extend(generated_data)
# In ra mảng dữ liệu giả lập
print(f"Generated cyclic load data: {cyclic_load_data}")
