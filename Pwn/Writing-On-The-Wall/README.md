# Writing-On-The-Wall

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: As you approach a password-protected door, a sense of uncertainty envelops you—no clues, no hints. Yet, just as confusion takes hold, your gaze locks onto cryptic markings adorning the nearby wall. Could this be the elusive password, waiting to unveil the door's secrets?

## NOTES

1. Start Docker
   1. IP: 94.237.48.205
   2. PORT: 59495
2. Unzip contents
   1. > unzip pwn_writting_on_the_wall.zip
      1. glibc, flag.txt, writting_on_the_wall
3. GHIDRA
   1. MAIN()

    ```c
        undefined8 main(void)

        {
        int iVar1;
        long in_FS_OFFSET;
        char local_1e [6];
        undefined8 local_18;
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        local_18 = 0x2073736170743377;
        read(0,local_1e,7);
        iVar1 = strcmp(local_1e,(char *)&local_18);
        if (iVar1 == 0) {
            open_door();
        }
        else {
            error("You activated the alarm! Troops are coming your way, RUN!\n");
        }
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return 0;
        }
    ```

    2. So it looks like we do s string comparison which sets the iVar1 variable, and we need it to be 0 to open_door()
    3. The read() function looks to have a buffer size of 6

   2. OPEN_DOOR()

    ```c
        void open_door(void)

        {
        ssize_t sVar1;
        long in_FS_OFFSET;
        char local_15;
        int local_14;
        long local_10;
        
        local_10 = *(long *)(in_FS_OFFSET + 0x28);
        local_14 = open("./flag.txt",0);
        if (local_14 < 0) {
            perror("\nError opening flag.txt, please contact an Administrator.\n");
                            /* WARNING: Subroutine does not return */
            exit(1);
        }
        printf("You managed to open the door! Here is the password for the next one: ");
        while( true ) {
            sVar1 = read(local_14,&local_15,1);
            if (sVar1 < 1) break;
            fputc((int)local_15,stdout);
        }
        close(local_14);
        if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                            /* WARNING: Subroutine does not return */
            __stack_chk_fail();
        }
        return;
        }
    ```
