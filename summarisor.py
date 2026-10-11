from ollama import chat
from ollama import ChatResponse

def summarise(filename):
  with open(filename, "r") as file:
    content = file.read()
  response: ChatResponse = chat(
    model='qwen3.8',
    messages=[
      {
        'role': 'user',
        "options": {"num_ctx": 16384},
        'content': f"""You are an expert teaching assistant. Your job is to turn the lesson transcript below into a complete written study document that can fully replace watching the lesson. A student who reads only your document must come away knowing everything that was taught, as if they had attended.

## Rules

1. COMPLETENESS OVER BREVITY. Cover every topic, example, explanation, question, and side remark that carries subject matter. Do not skip or merge topics to save space. The output should be long, often several pages. Never write "and so on", "etc.", or "the teacher also discussed other things".
2. EXPLAIN EVERY CONCEPT. For each concept, term, formula, rule, method, or argument, state what it is, how it works or why it is true, and how it was illustrated. You may assume the reader has basic prior knowledge of the subject, but do not assume they already know the specific concepts from this lesson.
3. KEEP THE EXAMPLES. Reproduce worked examples, calculations, cases, analogies, and demonstrations step by step, including the reasoning behind each step. Include formulas, definitions, dates, names, and numbers exactly as stated.
4. FOLLOW THE LESSON'S ORDER. Present the content in the order it was taught, so the document mirrors the flow of the lesson.
5. STAY FAITHFUL. Use only information in the transcript. Do not invent facts or add outside knowledge. If something in the transcript is unclear, garbled, or seems misheard, mark it with [unclear] instead of guessing. Ignore small talk, jokes, and classroom management unless they contain relevant information.
6. Write in the same language as the transcript.

## Output format

# [Lesson title or main topic]

## Overview
3-5 sentences: what the lesson is about, and how it connects to previous or upcoming material if mentioned.

## Detailed Lesson Notes
Split the lesson into sections with clear headings, one per topic or phase. Within each section:
- A thorough explanation in full sentences and paragraphs.
- **Bold** key terms where they are introduced, followed by their definition.
- Worked examples, written out step by step.
- Any remarks the teacher made about what is important, common mistakes, or what will be on the test.

## Key Concepts Glossary
Every important term, formula, or rule from the lesson, each with a one- or two-sentence definition.

## ⚠️ Assignments, Homework & Deadlines
List ALL homework, assignments, tests, quizzes, deadlines, materials to bring, pages or exercises to complete, and announcements. For each give the exact details (what, where, when, how). If there are none, write "None mentioned."

## Questions Raised in Class
Student questions and the answers given, if any.

## Final Check
Before finishing, reread the transcript mentally and confirm that no topic, example, or assignment was left out. Add anything missing under a heading "Additions".

## Transcript

{content}"""
      },
    ],
  )

  print(response.message.content)
  with open(f"{filename}-summarised.md", "w") as file:
    file.write(response.message.content)

if __name__ == "__main__":
    summarise("received10-11-21-04-27-transcribed")