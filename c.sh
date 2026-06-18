printf "\ec\e[47;31m\ngive me c file?\n"
read a
gcc -fPIC -fPIE -pie -fpic -m64 -fno-stack-protector -fomit-frame-pointer -finline-functions -fno-zero-initialized-in-bss -o $a.elf $a


