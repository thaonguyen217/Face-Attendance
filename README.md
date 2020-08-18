# Face-Attendance
Hệ thống điểm danh bằng khuôn mặt sử dụng face-regconition library, nhận diện khuôn mặt qua các bước :
- Tìm kiếm tất cả các khuôn mặt có trong image list (vd: danh sách nhân viên) và face location
- Từ khuôn mặt đã detect được, tạo các face landmarks
- Encoding: Từ các face landmarks, mã hóa chúng thành khoảng cách giữa các điểm (vd: khoảng cách giữa hai mắt, khoảng cách giữa mũi và miệng...). TẤt cả có 128 khoảng cách
- Từ một ảnh khuôn mặt mới (không có trong image list ban đầu), sau khi kết quả sau khi encoding được so sánh với kết quả encoding của các ảnh trong image list. Hai tiêu chí so sánh thường dùng :
+ face_compare: bằng True nếu đó là ảnh cùng một người, bằng False nếu là hai người khác nhau
+ face_distance: độ khác nhau giữa hai khuôn mặt. Nếu là cùng một người thì face_distance nhỏ và ngược lại.
Các file .py : 
- Basic: So sánh hai ảnh với nhau
- Attendance: So sánh hình ảnh người (một hoặc vài người) xuất hiện trong webcam với những người có sẵn trong thư mục 'Resources/Attendance'. Press 's' để lưu lại hình ảnh webcam lúc đó.


TLTK:
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
