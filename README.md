# AI Concepts Implementation Project

This repository contains three AI concept implementations:

1. Missionaries and Cannibals (Uninformed Search)
2. Text-Based CAPTCHA System
3. Simple Turing Test Simulation

Each section explains what the program does and how to run it locally.

---

# 1️⃣ Missionaries and Cannibals – Uninformed Search

## Overview

This program solves the classic Missionaries and Cannibals problem using:

* Breadth-First Search (BFS)
* Depth-First Search (DFS)
* Depth-Limited DFS (DLS)
* Iterative Deepening DFS (IDDFS)

### State Representation

Each state is represented as:

```
(M_left, C_left, Boat)
```

Where:

* `M_left` → Number of missionaries on the left bank
* `C_left` → Number of cannibals on the left bank
* `Boat` → `0` (boat on left), `1` (boat on right)

Start State:

```
(3, 3, 0)
```

Goal State:

```
(0, 0, 1)
```

The program ensures:

* Missionaries are never outnumbered by cannibals on either side.
* Only valid states are explored.

---

## How to Run

### 1️⃣ Make sure Python is installed

```bash
python3 --version
```

### 2️⃣ Run the program

```bash
python3 cannibal.py
```

### 3️⃣ Choose a search strategy

You will be prompted:

```
1 - BFS
2 - DFS
3 - Depth-Limited DFS
4 - Iterative Deepening DFS
```

The program will print the solution path if found.

---

# 2️⃣ Text-Based CAPTCHA System

## Overview

This is a simple CAPTCHA verification system that checks whether the user correctly enters the text shown in an image.

It simulates how websites distinguish between humans and bots.

The CAPTCHA image (example: `smwn`) must be stored at:

```
TTandCaptcha/captchaimage.png
```

---

## How It Works (High-Level)

1. A predefined text is embedded inside an image.
2. The image is displayed to the user.
3. The user types the text they see.
4. The program compares the input with the expected value.
5. If correct → Access Granted
   If incorrect → Access Denied

This works because automated bots generally struggle with reading distorted image-based text without advanced OCR systems.

---

## How to Run

Make sure the image exists at:

```
TTandCaptcha/captchaimage.png
```

Then run:

```bash
python3 captcha.py
```

Enter the text shown in the image when prompted.

---

# 3️⃣ Simple Turing Test Simulation

## Overview

This program simulates a simplified version of the Turing Test.

It:

* Accepts user questions
* Sends them to a language model
* Returns human-like responses

The goal is to demonstrate basic conversational AI behavior.

---

## High-Level Architecture

1. User Input
2. Model Processing (LLM or API call)
3. Response Generation
4. Output to User

The program runs in a loop until the user exits.

---

## How to Run

### Option 1: Using Hugging Face API

Set your Hugging Face token:

```bash
export HF_TOKEN="your_token_here"
```

Then run:

```bash
python3 turing_test.py
```

---

### Option 2: Using a Local Model

Simply run:

```bash
python3 turing_test.py
```

(Ensure required dependencies are installed if your implementation uses them.)

---

# Project Structure

```
/TTandCaptcha
    captchaimage.png
    captcha.py

cannibal.py
turing_test.py
README.md
```

---

# Requirements

* Python 3.8+
* Internet connection (only required for Turing Test if using API)
* No external libraries required unless using external model APIs

---

# Educational Purpose

This repository demonstrates:

* Uninformed Search Algorithms
* State-Space Problem Solving
* CAPTCHA-Based Human Verification
* Conversational AI Architecture
* Basic Turing Test Simulation

It is intended for academic learning and AI fundamentals practice.
