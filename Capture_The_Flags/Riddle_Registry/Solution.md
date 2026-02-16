# Riddle Registry

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

We will check the metadata of this PDF file by exiftool command.

