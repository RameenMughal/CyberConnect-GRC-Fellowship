# Riddle Registry 🧩🗂️

Platform: [PicoCTF](https://play.picoctf.org/)

Challenge: [Riddle Registry](https://play.picoctf.org/practice/challenge/530?category=4&difficulty=1&page=1&search=Riddle)

## Description

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered.

Download the PDF file and uncover the flag within the metadata.

## Solution

By downloading the file, we see 1 page document having content that might look important but is not because there are some black lines to cover some words.

I checked those by copying and pasting them to other medium such as Notepad but it was nothing special.

Example: Copy pasting the first black line gives: Aenean lacinia bibendum nulla sed consectetur

<img width="491" height="190" alt="image" src="https://github.com/user-attachments/assets/b3685b71-7c90-4867-a939-d7689ce42095" />

We will check the metadata of this PDF file by `exiftool` command.

Download the PDF file in Linux by `wget https://challenge-files.picoctf.net/c_amiable_citadel/3f00b89eeac6ac5242f747889ea4de24c804d9144cfa71e23d754e6a8e80e435/confidential.pdf`

<img width="941" height="143" alt="image" src="https://github.com/user-attachments/assets/823f1e43-f657-4412-9cd7-6ae7131f3754" />

Check the metadata of this PDF file by: `exiftool confidential.pdf`

<img width="463" height="241" alt="image" src="https://github.com/user-attachments/assets/8e4fb633-67b3-4ab4-9182-ab5cf0c24c0d" />

This gives us the encoded text at the `Author` tag `cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jOTk5ZTJhNH0=` and the `=` indicates that it is base64 encoded text.

Decoding this text at [CyberChef](https://gchq.github.io/CyberChef/) website by choosing `From Base64` then we get the flag!

<img width="1303" height="595" alt="image" src="https://github.com/user-attachments/assets/eb4522e2-a24f-425c-9102-eee91613d3f1" />
