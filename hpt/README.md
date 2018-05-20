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

#### 3.1. Phần cứng

##### a. Hệ đa vi xử lý
![các loại hệ đa vi xử lý](img/multi_process.png)

* Các bộ vi xử lý kết nối với nhau và với modun nhớ thông qua trục bus của hệ thống -> khi một cặp sử dụng trục thì cặp khác không sử dụng được -> tăng thời gian chờ
* Kiến trúc switch trung gian -> hiệu năng cao -> chi phí cao
* Mini computer: ít tiền, mỗi cpu sử dụng bộ nhớ riêng, yêu cầu các máy tính tương đối giống nhau

##### b. Hệ thuần nhất / hệ không thuần nhất

* Hệ thuần nhất: các máy tính tương đối giống nhau, thường sử dụng trong tính toán song song

* Hệ không thuần nhất: những máy tính khác nhau kết nối với nhau

#### 3.2. Hệ điều hành phân tán

##### a. Dos (Distributed OS)

![](img/dos.png)

Hệ điều hành duy nhất được cài đặt trên tất cả hệ thống phần cứng của hệ thống,  các vấn đề của hệ phân tán được xử lý ở tầng hệ điều hành. Người sử dụng không cần quan tâm đến các chi tiết của hệ phân tán, múc trong suốt tuyệt đối. 

##### b. NOS (Network OS)

![](img/nos.png)

Bổ sung thêm các tính năng vào các hệ điều hành cục bộ, cho phép tiến trình có thể sủ dùng hạ tầng mạng máy tính để kết nối và giao tiếp với nhau. Người xây dựng ứng dụng phải cung cấp các cơ chế để trao đổi thông tin với nhau (UDP, TCP, ..). người xây dựng ứng dụng phải xử lý những vấn đề của hệ phân tán. Thường dùng cho các hệ không thuần nhất.

##### c. **Middleware** 

![](img/middleware.png)

Nằm giữa nos và tầng ứng dụng phân tán. Là các thư viện các framework cung cấp các cơ chế giao tiếp trao đổi trong hệ phân tán, cho phép lập trình viên sử dụng để phát triển ứng dụng như môt thư viên có sẵn mà không phải lâp trình lại. Tức là trong trường hợp lý tưởng, hệ thống sẽ trở nên trong suốt đốio với người xây dựng ứng dụng!

MiddleWare cung cấp các dịch vụ:

- Truy cập trong suốt 
- Các phương tiện trao đổi thông tin bậc cao 
- Dịch vụ định danh 
- Dịch vụ lưu trữ bền vững 
- Giao tác phân tán 
- Bảo mật 
- Các dịch vụ khác


Có thể nói MiddleWare thừa kế những ưu điểm tử cả DOS (tính trong suốt cao) và NOS (tính mở, tính co giãn cao)

## Chương 2: Kiến trúc
### 1. Giới thiệu
#### 1.1. Kiến trúc

Hệ phân tán được phân chia thành các thành phần nhỏ, kiến trúc là sự mô tả cách tổ chức và tương tác giữa các thành phần. Mỗi thành phần được gọi là đơn vị module, với giao diện được định nghĩa và cung cấp rõ ràng nằm trong môi trường của chúng. Với giao diện tương đồng thì có thể kết nối và thay thế lẫn cho nhau. Các thành phần được kết nối vs nhau = các connecter, chính là các phương tiện để thực hiện các lời gọi thủ tục truyền thông điệp hay dữ liệu dòng.

Kiểu kiến trúc:

* Cách thức các thành phần kết nối với nhau
* Cách thức dữ liệu trao đổi giữa các thành phần
* Các thành phần kết hợp như thế nào để tạo nên một hệ thống

##### 1.1.1.Phong cách phân tầng

![](img/layered_arch.png)

ý tưởng: tổ chức thành phần theo phân tầng: tầng $L_i$  có thể sử dụng được các module ở tầng $L_{i-1}$

Tác dụng:

* đối với các hệ thống phức tạp, áp dụng nguyên lý chia để trị
* cho phép xác định rõ nhiệm vụ của các bộ phận và quan hệ giữa chúng
* dễ dàng bảo trì vả nâng cấp hệ thống, thay đổi thành phần này không ảnh hưởng đến thành phần khác (vd: khi chuyển từ ipv4 -> ipv6 chỉ quan tâm đến tầng mạng, ko ảnh hưởng đến các tầng khác)


