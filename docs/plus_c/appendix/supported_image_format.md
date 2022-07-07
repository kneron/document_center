## Supported Image Format

---

| Format                                | Byte3               | Byte2               | Byte1               | Byte0               | Comment                                        |
| ------------------------------------- | ------------------- | ------------------- | ------------------- | ------------------- | ---------------------------------------------- |
| KP\_IMAGE\_FORMAT\_RGB565             | R1\[4:0\],G1\[5:3\] | G1\[2:0\],B1\[4:0\] | R0\[4:0\],G0\[5:3\] | G0\[2:0\],B0\[4:0\] |                                                |
| KP\_IMAGE\_FORMAT\_RGBA8888           | A                   | B                   | G                   | R                   |                                                |
| KP\_IMAGE\_FORMAT\_YUYV               | Cr                  | Y1                  | Cb                  | Y0                  | Equal to KP\_IMAGE\_FORMAT\_YCBCR422\_Y0CBY1CR |
| KP\_IMAGE\_FORMAT\_YCBCR422\_CRY1CBY0 | Y0                  | Cb                  | Y1                  | Cr                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_CBY1CRY0 | Y0                  | Cr                  | Y1                  | Cb                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_Y1CRY0CB | Cb                  | Y0                  | Cr                  | Y1                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_Y1CBY0CR | Cr                  | Y0                  | Cb                  | Y1                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_CRY0CBY1 | Y1                  | Cb                  | Y0                  | Cr                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_CBY0CRY1 | Y1                  | Cr                  | Y0                  | Cb                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_Y0CRY1CB | Cb                  | Y1                  | Cr                  | Y0                  |                                                |
| KP\_IMAGE\_FORMAT\_YCBCR422\_Y0CBY1CR | Cr                  | Y1                  | Cb                  | Y0                  |                                                |
| KP\_IMAGE\_FORMAT\_RAW8               | N3                  | N2                  | N1                  | N0                  | NIR image format                               |  
