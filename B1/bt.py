def check_time(time_str):
        parts = time_str.split(":")
        
        # Kiểm tra đủ 3 phần
        if len(parts) != 3:
            return "Không hợp lệ"
        
        h, m, s = map(int, parts)
        
        # Kiểm tra điều kiện
        if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
            return "Hợp lệ"
        else:
            return "Không hợp lệ"