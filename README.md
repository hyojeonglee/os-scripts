***Common***
- mkdir "for-mount"
- prepare qemu script and defconfig file at dir "qemu-scripts" (only for qemu)
- mkdir "tizen-image" (only for qemu)

***in case of rpi3 device***
1. ./set_rpi3_env.py (modify team list and branch name to checkout)
2. (It is better to do it manually...) ./build_tester.py
   - make with Makefile or,
   - arm-linux-gnueabi-gcc -I"your kernel path"/include "test.c" -o test
3. insert SD card and do flashing. (ex) sudo ./flash-sdcard.sh /dev/sdc
4. ./mount_and_move_file_rpi3.sh "sdX2" "file"

***in case of qemu***
1. ./set_qemu_env.py (modify team list and branch name to checkout)
2. (It is better to do it manually...) ./build_tester.py
   - make with Makefile or,
   - arm-linux-gnueabi-gcc -I"your kernel path"/include "test.c" -o test
3. ./mk_env_per_team.sh "team number"
4. ./mount_and_move_file_qemu.sh "file"
5. "team-repo"/qemu.sh
