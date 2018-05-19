# Hệ phân tán
## Chương 1: Tổng quan
### 1. Định nghĩa
> hệ phân tán là hệ thống các máy tính độc lập kết nối lẫn nhau bằng mạng máy tính cung cấp một dịch vụ thống nhất cho người dùng như một máy tính đơn nhất

### 2. Đặc điểm
#### 2.1. Chia sẻ tài nguyên
Đây là mục tiêu quan trọng nhất cũa hệ phân tán, đảm bảo các tiến trình ở các máy tình khác nhau có thể sử dụng tài nguyên của nhau. Giảm thiểu chi phí lưu trữ tài nguyên, tăng tính sẵn có, nhưng đồng thời cũng tăng rủi ro về an toàn thông tin.
#### 2.2. Tính trong suốt
Là sự che dấu với người dùng cuối sự rời rạc, quy mô và vị trí của hệ thống, nhờ đó , đối với người dùng, hệ thống là duy nhất. Cần cân bằng giữa mức độ trong suốt và hiệu năng của hệ thống.

Các loại trong suốt, dùng để che dấu những thành phần khác nhau: trong suốt truy cập (sự bất đồng về biểu diễn và truy cập tài nguyên), trong suốt vị trí (vị trí tài nguyên), trong suốt di trú (khả năng di chuyển tài nguyên), trong suốt chuyển địa điểm (sự di chuyển tài nguyên khi đang sử dụng), trong suốt sao lưu (tình trạng sử dụng bản sao), trong suốt tương tranh, trong suố sự cố, trong suốt bền vững (lưu trong bộ nhớ ngoài hay bộ nhớ chính)

#### 2.3. Tính mở

Một hệ thống được gọi là mở nếu nó cung cấp dịch vụ theo các quy tắc được đặc tả bằng chuẩn cú pháp và ngữ nghĩa nhất định gọi là **giao diện**. Nhờ vậy, các thành phần của hệ thống có thể được cung cấp bởi các NSX khác nhau, miễn là phù hợp với giao diện của hệ thống.  Ngôn ngữ thường được sử dụng là IDL (interface description language)

* Khả năng phối hợp:  các cài đặt của hệ thống hoặc thành phần hệ thống từ các nhà sản xuất khác nhau có thể làm việc với nhau  

* Tính khả chuyển: một ứng dụng được phát triển cho hệ phân tán A có thể cài đặt mà không cần thay đổi gì trên hệ phân tán B khác, với điều kiện B có giao diện tương đống với A

* Tính mềm dẻo có thể mở rộng đươc
#### 2.4. Tính co dãn
Môt hệ phân tán phải thích nghi với sự thay đổi quy mô của hệ thống. Thể hiện trên các khía cạnh:

* dễ dàng bổ sung người sử dụng và tài nguyên hệ thống
* Thay đổi hoặc tăng quy mô về vị trí địa lý, phải đảm bảo trao đổi thông tin trên mạng diện rông như trên mạng cục bộ (tốc độ, độ tin cậy, đỗ trễ, đồng bộ hay ko đồng bộ, ...)
* Thay đổi quy mô về tổ chức quản trị

Giải pháp: Chia nhỏ (vd: DNS) 

### 3. Các thành phần hệ phân tán

####3.1. Phần cứng

#####a. Hệ đa vi xử lý
![các loại hệ đa vi xử lý](img/multi_process.png)

* Các bộ vi xử lý kết nối với nhau và với modun nhớ thông qua trục bus của hệ thống -> khi một cặp sử dụng trục thì cặp khác không sử dụng được -> tăng thời gian chờ
* Kiến trúc switch trung gian -> hiệu năng cao -> chi phí cao
* Mini computer: ít tiền, mỗi cpu sử dụng bộ nhớ riêng, yêu cầu các máy tính tương đối giống nhau

##### b. Hệ thuần nhất / hệ không thuần nhất

* Hệ thuần nhất: các máy tính tương đối giống nhau, thường sử dụng trong tính toán song song

* Hệ không thuần nhất: những máy tính khác nhau kết nối với nhau

#### 3.2. Hệ điều hành phân tán

##### a. Dos (Distributed OS)

![](img\dos.png)

Hệ điều hành duy nhất được cài đặt trên tất cả hệ thống phần cứng của hệ thống,  các vấn đề của hệ phân tán được xử lý ở tầng hệ điều hành. Người sử dụng không cần quan tâm đến các chi tiết của hệ phân tán, múc trong suốt tuyệt đối. 

##### b. NOS (Network OS)

![](img\nos.png)

Bổ sung thêm các tính năng vào các hệ điều hành cục bộ, cho phép tiến trình có thể sủ dùng hạ tầng mạng máy tính để kết nối và giao tiếp với nhau. Người xây dựng ứng dụng phải cung cấp các cơ chế để trao đổi thông tin với nhau (UDP, TCP, ..). người xây dựng ứng dụng phải xử lý những vấn đề của hệ phân tán. Thường dùng cho các hệ không thuần nhất.

##### c. **Middleware** 

![](C:\Users\Nguyen Chinh\Desktop\hpt\img\middleware.png)

Nằm giữa nos và tầng ứng dụng phân tán. Là các thư viện các framework cung cấp các cơ chế giao tiếp trao đổi trong hệ phân tán, cho phép lập trình viên sử dụng để phát triển ứng dụng như môt thư viên có sẵn mà không phải lâp trình lại. Tức là trong trường hợp lý tưởng, hệ thống sẽ trở nên trong suốt đốio với người xây dựng ứng dụng!

