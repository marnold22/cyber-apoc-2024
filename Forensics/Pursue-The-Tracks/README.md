# Pursue-The-Tracks

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: Luxx, leader of The Phreaks, immerses himself in the depths of his computer, tirelessly pursuing the secrets of a file he obtained accessing an opposing faction member workstation. With unwavering determination, he scours through data, putting together fragments of information trying to take some advantage on other factions. To get the flag, you need to answer the questions from the docker instance.

## NOTES

1. Start Docker
   1. IP: 83.136.250.12
   2. PORT: 52702
2. Open file
   1. > unzip forensics_pursue_the_tracks.zip
      1. z.mft
3. FILE INFO
   1. > file z.mft
      1. z.mft: data
4. ANALYZE MFT
   1. Using the analyzeMFT python tool lets try running it on our file
      1. > python3 analyzeMFT.py -f z.mft -o export_data
5. INTERACT WITH DOCKER
   1. > nc 83.136.250.12 52702

        ```text
            Luxx, leader of The Phreaks, immerses himself in the depths of his computer, tirelessly pursuing the secrets of a file he obtained accessing an opposing faction member workstation. With unwavering determination, he scours through data, putting together fragments of information trying to take some advantage on other factions. To get the flag, you need to answer the questions from the docker instance.
        ```

   2. QUESTIONS:
      1. Files are related to two years, which are those? (for example: 1993,1995) 
         1. 2023,2024
      2. There are some documents, which is the name of the first file written? (for example: randomname.pdf) 
         1. Final_Annual_Report.xlsx
      3. Which file was deleted? (for example: randomname.pdf)
         1. Marketing_Plan.xlsx
      4. How many of them have been set in Hidden mode? (for example: 43)
         1. 