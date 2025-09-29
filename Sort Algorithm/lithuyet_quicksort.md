Quick_Sort là 1 thuật toán sắp xếp nhanh là một mảng giá trị, chọn một trong các giá trị làm phần tử "trục" và di chuyển các giá trị khác sao cho các giá trị thấp hơn nằm ở bên trái trục và các giá trị cao hơn nằm ở bên phải trục

```note
Thuật toán QuickSort thực hiện thao tác tương tự một cách đệ quy các mảng con bên trái và bên phải của phần tử trục
```
![alt text](image-1.png)

Cách thức hoạt động

```note
1. Chọn một giá trị trong mảng để làm phần tử trục
2. Sắp xếp phần còn lại của mảng sao cho các giá trị thấp hơn phần tử trục nằm bên trái và giá trị cao hơn nằm bên phải
3. Hoán đổi phần tử trục với phần tử đầu tiên có giá trị cao hơn để phần tử trục nằm giữa giá trị thấp hơn và giá trị cao hơn
4. Thực hiện các thao tác tương tự (đệ quy) cho các mảng con ở bên trái và bên phải của phần tử trục
```

Demo Như sau:
Bước 1: Bắt đầu một mảng chưa được sắp xếp
<b>[ 11, 9, 12, 7, 3]</b>
Bước 2: Chọn giá trị cuối cùng làm phần tử trục
[ 11, 9, 12, 7, <b>3</b>]
Bước 3: Các giá trị còn lại trong mảng đều lớn hơn 3 phải nằm bên phải phần tử trục
[ <b>3</b>, 9, 12, 7, 11]
Bước 4: Giá trị 3 hiện đã ở đúng vị trí. Chúng ta cần sắp xếp các giá trị ở bên phải 3. Chúng ta chọn giá trị cuối cùng 11 làm phần tử trục mới.
[ 3, 9, 12, 7, 11]
Bước 5: Giá trị 7 phải nằm bên trái giá trị trục 11, và giá trị 12 phải nằm bên phải giá trị trục 11. Di chuyển 7 và 12.
[ 3, 9, 7, 12, 11]
Bước 6: Đổi 11 với 12 sao cho các giá trị thấp hơn là 9 và 7 nằm ở bên trái của 11, và 12 nằm ở bên phải.
Bước 7: 11 và 12 ở đúng vị trí. Ta chọn 7 làm phần tử trục trong mảng con [9, 7], nằm bên trái 11.
[ 3, 9, 7, 11, 12]
Bước 8: Ta phải đổi 9 với 7.
[ 3, 7, 9, 11, 12]
 
Và mảng đã được sắp xếp
