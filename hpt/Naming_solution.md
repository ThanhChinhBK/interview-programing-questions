**Câu hỏi 3**: Xét một thực thể di chuyển từ vị trí A sang vị trí B. Trong quá trình di chuyển thực thể đó có đi qua các nút trung gian nhưng chỉ dừng lại ở đó khoảng thời gian ngắn. Khi đến B, thực thể đó dừng lại. Chúng ta biết rằng việc thay đổi địa chỉ trong một dịch vụ tổ chức vị trí phân cấp (hierarchical location service) là rất mất thời gian để hoàn thành, vì vậy cần tránh làm việc này khi thực thể tạm dừng ở các nút trung gian. Hãy đề xuất một mô hình kết hợp cả dịch vụ tổ chức vị trí phân cấp và cơ chế chuyển tiếp con trỏ (forwarding pointers) để có thể xác định được vị trí của thực thể khi nó ở các nút trung gian.

**Trả lời**: Dùng cơ chế chuyển tiếp con trỏ, khi thực thể đến B thì xoá con trỏ và cập nhập theo cơ chế phân cấp, xoá con trỏ và địa chỉ tại A bị xoá.

**Câu hỏi 4**: Trình bày một số phương pháp ARP Spoofing để thấy được điểm yếu của phương pháp định danh sử dụng cơ chế quảng bá.

**Trả lời**: ARP không có cơ chế xác thực, host có thể chấp nhận 1 arp reply mà trước đó không cần phải gửi gói tin đi trước đó.

* Man In the Middle: Host A và Host B đều nhận được ARP giả, thu được địa chỉ giả và giao tiếp với địa chỉ đó.
* Denied of Service: Gửi địa MAC giả của gate way to71o tất cả các tiến trình khiến cho toàn bộ tiến trình không thể kết nối được mạng
* mac flooding: Gửi ARP reply đến làm quá tải switch.

**Câu hỏi 7**: Khi áp dụng giải pháp sử dụng hàm băm phân tán vào hệ thống Chord thì nó đã tối ưu cơ chế định danh như thế nào? 

**Trả lời**: Mỗi node trong Chord quản lý 1 số lượng thực thể xấp xỉ nhau nên luôn đảm bảo cân bằng tải, ngoài ra cơ chế finger table luôn đảm bảo cho quá trình tìm kiếm có độ phức tạp O(n).

**Câu hỏi 10**: Khi chúng ta thêm 1 node mới vào hệ thống Chord, chúng ta có cần phải cập nhật toàn bộ các bảng finger?

**Trả lời**: Không nhất thiết, ví dụ:

![](img/chord_naming.jpg)

Trong mạng trên, khi thêm node 7 vào mạng, finger table của node 7 sẽ gồm có [9, 9, 11, 18, 28]. Vả chỉ cần update các node #4([7,7,9,14,28]), #21([28,28,28,1,7] và #1([4,4,7,9,18]).
