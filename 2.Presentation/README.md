# Tổng quan
Đây là nơi tổng hợp tài liệu cho buổi thuyết trình vòng 2

# Nội dung 
- Thông tin thu thập khi đi factory tour 2
- Tài liệu làm slide
- Demo

# Thông tin thu thập khi đi tour 2
Mục tiêu khi đi tour:
- Tìm một máy để thu thập dữ liệu 
- Hỏi sâu về quy trình dừng ngắn, dừng dài 
- Các lỗi máy móc hay gặp phải 
- Xin dữ liệu của máy móc 
  
Kết quả đạt được:
- Dữ liệu của một máy móc có rất rất nhiều trường, tuy vậy chưa có được dữ liệu luôn 
- Có 2 loại máy trong nhà máy:
  - Máy cũ: Vẫn sẽ có màn hình và đồng hồ 
  - Máy mới: Có thể truyền dữ liệu 1 phần trực tiếp, phần còn lại có thể dùng USB cắm vào máy để lấy dữ liệu ra 
- Mục tiêu: Nên tập trung làm giải pháp cho máy mới, do tính triển khai cao, chi phí thấp (Do máy cũ phải lắp các loại CAM)
- Tên của một loại máy cụ thể
`Máy ép Oilseal - d/c MCVe` - cảnh báo được tải trọng ép 

# Demo
## Thông tin về máy ép

Máy ép Oilseal - d/c MCVe là một loại máy dùng trong công nghiệp sản xuất phụ tùng ô tô, đặc biệt là trong các nhà máy như DENSO, nơi họ chế tạo các linh kiện phức tạp. Oilseal là một loại phớt chặn dầu (oil seal) được sử dụng để ngăn dầu và chất lỏng khác rò rỉ từ các bộ phận chuyển động. Máy MCVe có thể là một dòng máy ép chuyên dụng để lắp hoặc sản xuất các phớt chặn dầu cho linh kiện ô tô.

Khả năng cảnh báo tải trọng ép của máy
Thông thường, các máy ép công nghiệp hiện đại như MCVe thường được trang bị hệ thống cảm biến tải trọng (load sensors) hoặc đồng hồ đo áp lực (pressure gauges) để giám sát tải trọng ép. Hệ thống này giúp đảm bảo tải trọng nằm trong giới hạn an toàn, và sẽ cảnh báo nếu phát hiện bất thường.

Cảm biến tải trọng (Load Sensors): Được gắn trực tiếp lên cơ cấu ép của máy, cảm biến này đo tải trọng thực tế đang tác động lên sản phẩm trong quá trình ép.
Hệ thống điều khiển PLC: Nếu máy MCVe được trang bị hệ thống điều khiển tự động PLC (Programmable Logic Controller), nó có thể dễ dàng tích hợp với các cảm biến để đưa ra cảnh báo khi tải trọng vượt mức, thậm chí ngắt máy để tránh gây hỏng hóc.
Màn hình giám sát và cảnh báo: Các máy ép hiện đại thường có giao diện người dùng (HMI) hiển thị thông số tải trọng theo thời gian thực. Hệ thống cảnh báo này sẽ phát ra tín hiệu âm thanh, đèn báo, hoặc thậm chí gửi thông tin cảnh báo đến các bộ phận bảo trì nếu tải trọng vượt mức an toàn.