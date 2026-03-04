# Turing Test – High Level Architecture

## 1. Overview
The Turing Test evaluates whether an AI system can produce responses that are indistinguishable from a human in a text-based conversation. A human judge interacts with two hidden participants: one human and one AI model. The judge must determine which participant is the machine.

---

## 2. High-Level Architecture

### 1. Judge Interface (Client Layer)
- Command-line interface (CLI)
- Accepts questions from the judge
- Displays anonymized responses (Entity A / Entity B)
- Collects final decision

### 2. Conversation Controller (Application Layer)
- Receives judge questions
- Sends the same question to both participants
- Maintains conversation history
- Ensures anonymity
- Controls overall session flow

### 3. Human Participant Module
- Accepts question
- Returns human-written response

### 4. AI Agent Module (LLM-Based)
- Formats conversation history into structured prompt
- Sends request to cloud-hosted Large Language Model
- Receives generated response
- Returns AI reply to controller

### 5. Evaluation Module
- Collects judge’s guess
- Compares guess with actual AI identity
- Outputs final result

---

## 3. Model Used

The AI agent uses a cloud-hosted Large Language Model:

Model: Zephyr-7B (Instruction-tuned)
Provider: Hugging Face Inference Router API
Access Method: HTTP POST request with authentication token

The model generates context-aware responses based on the entire conversation history. The Inference Router acts as an API gateway between the local Python application and the hosted model.

---

## 4. Data Flow

Judge Question
      ↓
Conversation Controller
      ↓
Human Module → Human Response
AI Module → Hugging Face Router → Zephyr-7B Model → AI Response
      ↓
Responses shown anonymously to Judge
      ↓
Judge makes final decision

---

## 5. Architectural Characteristics
- Modular and layered design
- Clear separation between interface, logic, and AI processing
- Context-aware response generation
- Secure token-based authentication
- Scalable to web-based or multi-user versions

This architecture demonstrates how a modern LLM can be integrated into a structured evaluation framework to simulate the classical Turing Test.
