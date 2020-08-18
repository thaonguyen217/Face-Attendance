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

![result](https://user-images.githubusercontent.com/49630112/90501580-c70b0480-e176-11ea-872b-c46138ce6633.jpg)
![result](https://user-images.githubusercontent.com/49630112/90501900-3f71c580-e177-11ea-95fe-097394a879d6.jpg)
![papa](https://user-images.githubusercontent.com/49630112/90502412-f9693180-e177-11ea-8c1e-a13aaddcfde9.jpg)

Kết quả điểm danh bằng khuôn mặt :

PAPAYA,15:56:25

KAIZ,15:56:34

BRAND,15:57:34

TLTK:
https://medium.com/@ageitgey/machine-learning-is-fun-part-4-modern-face-recognition-with-deep-learning-c3cffc121d78