##### 1.1.2. Phong cách hướng đối tượng 

![](img/object_arch.png)

Các thành phần là các đối tượng, các kết nối là các lời gọi thủ tục, cơ chế kết nối là cơ chế lời gọi thủ tục. Bao gồm 2 loại đối tượng là khách (object client) và chủ (Object server).

Kết nối giữa các đối tượng là kết nối lỏng, tức là chúng có thể không đồng, khác nhau về các phương thức hay thuộc tính. 

##### 1.1.3. Phong cách hướng sự kiện

![](img/event_arch.jpg)

Các thành phần hệ thống trao đổi thông tin với nhau thông qua các sự kiện, các sự kiện có thể kích hoạt các thao tác thông qua các tiến trình. Kết nối giữa các đối tượng là kết nối lỏng, các thành phần có thể khác nhau về cả phần cứng lẫn phần mềm. 

##### 1.1.4 Kiến trúc hướng dữ liệu

![](img/data_arch.png)

Các tiến trình có thiết kế tách rời, trao đổi thông tin qua một kho dữ liệu chung, vì vậy 2 tiến trình không đồng thời cùng chạy vẫn có thể trao đổi dữ liệu.

#### 1.2. Mô hình

là kết quả của sự trìu tượng hoá hpt. Có 3 loại:

* Mô hình lỗi
* Mô hình tương tác
* Mô hình bảo mật

### 2. Kiến trúc hệ thống
#### 2.1. Kiến trúc tập trung
##### 2.1.1 Client-Server

![](img/client_server.png)

* Client:  Là 1 tiến trình sử dụng dịch vụ của server bằng cách gửi yêu cãu, nhận kết quả và hiển thị
* Server: Là 1 tiến trình triển khai 1 dịch vụ cụ thể. Lằng nghe, nhận yêu cầu, xử lý và trả lời
* Giao thức kết nối: Hướng kết nối hoặc ko kết nối

##### 2.1.2 Phân tầng ứng dụng

Thay vì phân biêt client server thì chuyển sang phân biệt các tầng,

* tầng giao diện người dùng: cung cấp chương trình cho người dùng cuối tương tác vs hệ thống
* tầng nghiệp vụ
* tầng dữ liệu

![](img/app_layered.jpg)

#### 2.2. Kiến trúc phi tập trung

Phân phối các client và server chia 1 cách vật lý các phần việc tương ứng, được gọi là phân phối ngang.

##### 2.2.1 p2p có cấu trúc

> **Mạng Overlay**: Được xây dựng bên trên hệ thống mạng vật lý thật, mỗi node là 1 tiến trình và các cạnh là các kênh liên lạc có thể của tiến trình đó. 

Tên tệp được mã hoá bằng DHT (distributed hash table) thu đươc 1 dãy 128 bit, vấn đề cần giải quyết là cung cấp thủ tục routing (thầy gọi là phân vùng khoá) tìm ra địa chỉ mạng của node chịu trách nhiệm khi tìm kiếm têp tin.

**Chord System**:

![](img/chord.jpg)

* succ(key) = id nhỏ nhất lớn hơn key
* lookup(key) : trả về succ(key)
* thêm node: thêm ngay sau succ(id mới), sau khi thêm gán lại succ(key) cho các key cũ
* xoá node: ngược lại

**Content Address Network(CAN)**:

![](img/can.png)

##### 2.2.2. p2p không câu trúc

Mỗi node có 1 list các node hàng xóm, dữ liệu được lưu trữ môt cách ngẫu nhiên, vì vậy khi muồn tìm kiếm phải truy vấn toàn bộ mạng

#### 2.3. Kiến trúc hỗn hợp

##### 2.3.1. Máy chủ biên

![](img/edge_server.jpg)

Server triển khai ở biên mạng (danh giới cùa mạng doanh nghiệp và mạng internet). Các cient có thể lấy nội dung mà không cần kết nối đến nhà cung cấp nội dung.

##### 2.3.2 Hệ phân tán hợp tác

![](img/torrent.jpg)

Kết hợp giữa kiến trúc tâp trung và không tâp trung. Sử dụng hệ thống tập trung để tìm kiếm file torrent, lấy list các node tracker đang lưu giữ tập tin cần tải. Sử dụng hệ thống phi tập trung để tải và seed file.


 