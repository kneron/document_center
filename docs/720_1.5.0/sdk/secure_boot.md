# Secure Boot
Kneron KL720 provide secure protect with AES and SHA. The boot mechanism will apply AES 256 CBC mode and SHA256. For AES, this requires 256 bits Key and 128 bits IV to encrypt or decrypt the data. For SHA, this requires 256 bits space on SPI flash to keep the hash value.   

The SEC_EN bit from eFuse is used to decide if the secure boot mechanism should be applied or ignored. The content of 32 bits authentication number, the 256 bits Key and 128 bits IV inside eFuse should be decided and write to eFuse before the SEC_EN bit is set.  If the  SEC_EN bit of eFuse is 1. The boot flow will enter secure boot, and the firmware of SPL, SCPU and NCPU need be encrypted with the correct key. 

![](../imgs/sdk/secure_boot_flow.png)


## 1. eFuse Programming

The eFuse data will be programmed during chip or module production. The eFuse's data contains the following vendor's key information. The user only obtains the encrypted key(sbtkey.bin) and uses the sbtenc tool to perform firmware secure boot encryption.

* Auth value: 32bits 
* AES key size: 256bits
* IV: 128bits

## 2. Build Firmware and Create Encrypted Binary File

If the SEC_EN bit of eFuse is 1. The boot flow will enter secure boot, and the firmware of SPL, SCPU and NCPU need be encrypted with the correct key. We provide a "sbtenc.exe" tool for users to encrypt their firmware with SBT key(sbtkey.bin) for secure boot. You can refer the example projects of secure boot for SPL, SCPU and NCPU.
```
sbtenc.exe optional arguments: 
    -h, --help          Show this help message and exit
    -hd, --header       Add header file.
    -e, --encrypt       AES encryption.
    -i INFILE, --infile INFILE
                        Input firmware file for AES encryption.
    -o OUTFILE, --outfile OUTFILE
                        Encrypted output file.
    -s SBTKEYFILE, --sbtkeyfile SBTKEYFILE
                        Secure boot key file(sbtkey.bin)
Example Command:
Encrypt firmware with user's sbtkey file(sbtkey.bin).
​    sbtenc.exe -e -i fw_scpu_tmp.bin -o fw_scpu_enc.bin -s keys\sbtkey.bin.
```


## 3. KL720 SDK Secure Boot Example

The following are the example projects and post_build_enc.bat for secure boot on the KL720 SDK.
Please reference the post_build_enc.bat for firmware encryption.
```
Example key. 
    .\firmware\utils\sbtenc\keys\sbtkey.bin
        
Example projects for SPL, SCPU and NCPU.
​    SPL 
​        .\firmware\platform\kl720\scpu\spl\sn72096_9x9\scpu_keil\spl_enc.uvprojx
​    SCPU 
        .\firmware\build\example_sbt\scpu\sn72096_9x9\scpu_keil\scpu_enc.uvprojx
​    NCPU 
        Xtensa workspace and import HelloWorld project
​        .\firmware\build\example_sbt\ncpu\
```
After the project is built, please run flash programming to update the flash data.
```
    .\firmware\utils\JLink_programmer\flash_prog_enc.bat
```
Secure boot success message.
![](../imgs/sdk/secure_boot_ok.png)

Secure boot fail message.
![](../imgs/sdk/secure_boot_fail.png)

