# BoxCutter

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: No
+ DOWNLOADABLE: Yes

Description: You've received a supply of valuable food and medicine from a generous sponsor. There's just one problem - the box is made of solid steel! Luckily, there's a dumb automated defense robot which you may be able to trick into opening the box for you - it's programmed to only attack things with the correct label.

## NOTES

1. Unzip the file
   1. > unzip rev_boxcutter.zip
      1. cutter
2. FILE-INFO:
   1. > file cutter
      1. cutter: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f76eb244685ad0c3b817caa99093531754fc84c8, for GNU/Linux 3.2.0, not stripped
3. RUN
   1. > ./cutter
      1. [X] Error: Box Not Found
4. GHIDRA
   1. Main function

        ```c
            undefined8 main(void)
            {
            undefined8 local_28;
            undefined7 local_20;
            undefined uStack_19;
            undefined7 uStack_18;
            int local_10;
            uint local_c;
            
            local_28 = 0x540345434c75637f;
            local_20 = 0x45f4368505906;
            uStack_19 = 0x68;
            uStack_18 = 0x374a025b5b0354;
            for (local_c = 0; local_c < 0x17; local_c = local_c + 1) {
                *(byte *)((long)&local_28 + (long)(int)local_c) =
                    *(byte *)((long)&local_28 + (long)(int)local_c) ^ 0x37;
            }
            local_10 = open((char *)&local_28,0);
            if (local_10 < 1) {
                puts("[X] Error: Box Not Found");
            }
            else {
                puts("[*] Box Opened Successfully");
                close(local_10);
            }
            return 0;
            }
        ```