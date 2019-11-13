#STEP

Common
- mkdir "for-mount"
(for qemu)
- prepare qemu script and defconfig file at dir "qemu-scripts"
- mkdir "tizen-image"

in case of rpi3 device
1. ./set_rpi3_env.py (modify team list and branch name to checkout)
    - ./clone_all_projs.py
    - ./checkout_and_build.py
    - ./mkimg_and_tar.sh
2. (It is better to do it manually...) ./build_tester.py
   - make with Makefile or,
   - arm-linux-gnueabi-gcc -I"your kernel path"/include "test.c" -o test
3. insert SD card and do flashing. (ex) sudo ./flash-sdcard.sh /dev/sdc
4. ./mount_and_move_file_rpi3.sh "sdX2" "file"

in case of qemu
1. ./set_qemu_env.py (modify team list and branch name to checkout)
2. ./build_tester.py
3. ./mk_env_per_team.sh "team number"
4. ./mount_and_move_file_qemu.sh "file"
5. "team-repo"/qemu.sh
