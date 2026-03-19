# Turing Test and CAPTCHA – High Level Architecture

PART 1: TURING TEST ARCHITECTURE

1. Overview
The Turing Test evaluates whether an AI system can produce responses indistinguishable from a human in a text-based conversation. A human judge interacts with two hidden participants: one human and one AI model.

2. High-Level Architecture

 . Judge Interface
- Command-line interface (CLI)
- Accepts questions from the judge
- Displays anonymized responses (Entity A / Entity B)
- Collects final decision

2. Conversation Controller
- Sends each question to both participants
- Maintains conversation history
- Ensures anonymity
- Controls session flow

3. Human Module
- Accepts question
- Returns human-written response

4. AI Agent Module
- Formats conversation history into a prompt
- Sends request to cloud-hosted LLM (Zephyr-7B via Hugging Face Router)
- Receives generated response
- Returns AI reply to controller

5. Evaluation Module
- Collects judge’s guess
- Compares guess with actual AI identity
- Outputs result

3. Data Flow
Judge Question → Controller →
• Human Module → Human Response
• AI Module → LLM → AI Response
Responses → Judge → Final Decision


PART 2: TEXT-BASED CAPTCHA ARCHITECTURE

1. Overview
A CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) is a challenge–response mechanism used to determine whether the user is human.

In this implementation, a distorted text image ("smwn") is displayed to the user, and the user must correctly type the text to proceed.

2. High-Level Architecture

1. CAPTCHA Image Module
- Stores distorted image file (captchaimage.png)
- Contains hidden correct answer ("smwn")
- Sends image to user interface

2. User Interface Module
- Displays CAPTCHA image
- Accepts user input
- Sends input for verification

3. Verification Module 
- Receives user input
- Normalizes input (lowercase, trimmed spaces)
- Compares input with stored correct value
- Returns success or failure

4. Attempt Control Module
- Limits number of attempts
- Blocks access after maximum failures

3. How It Works
    1. System displays distorted text image.
    2. User visually interprets the text.
    3. User submits typed response.
    4. System compares input with stored answer.
    5. If matched → user verified as human.
    6. If not → retry or block.

4. Why It Works 
- Humans are naturally strong at visual pattern recognition, even with distortion.
- Basic automated bots struggle with distorted or noisy text.
- The system relies on the assumption that visual perception is easier for humans than for simple scripts.

This makes it a practical challenge to response authentication mechanism for filtering automated submissions.


