# Writeup Bandit Overtherwire
---

1. **Lv0 -> Lv1**
    >pass : NH2SXQwcBdpmTEzi3bvBHMM9H66vVXjL

    Câu đầu tiên khá đơn giản, sau khi dùng `ls` để list ra các file thì thấy file `readme`, ta chỉ cần đọc file bằng lệnh `cat readme` là có thể lấy được password cho LV tiếp theo.

    ![](https://i.imgur.com/oLICBfi.png)

---
2. **Lv1-> Lv2**
    >pass : rRGizSaX8Mk1RTb1CNQoXTcYZWU6lgzi

    Tương tự như **Lv0** nhưng file này là một file có tên khá đặc biệt. Đối với file đặc biệt nên chỉ đường dẫn cụ thể hoặc có thể thêm `<` sau `cat` để có thể đọc file này.

    ![](https://i.imgur.com/TMfm2UI.png)

---
3. **Lv2-Lv3** 
    >pass : aBZ0W5EmUfAf7kHTQeOwd8bauFJ2lAiG

    Tương tự như **Lv0** nhưng file này lại có khoảng trắng giữa các từ. Dùng `\` để chỉ cho một ký tự đặc biệt

    ![](https://i.imgur.com/xJEu7V8.png)

---
4. **Lv3-Lv4** 
    >pass : 2EW7BBsr6aMMoJ2HjW067dm8EgX26xNe

    Đề cần ta đọc file `.hidden`. Để hiển thị tất cả các file gồm hidden thì t dùng thêm option `-a`

    ![](https://i.imgur.com/6psCTXD.png)

---
5. **Lv4-Lv5** 
    >pass : lrIWWI6bB37kxfiCQZqUdOIYfr6eEeqR
    
    Ta thấy ở đây có rất nhiều file, mục tiêu của ta là cần tìm file có thể đọc được. Ta có thể sử dụng lệnh `file` để kiểm tra.
    Nhưng ở đây có khá nhiều file nên việc kiểm tra từng file sẽ rất tốn thời gian, ta có thể dùng `*` để đại diện cho phần khác nhau và thực hiện tìm kiếm tất cả.
    Sau khi có kết quả thì ta có thể quan sát là `-file07` có kiểu dữ liệu là `ASCII text`, đúng thứ ta đang tìm, vậy chỉ cần đọc nó ra là có được password cho LV tiếp theo

    ![](https://i.imgur.com/H33iukI.png)

---   
6. **Lv5-Lv6** 

    >P4L4vucdmLnm8I7Vl7jG1ApGSfjYKqJU

    Đề bài yêu cầu ta tìm một file có con người có thể đọc được, thực thi không được và có kích thước 1033 bytes. Ta có thể sử dụng lệnh `find` cùng với các option như `-size` `! -executable` để tìm được file theo yêu cầu.

    ![](https://i.imgur.com/TJxdW4R.png)

    Để kiểm tra 1 file con người đọc được hay không thì có thể sử dụng ls -l nhưng ở đây điều đó là không cần thiết bởi vì chúng ta chỉ tìm được 1 file có điều kiện 1033bytes và không thực thi được .
 ---   
    
7. **Lv6-Lv7** 
    >pass : z7WtoNQU2XfjmMtWA8u5rN4vzqu4v99S
    
    Theo hướng dẫn ‘somewhere on the server’ thì ta nên ra thư mục root để kiểm tra toàn bộ với lệnh `find` cùng các option như là `-user` `-group` `size`
    
    ![](https://i.imgur.com/JgD8zWK.png)
    ![](https://i.imgur.com/Wfl8ivt.png)

    Quan sát thấy phần lớn các file đều thông báo `Permission denied` và có một file `bandit7.password` trông khá uy tín =))
    Đọc nó và lấy password chiến LV tiếp theo thôi.

    ![](https://i.imgur.com/lcoou9K.png)
---
8. **Lv7-Lv8** 
    >pass : TESKZC0XvTetK0S9xNwm25STk5iWrBvP
    
    Password nằm kế `millionth` thì chỉ cần tìm ra `millionth` thôi. Linux cung cấp cho ta lệnh `grep` để tìm kiếm. Và thấy đấy, ta đã có password cho LV tiếp.

    ![](https://i.imgur.com/ANNuqiF.png)
---
    
9.  **Lv8-Lv9** 
    >pass : EN632PlfYiZbn3PhVK3XOGSlNInNE00t

    Dùng `uniq` với option `-u` để in ra dòng chỉ xuất hiện 1 lần. Nhưng để linux hiểu là chúng xuất hiện một lần thì chúng ta cần phải sắp xếp chúng lại trước.
    
    ![](https://i.imgur.com/bQABSpP.png)

---    
10. **Lv9-Lv10** 
    >pass : G7w8LIi6J3kTb8A7j9LgrywtEUlyyp6s

    Dùng lệnh `strings` để hiển thị chuỗi mà con người có thể đọc được cùng với gợi ý của đề thì ta có thể dễ dàng tìm được password.
    
    ![](https://i.imgur.com/qkgsX9c.png)
    
---
11. **Lv10-Lv11** 
    >pass : 6zPeziLdR2RKNdNYFNb6nVCKzphlXHBM

    Bài này thì chỉ là một mã hóa đơn giản `base64` (Tuy nhiên nếu bạn chưa biết base 64 là gì thì click đây : https://en.wikipedia.org/wiki/Base64). Linux cho ta lệnh `base64` với option `-d` để decode base64.

    ![](https://i.imgur.com/0qLp6j0.png)
---
12. **Lv11-Lv12** 
    >pass : JVNBBFSmZwKKOP0XbFXOoW8chDz5yVRv

    Theo đề bài thì đây chính là mã hóa `ROT13`, một loại mã hóa thay thế với cơ chế xoay vòng. Ta dùng lệnh `tr` để translate vị trí các chữ cái
        
    `tr  ‘A-Za-z’ ‘N-ZA-Mn-za-m’` tức là A—>Z sẽ thay thế thành N-Z và A—>M tương tự chữ với thường

    ![](https://i.imgur.com/TUbhUtI.png)

---
        
13. **Lv12-Lv13** 
    >pass : wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

    Đầu tiên ta làm theo đề bài là copy file qua thư mục tự tạo (ở đây tôi tạo tên zios) để thực hiện giải nén nhiều lần ở đây.

    ![](https://i.imgur.com/ynIyPcg.png)

    
    Câu này khá dài nhưng dễ , nó được nén nhiều lần với các công vụ như `gzip, bzip2, tar` Để làm được câu này chúng ta chỉ cần biết cách giải nén của từng công cụ và chuyển từ hexdump sang binary file là oke
    - `xxd -r hexdumpFIle > binaryFile` —> với option `-r (reverse)` chuyển ngược lại từ hexdump sang binary
    - `gzip -d file.gz` —> để decompress đối với `gzip`
    - `bzip2 -d file.bz2` —> để decompress đối với `bzip2`
    - `tar -xf file.tar` —> để decompress đối với file `tar`
    
    >***Lưu ý để decompress ta phải đổi tên thành file.suffix với suffix tương ứng thì mới có thể decompress được.***
    
    Cứ tiếp tục decompress như thế đến khi thông tin của file là ASCII text thì ta đã có thể lấy được pass *(một LV khá tốn thời gian)*
    
    ![](https://i.imgur.com/5EuYa6o.png)

---   
14. **Lv13-Lv14** 
    
    >pass : fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq

    Đề bài cho thấy chỉ có ở **Lv14** mới có thể đọc pass được và cho chúng ta 1 private key —> tức là ta phải dùng nó để vào được **Lv14** và đọc pass
    >*(Nếu bạn chưa biết `private key` là gì thì từ khóa `Asymmetric Encryption` sẽ có thể giúp bạn)*
    
    ![](https://i.imgur.com/CjB7VSZ.png)

    
    ta sử `man ssh` để đọc thì thấy option `-i` sẽ thay vì dùng pass để kết nối thì sẽ dùng private key để xác thực
    
    ![](https://i.imgur.com/goAWaNI.png)

    
    Bây giờ ta chỉ cần tìm đến thư mục `etc/bandit_pass/bandit14` để đọc pass này thôi

    ![](https://i.imgur.com/n5ye8Ht.png)
---
    
15. **Lv14-Lv15** 
    >pass: jN2kgmIXJ6fShzhT2avhotn4Zcka6tnt
    
    Ta chỉ việc kết nối đến `localhost` port `30000` và gửi password LV14 là oke. Kiến thức bạn cần biết ở Lv này chỉ đơn giản là cách dùng lệnh `nc`
    
    ![](https://i.imgur.com/sUGqlf2.png)

---    
16. **Lv15-Lv16** 
    >pass : JQttfApK4SeyHwDlI9SXGR50qclOAil1
    
    Đề yêu cầu gửi pass đến `localhos` port `300001` và dùng `SSL encryption` thì chúng ta có lệnh `openssl s_client` với option `-connect host:port` để connect tới localhost  
    
    ![](https://i.imgur.com/xFWRqWY.png)

    Sau khi đã connect thành công ta chỉ việc gửi thông tin pass LV trước là đã có thể lấy được pass
    
    ![](https://i.imgur.com/QiqU6Vv.png)
---
    
17. **Lv16-Lv17** 
    >pass : VwOSWtCA7lRKkTfbr2IDh6awj9RNZM5e

    Ở lv này ta cũng gần gửi pass tới `localhost` nhưng đề chưa cho biết port nào là chính xác vậy nên chúng ta cần phải tìm ra port nào có thể gửi trong đống port `31000 —> 32000`
    Chúng ta cần dò xem port nào hoạt động từ `31000->32000`. Linux cung cấp cho ta lệnh `nmap` để kiểm tra. Ta có thể thấy ở đây có 5 Port ở trạng thái mở
    
    ![](https://i.imgur.com/4T8OzaL.png)

    
    Nhưng trong số port này chỉ có 1 port là sẽ trả về Pass chính xác. Vì vậy chúng ta sẽ brute force và xem kết quả thử
    
    Tại port `31790` ta nhận được một thông báo `corect` và private key
    
    ![](https://i.imgur.com/GlSRMYF.png)

    
    ![](https://i.imgur.com/plM25u1.png)

    
    Ta dùng private key này để đăng nhập vào LV bandit tiếp theo, thì để làm được điều đó ta cần vào `tmp` và tạo một thư mục mới tiếp đến vào thư mục đó để tạo file và lưu trữ private key này. Cuối cùng dùng `ssh` với option `-i` để đang nhập LV tiếp theo
    
    ![](https://i.imgur.com/1DOt7N5.png)

    
    Dùng chmod để câp quyền cho privatekey và kết nối đến LV bandit17
    
    ![](https://i.imgur.com/vH2JZhU.png)

    
    Sau đó chỉ cần đọc file `bandit17` là có thể lấy được Pass 
    
    ![](https://i.imgur.com/G4LkELm.png)

---    
1.  **Lv17-Lv18** 
    >pass : hga5tuuCLF6fFzUpnagiMN8ssu9LFrdg

    Chúng ta cần tìm ra sự khác biệt giữa 2 file `password.new` và `password.old`. Linux cung cấp cho chung ta command `diff` để làm việc đó. Và password cho Lv tiếp theo nằm trong `password.new`
    
    ![](https://i.imgur.com/ypS5xhL.png)
---
    
19. **Lv18-Lv19** 
    >pass: awhqfNnAbc1naukrpqDYcF95h7HoMTrC
    
    Đề cho biết là đã config tại file `.bashrc` là khi login vào thì sẽ tự logout và pass nằm ở file `readme`.
    
    ![](https://i.imgur.com/5NoQDQ6.png)

    
    Vậy chúng ta cần làm đó là login và đọc file `readme` mà không cần gõ shell trước khi bị logout. Và SSH cho phép chúng ta làm điều đó
    
    ![](https://i.imgur.com/s99rM5c.png)

---    
20. **Lv19-Lv20** 
    >pass : VxCazJaVykI6W36BkBU0mJTCM8rR95XT

    Đề cho một shell scripst `bandit20-do` và chủ sở hữu là `bandit20` trong khi chúng ta chỉ mới được cấp quyền ở `bandit19` nhưng vẫn có thể thực thi được vì file này đã được setuid binary `(dùng ls -l để kiểm tra để thấy rõ hơn)`. Chúng ta có thể tận dụng file này để có thể lấy được pass của LV tiếp theo
    
    ![](https://i.imgur.com/lesWRrK.png)

    
    Đề còn cho gợi ý là hãy run `bandit20-do` mà không truyền tham số để biết cách dùng. Và thấy đấy `bandit20-do` dùng để chạy một command với tư cách người dùng khác, cụ thể ở đây là sẽ chạy được command với tư cách là `bandit20`. Thế thì để lấy được pass chúng ta chỉ cần đọc được file tại `etc/bandit_pass/bandit20`
    
    ![](https://i.imgur.com/8aG8oHp.png)

---    

21. **Lv20-Lv21**  

    >Pass : NvEJF7oVjkddltPSrdKEFOllh9V1IBcq

    Đề cho chúng ta một file `suconnect` và chủ sở hữu là `bandit21` với tác dụng là kết nối đến một port nào đó. Và nếu nó nhận được một password đúng thì nó sẽ trả về một password
    
    ![](https://i.imgur.com/l4R6izb.png)

    
    Vậy bây giờ ta cần tạo ra một server và mở port để chương trình `suconnect` có thể kết nối vào. Sau đó gửi cho nó một password của LV 20 để nhận được password của LV tiếp theo. *(Lý thuyết là thấy ổn áp gòi đó, giờ thực hành thôy)*
    - Đầu tiên ta mở port `4444` và listen ở 1 terminal khác
    
        ![](https://i.imgur.com/7bamtPQ.png)
        
    - tiếp theo ta dùng file `suconnect` để connect vào
    
        ![](https://i.imgur.com/9PTW15r.png)
    
    - Ta có thể thấy đã có một kết nối đến server, bây giờ ta sẽ gửi password ở LV 20 để nhận được pass của LV tiếp theo
    
        ![](https://i.imgur.com/1HOUiqG.png)

    
    Bên client thực hiện file `suconnect` thông báo `pasword matches` và đã gửi password Lv tiếp cho phía server. Thế là ta đã có thể lấy được pass cho LV tiếp theo

    ![](https://i.imgur.com/lty0XI3.png)
    
    ![](https://i.imgur.com/mNs3CHd.png)

---

22. **Lv21-Lv22** 
    >pass : WdDozAdTM2z9DiFEQ2mGlwngMfj4EZff
    
    Đề cho biết rằng trong `/etc/cron.d` có các chương trình được lên lịch và chạy một cách tự động
    Ở đây có khác nhiều chương trình nhưng cái chúng ta cần quan tâm đó chính là `bandit22` vậy nên đọc xem nó thực hiện gì nào...
    
    ![](https://i.imgur.com/NiHvlkT.png)

    
    Ta thấy tại mọi thời điểm thì đều thực hiện file `cronjob_bandit22.sh` .
    
    ![](https://i.imgur.com/fPi88Fs.png)

    
    Ta xem thử file đó thì thấy nó sẽ cấp quyền `Ower` là `read` và `write` còn `group` và `other` là quyền `read` sau đó sẽ đọc file password của Lv22 vào `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`
    Vậy để có password cho LV tiếp theo ta chỉ cần đọc file tại `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`
    
    ![](https://i.imgur.com/j2R2m40.png)
---
    
23. **Lv22-Lv23** 
    >pass : QYw0Y2aiA672PsMmh9puTQuhoz8SyR2G
    
    Với LV này thì cũng tương tự như LV trước
    Ta vào và đọc file cron của LV 23 xem cách nó thực hiện
    
    ![](https://i.imgur.com/PMeiT0u.png)

    
    Ở đây nó sẽ copy password vào`/tmp/$target` vậy nên chỉ cần hiểu được chương trình và tìm được giá trị các biến thì ta có thể biết được đường dẫn và lấy được password cụ thể `myname = bandit23` và `mytarget = 8ca319486bfbbc3663ea0fbe81326349`
    
    ![](https://i.imgur.com/VqsMxtV.png)

    
    Vậy ta đã có thể thấy được password LV tiếp theo sẽ được copy vào đường dẫn `/tmp/8ca319486bfbbc3663ea0fbe81326349` nên là chỉ cần đọc file tại đó là lấy được password.
    
    ![](https://i.imgur.com/Cep4ZqE.png)
---
24. **Lv23-Lv24** 
    >pass : VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar
    
    Tiếp tục thực hiện các bước giống LV trước và đọc file shell code ở LV 24
    
    ![](https://i.imgur.com/bCdSa03.png)

    
    shell code này cho biết nó sẽ **thực hiện** tất cả các scripts tại đường dẫn `/var/spool/$myname/foo` và sau đó sẽ **xóa** các scripts đó đi. Vậy chúng ta sẽ cần đọc và tìm ra các biến để xem đường dẫn và các hoạt động trong vòng `for`. Sau đó sẽ ghi một script để có thể khai thác được password lv tiếp theo
    Ta thấy `myname=bandit24` và vòng `for` với nhiệm vụ duyệt hết tất cả các file trừ `.` và `..`và nếu file có chủ sở hữu là `bandit23` thì sẽ **thực hiện 60s/lần** sau đó thì **xóa đi**
    Từ việc tìm ra biến `myname` thì ta có được đường đẫn mà shell code sẽ thực thi và xóa scripts sẽ là `/var/spool/bandit24/foo`
    Vậy ta chỉ cần viết một shell scripts đọc password của LV `bandit24` và chuyển vào một file ở `tmp/ziosbandit23/pass.txt` mà LV bandit 23 có thể đọc được nhưng cần phải chú ý thời gian vì sau một phút hệ thống thì file shell code của mình sẽ bị xóa đi
    - Đầu tiên ta tạo một thư mục `ziosbandit23` ở `tmp` cấp đầy đủ quyền
    
        ![](https://i.imgur.com/u1yzFRe.png)

    
    - Tiếp đến ta sẽ tạo 1 shell code ở đường dẫn `/var/spool/bandit24/foo` với nội dung:
    
        ![](https://i.imgur.com/Yf4J3iq.png)

    
    - Sau đó cấp quyền thực thi cho file `getpass.sh` . Ta có thể thấy trước khi hết 1 phút hệ thống ta đọc file `/tmp/ziosbandit23/pass.txt` thì không được vì nó chưa được tạo nhưng sau khi qua phút mới thì nó đã được tạo với nội dung là pass của LV tiếp theo.
    - 
        ![](https://i.imgur.com/Sz8YlWw.png)
---
25. **Lv24-Lv25** 
    >pass : p7TaowMYrmu23Ol8hiZh9UvD0O9hpx8d

    Đề bài này yêu cầu khá đơn giản, chỉ cần gửi pass của Lv trước kèm với 1 số có 4 chữ số (0000 -> 9999) đến port `30002` nếu gửi đúng port thì sẽ nhận được pass
    Đề thì đơn giản nhưng làm thì có vẻ khá khó. Giống câu trên đó chính là mình phải tự viết ra một scipt để có thể làm được điều này.
    - Được rồi, hiểu ý tưởng thì bắt tay vào làm thôi. Vào thư mục `tmp` tạo thư mục `ziosbandit24`
    - 
    ![](https://i.imgur.com/lL6x8jP.png)
    
    - Bắt đầu tạo và viết shell code `getpass.sh` cho Lv này với nội dung :
    - 
    ![](https://i.imgur.com/HZrMZyd.png)

    - Thực hiện cấp quyền và chạy file shell code, sau đó đọc thử file `payload.txt` thì thấy có vẻ ta đã nhận được kết quả như mong muốn rồi. 
    - 
    ![](https://i.imgur.com/eAYlea6.png)
    - Bây giờ chỉ việc gửi các kết quả này đến cho port `30002` và chờ password lv tiếp theo trả về thôi 
    
        ![](https://i.imgur.com/l1kJyH8.png)
        ![](https://i.imgur.com/qzgZff2.png)

    Và thế là ta đã nhận được password cho Lv tiếp theo.
---
26. **LV25-LV26**
    >pass : c7GvcKlw9mC7aUQaPx7nwFstuAIBw1o1

    Vừa vào thì list ra thì thấy một privatekey ta thử đăng nhập vào bằng `ssh -i` thì vào được **LV26** thật. 

    ![](https://i.imgur.com/P76sqf1.png)

    Nhưng vừa vào thì lại bị đuổi ra. Khá là ảo ma nhưng lại hợp lý, chứ LV này mà như LV đã chơi thì lại dễ quá =))
    
    Đề bảo shell của bandit26 không phải là `/bin/bash`, nhiệm vụ của ta là tìm ra nó là gì và xem cách nó hoạt động để trả lời cho câu hỏi tại sao mình lại bị logout khi vào.
    Điều đầu tiên là tìm thấy shell, tại file `/etc/passwd` linux có lưu các user cùng thông tin shell mà user đó sở hữu.

    ![](https://i.imgur.com/SpT2ePl.png)

    Bây giờ thử xem trong này hoạt động như nào

    ![](https://i.imgur.com/rjs4JHL.png)

    Ta thấy file này sẽ thực hiện đặt trình giả lập là `linux` và thực hiện câu lệnh `more` để hiển thị file `text.txt` trên terminal và `exit 0` để thoát. Vậy ta có thể biết được tại sao lại bị tự động logout như thế.
    Bây giờ giải pháp sẽ là ngăn chạy lệnh `exit 0`, điều đó khá đơn giản khi ta biết đặc tính của lệnh `more`. Khi nội dung quá nhiều thì lệnh `more` sẽ không thể thực thi hết được và dừng lại, nó sẽ tiếp tục chạy khi ta nhấn `ENTER`. Và đương nhiên là ta chưa thể thay đổi nội dung trong file `text.txt` trở nên nhiều đến mức có thể dừng lệnh `more` nhưng ta có thể làm cho nơi mà lệnh `more` xuất ra nhỏ đi để lệnh `more` tạm dừng .

    ![](https://i.imgur.com/DK1UtSY.png)

    Có thể thấy khi kéo nhỏ terminal lại thì lệnh more chỉ có thể hiển thị được một phần và còn `16%` nội dung chưa thể show 
    
    Bây giờ ta chỉ việc thực hiện đọc `pass` ở thư mục `etc/bandit_pass/bandit26`, để làm được điều đó ta cần phải thực thi được một câu lệnh đọc file. Tại thời điểm này có công cụ giúp ta thực hiện điều đó chính là `vi editor`, ta nhấn `v` để vào `vi editor` *(bạn có thể dùng lệnh `man more` để rõ hơn)*. Sau khi vào `vi editor` thì chỉ cần thực hiện câu lệnh `:r /etc/bandit_pass/bandit26` để đọc tệp `bandit26` và chèn vào sau dòng hiện tại. 
    
    ![](https://i.imgur.com/KVNcW3D.png)

    Nhấn `ENTER` và thế là ta đã giải quyết xong Lv này. Tiếp đến thì chỉ việc thực hiện `:q!` để out.

    ![](https://i.imgur.com/kjC78Is.png)

    Sau khi có pass ta thực hiện kết nối thì thấy chúng ta lại không được hoang nghênh dù đã có đúng mật khẩu. Hay nhờ =))

    ![](https://i.imgur.com/Nz6OMRx.png)

    Vậy thì chúng có lẽ chúng ta đã bỏ sót gì đó rồi. Có lẽ đó chính là `/bin/bash`. Đã đến lúc chúng ta cần thay đổi shell về dạng thông thường rồi. Vẫn tiếp tục vào `vi editor` giống các bước trên. Khi vào được `vi editor` rồi thì thực hiện lệnh `:set shell=/bin/bash` để đổi shell.
    
    ![](https://i.imgur.com/nrU3scF.png)

    Và dùng lệnh `:shell` để thực hiện hoàn thành công đoạn cuối của việc thay đổi đó. Và thế là ta đã thành công đăng nhập vào LV26

    ![](https://i.imgur.com/QpSbyHw.png)

27. **Lv26-Lv27** 

    >pass : YnQpBuifNMas1hcUFk70ZmqkhUU2EuaS
    
    Ở đây ta thử list ra bằng lệnh `ls` thì thấy có file `bandit27-do` và file `text.txt` khi nãy dùng để hiển thị.

    ![](https://i.imgur.com/Hv3s4j0.png)

    Thử thực hiện file `bandit27-do` trường hợp không truyền tham số để xem nó cần truyền gì và tác dụng làm gì.

    ![](https://i.imgur.com/QKnew3U.png)

    Thì có thể thấy file này dùng để thực hiện chạy một command của người dùng khác, khá giống một LV trước đã làm qua thì bây giờ ta chỉ cần đọc file tại `/etc/bandit_pass/bandit27` là hoàn thành LV này. Một LV khá dễ dàng.

    ![](https://i.imgur.com/CZM3Oj9.png)

---

28. **Lv27-Lv28**

    >pass : AVanL161y9rsbcJIsFHuw35rjaOM19nR

    Ở lv này bạn nên tìm hiểu sơ về `git`, đề yêu cầu ta clone repo `ssh://bandit27-git@localhost:2220/home/bandit27-git/repo`.
    Vì ở thư mục `~` không được quyền thực hiện `git clone` nên ta tạo một thư mục mới `ziosbandit27` tại thư mục `tmp` và vào đó để thực hiện `git clone`. Với password của `bandit27-git` tương tự như `bandit27`
    
    ![](https://i.imgur.com/oZk5eMt.png)
    
    Sau khi `git clone` về thì ta có file `repo`, vào và kiểm tra thì thấy có file `README`. Đọc ra thì đó chính là password cho LV tiếp theo.

    ![](https://i.imgur.com/SaUrcUI.png)
---
29. **Lv28-Lv29**

    >pass : tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S

    Tiếp tục thực hiện clone `ssh://bandit28-git@localhost:2220/home/bandit28-git/repo` về và kiểm tra giống LV trước
    
    ![](https://i.imgur.com/qZlixNc.png)
    
    Vào `repo` kiểm tra thì thấy file `README.md` với nội dung là một ẩn số. 

    ![](https://i.imgur.com/y3IAmRl.png)
    
    Bây giờ chúng ta chỉ còn cách xem lại sự hình thành của file này và mong chờ một kết quả tốt bằng lệnh `git log`

    ![](https://i.imgur.com/v9YWBUw.png)
    
    Có thể thấy được rằng là có 3 lần `commit` vậy chúng ta đi kiểm tra lần lượt nội dung tại các lần từ dưới lên bằng lệnh `git show` :
    
    ![](https://i.imgur.com/yC5VQHM.png)

    Commit đầu tiên được tạo với `password = <TBD>`
    
    ![](https://i.imgur.com/cSKALV9.png)

    Commit thứ 2 thì xóa dòng password cũ đi là thêm `password = tQKvmcwNYcFS6vmPHIUSI3ShmsrQZK8S`
    
    ![](https://i.imgur.com/TIySnlO.png)

    Và cái cuối cùng chính là để phòng trường hợp bị lộ thông tin nên đã chuyển mật khẩu về `password = xxxxxxxxxx`
    
    Vậy dễ dàng nhận thấy quá trình hình thành của file qua `git log` và lấy được password một cách dễ dàng.
    
---

30. **Lv29-Lv30**

    >pass : xbhV3HpNGlTIdnjUrdAlPzc2L6y9EOnS
    
    Tiếp tục giống các bước ở LV trên với `ssh://bandit29-git@localhost:2220/home/bandit29-git/repo`

    ![](https://i.imgur.com/IZgxZO8.png)
    
    Kiểm tra thì thấy `passwords = <no passwords in production`

    ![](https://i.imgur.com/L4VzXMS.png)
    
    Kiểm tra log thì cũng không có gì cả,`no passwords in production` đây là một hint cho thấy là nó có thể khôgn nằm trong branch này. Vậy nên dùng lệnh `git branch -a` để kiểm tra tất cả các branch có thể.
    
    ![](https://i.imgur.com/F6dFVOk.png)
    
    Nó đã hiển thị hết tất cả branch, giờ thì chúng ta chỉ việc đi qua từng branch với lệnh `git checkout` .

    ![](https://i.imgur.com/BRiierA.png)
    
    Và kiểm tra hết log để tìm được password.

    ![](https://i.imgur.com/NtI5CiS.png)

    Thật may là cái đầu tiên thì mình đã lấy được password.

    ![](https://i.imgur.com/NQ7Ibrz.png) 

    Có vẻ là may mắn hoặc là designer lv này thích thế. Đương nhiên là tùy trường hợp. Ví dụ như tôi thì tôi không chọn cách brute force bằng tay như thế vì cái gì khó thì để code lo. Nên ta sẽ viết một đoạn code nhỏ để tối ưu việc tìm log.
    ``` shell
    git log |grep "commit"| cut -d " " -f2 |while read line; do git show $line>>myLog.txt;done && cat myLog.txt | grep password
    ```
    
    ![](https://i.imgur.com/mF7D6lU.png)
---
31. **Lv30-Lv31**
    >pass : OoffzGDlzhAlerFJ2cAiz1D41JW1Mhmt

    Tiếp tục giống các bước ở LV trên với `ssh://bandit30-git@localhost:2220/home/bandit30-git/repo`
    
    ![](https://i.imgur.com/yGBxCRS.png)

    Làm lại giống 2 LV trên và không thu được gì cả vì độ khó nó đã khá cao.
    Một số kiên thức liên quan như `git` có một cơ chế đó là `ref`. Đây có thể nói là một cách sử dụng gián tiếp mã hash commit. Chúng ta sẽ đi kiểm tra nó xem. Để có thể xem được nó chúng ta dùng lệnh ` git show-ref`
    
    ![](https://i.imgur.com/sqUABci.png)
    
    Hoặc ta có thể vào file `.git` để đọc thư mục `packed-refs`
    
    ![](https://i.imgur.com/QYqBlpp.png)
    
    Cái `ref` bên trên là của commit còn dưới là một `ref` của tags *(tags khá là tương tự so với commit, chỉ là tag được dùng để trỏ tới mã hash commit)* . Bây giờ  `git show` để lấy được thông tin của tag này. Thì đó không phải là một mã hash commit mà chính là password ta đang tìm.
    
    ![](https://i.imgur.com/kPYei40.png)
    
---

32. **Lv31-Lv32**

    > Pass : rmCBvG56y58BXzv98yZGdO7ATVL5dW8y

    Làm tương tự như các Lv trên với repo `ssh://bandit31-git@localhost:2220/home/bandit31-git/repo`

    ![](https://i.imgur.com/23jxwQP.png)

    Sau khi đọc file `README.md` thì có thể thấy mục tiêu của Lv này là đó là cho ta làm quen với `git push`. Ta cần tạo một file tên `key.txt` với nội dung `May I come in?` và `push` lên branch `master`.

    ![](https://i.imgur.com/z8nHfgL.png)

    Tạo file theo yêu cầu và dùng `git add` để chuẩn bị `git push` nhưng có gì đó không đúng lắm.

    ![](https://i.imgur.com/V48vmjG.png)

    Thử kiểm tra thì thấy có file `.gitignore` với nội dung `*.txt`, tức là sẽ bỏ qua các file có đuôi là `txt` vậy thì ta sẽ dùng thêm option `-f` để xác nhận rằng bạn thực sự muốn thêm file `key.txt` và thực hiện `git push`.

    ![](https://i.imgur.com/J2TX4ym.png)

    Thế là ta đã nhận được password cho LV tiếp theo
    
---
32. **Lv32-Lv33**
    
    > Pass : odHo63fHiFqcWWJG9rLiLDtPm45KzUKy

    Sau khi thực hiện login vào thì ta được đưa vào một `uppercase shell`, nơi mà tất cả những thứ mình nhập sẽ bị in hoa lên. 

    ![](https://i.imgur.com/XmJ1Ut1.png)

    Vậy mục đích của LV này đó chính là làm sao để có thể thực hiện câu lệnh ở đây. Tôi thử nhập một số biến môi trường mà tôi biết xem có gì xảy ra nhưng kết quả nhận lại là không có gì cả.

    ![](https://i.imgur.com/z1lFmte.png)

    Tôi tiếp tục thử với một số `special parameter` và nhận được kết quả khi dùng `$0` và thế là tôi có thể thoát ra khỏi `uppercase shell`, thử kiểm tra thì thấy tôi đã chính là `bandit33` vì vậy tôi chỉ cần đọc password tại `/etc/bandit_pass/bandit33`.

    ![](https://i.imgur.com/ZwuA8Sv.png)

    Sẽ có người thắc mắc rằng `special parameter $0 là gì ?`... Thì đó là một tham số đặc biệt đại diện cho tên `shell` hoặc là tên của `shell script`. Ví dụ khi thực thi một shell code bằng câu lệnh `./scipt input1 input2` thì `$0 = script`, `$1 = input1` và `$2 = input2`. Bạn có thể đọc thêm tài liệu trên `Bash man page` để có thể hiểu rõ hơn về `special parameter`

33. **Lv33-Lv34**

    > pass : 
    
    ![](https://i.imgur.com/VKr7cmR.png)
    
    Vậy là ta đã hoàn thành wargame bandit 
    