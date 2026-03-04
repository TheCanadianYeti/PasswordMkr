# PasswordMkr

> A simple Python password generator — built because most online generators are ad-riddled.

---

## Overview

PasswordMkr is a lightweight personal utility that generates a random password directly in your terminal. You choose the length and whether to include special characters, and it outputs a password instantly. No ads, no browser, no bloat.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3** | Core language |
| **`random`** | Character selection |

No external dependencies — just the Python standard library.

---

## How It Works

1. You're prompted to enter a desired password length (whole numbers only)
2. You're asked whether to allow special characters (`y/n`)
3. A password is randomly assembled from the enabled character sets and printed to the terminal

### Character Sets

| Set | Characters |
|-----|-----------|
| Lowercase | `a–z` |
| Uppercase | `A–Z` |
| Numbers | `0–9` |
| Symbols *(optional)* | `!@#$%^&*()[]{}-_+=~` |

---

## Usage

```bash
python psrdmkr.py
```

```
How many characters long?: 16
Are special characters allowed (y/n)?: y
Ok, special characters added.
Your password is: aB3!xZ9@Lm#2Yw&q
```

---

## Motivation

Most online password generators are cluttered with ads or require trusting a third-party site. This is a quick, offline, no-nonsense alternative you can run locally anytime.

---

## Status

✅ **Complete** — Does exactly what it needs to. Built as a personal utility.

---

## Author

Built by [TheCanadianYeti](https://github.com/TheCanadianYeti)
