# Table of Contents
- [Table of Contents](#table-of-contents)
- [Các nội dung cần có trong slide](#các-nội-dung-cần-có-trong-slide)
  - [Giới thiệu team](#giới-thiệu-team)
    - [Giới thiệu tên nhóm, xuất thân của nhóm](#giới-thiệu-tên-nhóm-xuất-thân-của-nhóm)
    - [Giới thiệu sơ qua về từng thành viên của nhóm](#giới-thiệu-sơ-qua-về-từng-thành-viên-của-nhóm)
    - [Lý do tham gia cuộc thi hackathon](#lý-do-tham-gia-cuộc-thi-hackathon)
  - [Đặt vấn đề](#đặt-vấn-đề)
    - [Đánh giá về nhà máy DENSO](#đánh-giá-về-nhà-máy-denso)
    - [Các điểm mạnh của nhà máy](#các-điểm-mạnh-của-nhà-máy)
    - [Các vấn đề đã nhìn thấy](#các-vấn-đề-đã-nhìn-thấy)
    - [Vấn đề mà nhóm sẽ tập trung giải quyết](#vấn-đề-mà-nhóm-sẽ-tập-trung-giải-quyết)
  - [Giải pháp đề xuất](#giải-pháp-đề-xuất)
    - [What? - Nêu ra giải pháp Anomaly detection for machine](#what---nêu-ra-giải-pháp-anomaly-detection-for-machine)
    - [Why? - Tại sao lại chọn giải pháp này, nêu các ví dụ tương đương trong ngành công nghệ thông tin, nghiên cứu thị trường, các đối thủ khác của DENSO](#why---tại-sao-lại-chọn-giải-pháp-này-nêu-các-ví-dụ-tương-đương-trong-ngành-công-nghệ-thông-tin-nghiên-cứu-thị-trường-các-đối-thủ-khác-của-denso)
    - [How? - Trình bày sơ bộ kiến trúc của giải pháp](#how---trình-bày-sơ-bộ-kiến-trúc-của-giải-pháp)
  - [Hiệu quả dự tính mang lại](#hiệu-quả-dự-tính-mang-lại)
    - [Trình bày về lượng thời gian dừng ngắn, dừng dài được giảm bớt khi áp dụng, làm cho quy trình sản xuất mượt mà hơn](#trình-bày-về-lượng-thời-gian-dừng-ngắn-dừng-dài-được-giảm-bớt-khi-áp-dụng-làm-cho-quy-trình-sản-xuất-mượt-mà-hơn)
  - [Thời gian triển khai thực tế](#thời-gian-triển-khai-thực-tế)
    - [Ước lượng các công đoạn cần có và thời gian cần thiết để triển khai từng công đoạn](#ước-lượng-các-công-đoạn-cần-có-và-thời-gian-cần-thiết-để-triển-khai-từng-công-đoạn)
  - [Các điểm khó khăn dự án có thể gặp phải trong thực tế](#các-điểm-khó-khăn-dự-án-có-thể-gặp-phải-trong-thực-tế)
  - [Kết luận](#kết-luận)
# Các nội dung cần có trong slide
## Giới thiệu team
### Giới thiệu tên nhóm, xuất thân của nhóm
- Tên nhóm ANSAERS, gồm các thành viên đến từ ANSA Lab - Do thầy Nguyễn Tài Hưng quản lý - thưộc viện Điện Tử Viễn Thông - Đại Học Bách Khoa Hà Nội
### Giới thiệu sơ qua về từng thành viên của nhóm
- Leader: Phạm Tiến Đạt
  - Role: BA, Dev
  - Năm sinh: 2002
  - Hiện đang làm việc tại FPT Smart Cloud, vị trí Cloud Database Engineer
- Thành viên: Nguyễn Tiến Chinh
  - Role: Devops
  - Năm sinh: 2002
  - Hiện đang làm việc tại FPT Smart Cloud, vị trí Fullstack Developer
- Thành viên: Nguyễn Minh Thành
  - Role: AI Engineer
  - Năm sinh: 2003
  - Đã có báo khoa học liên quan đến vấn đề Network cho mạng 5G
- Thành viên: Nguyễn Thùy Linh
  - Role: BA, AI Engineer
  - Năm sinh: 2003
  - Hiện đang là thực tập sinh Fullstack developer tại công ty XXX
- Thành viên: Trần Quang Huy
  - Role: AI Engineer
  - Năm sinh: 2003

### Lý do tham gia cuộc thi hackathon
- Với sự tò mò và niềm đam mê công nghệ, sau khi có được thông tin cuộc thi DENSO Hackathon năm nay tổ chức, nhóm em đã rất háo hức vì có thể tiếp cận với các bài toán thực tế của doanh nghiệp - thứ sẽ đem lại rất nhiều kinh nghiệm cho nhóm em sau này, đồng thời phần thưởng mà cuộc thi đem lại cũng rất hấp dẫn, cũng một động lực để chúng em tham gia cuộc thi !
## Đặt vấn đề
### Đánh giá về nhà máy DENSO
Đây là lần đầu em được tham quan một nhà máy công nghiệp, em thực sự choáng ngợp trước phạm vi và độ hiện đại của nhà máy, độ sạch sẽ, nhân viên và các anh chị đã tiếp đón vô cùng chu đáo, quy trình của công ty vô cùng bảo mật và nghiêm ngặt, làm nhóm em có một ấn tượng rất sâu sắc
### Các điểm mạnh của nhà máy
Các điểm mạnh nhận thấy được sau khi tham quan:
- Nhà máy có tầm nhìn, định hướng rõ ràng cho tương lai
- Có các quy trình làm việc rõ ràng
- Sẵn sàng thay đổi và áp dụng các công nghệ mới
- Máy móc hiện đại
### Các vấn đề đã nhìn thấy
Tuy vậy sau khi tham quan và hỏi đáp với ban điều hành, nhóm chúng em có nhận ra được các painpoint cơ bản sau:
- Các máy trong nhà máy đang hoạt động độc lập, tất cả các hoạt động monitor là do con người, đội vô địch năm ngoái nhìn ra điều này và làm 1 AI chụp ảnh đồng hồ rồi tập hợp số liệu, tuy vậy cảm giác vẫn không ổn với các máy không có đồng hồ, liệu có thể số hóa máy móc hay không?
- Chưa thể truy xuất vị trí lỗi của sản phẩm một cách tự động khi một lỗi phát sinh, đặc biệt khi dữ liệu không liên kết với mã serial trong các giai đoạn như Processing hay Assembly
- Về vấn đề sản xuất, khi máy móc có xảy ra bất thường, buộc phải dừng ngắn hoặc dừng dài để đội bảo trì xử lý máy, gây ảnh hưởng đến quy trình sản xuất sản phẩm
### Vấn đề mà nhóm sẽ tập trung giải quyết
Vấn đề thì hiện tại nhóm nhận thấy rất nhiều, tuy nhiên thời gian và nguồn lực có hạn, nhóm em quyết định sẽ tập trung giải quyết tối ưu các cảnh báo về máy móc, để đội bảo trì có thể xử lý trước khi cả bất thường xảy ra, và đó chính là ý tưởng của nhóm chúng em - Anomaly Detection for Machine

## Giải pháp đề xuất
### What? - Nêu ra giải pháp Anomaly detection for machine 
- Giải pháp: Phát triển hệ thống giám sát và phát hiện bất thường (Anomaly Detection) dựa trên dữ liệu từ máy móc trong nhà máy. Hệ thống này sẽ thu thập dữ liệu thời gian thực từ máy móc và phân tích dữ liệu bằng các thuật toán học máy (machine learning) nhằm phát hiện các dấu hiệu bất thường trước khi xảy ra sự cố.

- Các thành phần chính:
  - Hệ thống phân tích: Sử dụng các mô hình AI để học từ dữ liệu lịch sử và phát hiện các dấu hiệu bất thường.
  - Giao diện cảnh báo: Gửi cảnh báo tức thời đến đội bảo trì khi phát hiện bất thường.
### Why? - Tại sao lại chọn giải pháp này, nêu các ví dụ tương đương trong ngành công nghệ thông tin, nghiên cứu thị trường, các đối thủ khác của DENSO
- Lý do: Phát hiện và xử lý sự cố máy móc trước khi chúng gây ra ảnh hưởng nghiêm trọng là một trong những yếu tố quan trọng giúp tối ưu hóa quy trình sản xuất. Khi bất thường xảy ra, việc dừng dây chuyền để bảo trì có thể làm gián đoạn sản xuất, gây thiệt hại lớn về thời gian và tài nguyên.

- Liên hệ với ngành ngành công nghệ thông tin: Các hệ thống giám sát máy chủ và cơ sở hạ tầng trong IT sử dụng các công nghệ tương tự để phát hiện các sự cố tiềm tàng trước khi chúng xảy ra, nhằm giảm thiểu downtime.

- Nghiên cứu thị trường: Nhiều công ty lớn như General Electric, Siemens và Bosch đã triển khai các giải pháp tương tự để tăng hiệu suất vận hành và giảm chi phí bảo trì máy móc trong các nhà máy sản xuất.

- Đối thủ cạnh tranh của DENSO: Các nhà sản xuất ô tô và công nghiệp khác cũng đang hướng đến việc tự động hóa giám sát máy móc và bảo trì dự đoán nhằm tối ưu hóa quy trình và tăng năng suất.
### How? - Trình bày sơ bộ kiến trúc của giải pháp
- Kiến trúc sơ bộ:
  - Data Processing Layer (Tầng xử lý dữ liệu): Dữ liệu từ các cảm biến được gửi đến một nền tảng đám mây hoặc máy chủ cục bộ để xử lý.
  - Anomaly Detection Model (Mô hình phát hiện bất thường): Sử dụng các thuật toán AI như Random Forest, k-NN, hoặc Neural Networks để phát hiện bất thường trong dữ liệu.
  - Alert System (Hệ thống cảnh báo): Khi hệ thống phát hiện bất thường, cảnh báo sẽ được gửi đến đội bảo trì qua email, SMS, hoặc ứng dụng di động.
  - Monitoring Dashboard (Bảng điều khiển giám sát): Bảng điều khiển cho phép quản lý và đội bảo trì theo dõi tình trạng máy móc theo thời gian thực và đưa ra quyết định hành động.
## Hiệu quả dự tính mang lại
### Trình bày về lượng thời gian dừng ngắn, dừng dài được giảm bớt khi áp dụng, làm cho quy trình sản xuất mượt mà hơn
Lợi ích:
- Giảm thời gian dừng ngắn và dừng dài: Với hệ thống phát hiện bất thường, nhóm bảo trì sẽ có thể dự đoán và xử lý sự cố trước khi nó ảnh hưởng đến quy trình sản xuất, từ đó giảm thời gian dừng máy không mong muốn.

- Tối ưu hóa quy trình sản xuất: Sự gián đoạn sản xuất sẽ được giảm thiểu, giúp tối ưu hóa quy trình vận hành liên tục và mượt mà hơn, đồng thời tăng cường hiệu suất sử dụng máy móc.

- Giảm chi phí bảo trì: Bằng cách dự đoán và xử lý sự cố trước khi chúng trở nên nghiêm trọng, chi phí bảo trì sẽ được giảm đáng kể, đồng thời tránh được các chi phí phát sinh từ việc sửa chữa lớn hoặc thay thế máy móc.
Con số ước lượng:
- Dự kiến giảm 30-50% thời gian dừng ngắn và dừng dài.
- Tăng cường hiệu suất máy móc lên đến 15-20% trong 6 tháng đầu triển khai.
## Thời gian triển khai thực tế
### Ước lượng các công đoạn cần có và thời gian cần thiết để triển khai từng công đoạn
1. Khảo sát nhà máy và thu thập dữ liệu ban đầu (2-4 tuần):

- Khảo sát toàn bộ hệ thống máy móc và lựa chọn các máy móc cần giám sát.
- Triển khai cảm biến IoT và thu thập dữ liệu từ các máy móc quan trọng.
2. Phát triển và huấn luyện mô hình AI (4-6 tuần):

- Sử dụng dữ liệu thu thập để huấn luyện các mô hình AI phát hiện bất thường.
- Điều chỉnh mô hình dựa trên các yếu tố sản xuất thực tế.
3. Triển khai thử nghiệm và tích hợp hệ thống cảnh báo (4 tuần):

- Triển khai hệ thống giám sát và cảnh báo thử nghiệm trên một số máy móc.
- Điều chỉnh hệ thống dựa trên phản hồi từ đội ngũ vận hành và bảo trì.
4. Tích hợp hoàn toàn và giám sát hiệu quả (2-4 tuần):

- Hoàn thành việc tích hợp hệ thống vào quy trình sản xuất.
- Giám sát hiệu quả và phân tích kết quả từ hệ thống để cải thiện mô hình.

## Các điểm khó khăn dự án có thể gặp phải trong thực tế 
- Khả năng thu thập dữ liệu từ các thiết bị cũ: Nhiều thiết bị trong nhà máy vẫn sử dụng hệ thống analog, khó khăn trong việc tích hợp và thu thập dữ liệu tự động.

- Độ chính xác của mô hình phát hiện bất thường: Mô hình AI cần phải được điều chỉnh và huấn luyện đúng cách để đảm bảo độ chính xác cao trong việc phát hiện các bất thường. Sai sót trong dữ liệu có thể làm giảm hiệu quả phát hiện.

- Sự phối hợp giữa đội bảo trì và công nghệ mới: Nhân viên bảo trì có thể không quen với việc sử dụng các hệ thống giám sát tự động, đòi hỏi thời gian để đào tạo và làm quen với quy trình mới.

- Chi phí triển khai và bảo trì hệ thống: Việc đầu tư cho các thiết bị IoT và hạ tầng công nghệ có thể là một thách thức về mặt chi phí cho nhà máy trong giai đoạn đầu.


## Kết luận
- Giải pháp Anomaly Detection for Machine sẽ giúp nhà máy DENSO tối ưu hóa quy trình sản xuất, giảm thiểu thời gian dừng máy không mong muốn và tăng cường hiệu suất vận hành.
- Đây là một bước tiến quan trọng trong việc số hóa và tự động hóa quy trình giám sát và bảo trì máy móc, giúp nhà máy bắt kịp với xu thế công nghệ 4.0.
- Nhóm chúng em tin rằng giải pháp này không chỉ giúp nhà máy DENSO nâng cao hiệu suất sản xuất mà còn tạo ra giá trị bền vững cho tương lai.