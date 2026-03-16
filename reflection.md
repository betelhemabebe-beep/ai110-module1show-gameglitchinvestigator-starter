# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
There was a box where I could put my guess. Show hint was selected by default. The difficulty was also selected by default. There was developer debug info drop down.
- List at least two concrete bugs you noticed at the start  
1. Hard difficulty had a range of 1–50, which was easier than Normal (1–100).
2. On every other guess, hints were wrong — guessing 9 with secret 10 said "Go LOWER."
3. The attempts counter started at 1 instead of 0, so you silently lost one attempt before guessing.
4. The info banner always said "between 1 and 100" no matter which difficulty was selected.
5. New Game always picked a number between 1 and 100, ignoring the selected difficulty.
6. New Game did not reset your history or score from the previous game.
7. Wrong guesses on even-numbered attempts gave +5 points instead of deducting 5.
8. A first-attempt win only gave 80 points instead of 100.
9. the emoji next to the hint was not correct.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
it was able to fix the issue. 

The AI identified and fixed all 8 bugs in the code. For example, on every other attempt the secret number was being converted to a string, causing wrong hints because Python compares strings by character order. Guessing 9 with a secret of 10 would say "Go LOWER" instead of "Go HIGHER." The AI fixed this by always keeping the secret as an integer. Other bugs included Hard difficulty having a range of 1 to 50 which was easier than Normal, the attempts counter starting at 1 instead of 0 so you silently lost one attempt, the info banner always showing "between 1 and 100" regardless of difficulty, New Game ignoring the selected difficulty and not resetting history or score, wrong guesses on even attempts giving +5 points instead of deducting 5, and a first-attempt win only awarding 80 points instead of 100. I verified the fixes by playing the game and confirming hints, scores, and difficulty ranges all behaved correctly.

- Give one example of an AI suggestion that was incorrect or misleadin (including what the AI suggested and how you verified the result).

The AI suggested adding a full guess history display section to the UI, showing every guess with icons and results. I undid this change because the game already had a Developer Debug Info section that showed the history, so adding another display was unnecessary and cluttered the page. I verified it was not needed by checking that the debug panel already had the information.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

i reran the program and tested it manually

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

  I ran python -m pytest tests/test_game_logic.py -v after the fixes. The new test test_guess_above_secret_is_too_high_not_too_low checked that check_guess(9, 10) returns "Too Low", which would have failed before the fix because the string comparison made "9" > "10" return True and gave the wrong hint. All 4 tests passing confirmed the logic was correct.

- Did AI help you design or understand any tests? How?

The AI pointed out that the existing 3 starter tests were all broken because they compared check_guess(...) directly to a string like "Win", but the function actually returns a tuple (outcome, message). The tests would have always failed without that fix. The AI also designed the new test specifically targeting the string comparison bug, which helped me understand exactly what the bug was doing and why check_guess(9, 10) was the right case to test.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.

The line random.randint(low, high) was being called every rerun, so a brand new secret number was picked each time before you could even guess.

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

every click reran the whole script of the whole page

- What change did you make that finally gave the game a stable secret number?

Wrapping the secret generation in if "secret" not in st.session_state meant the random number only gets picked once 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

  Writing pytest tests right after fixing a bug. instead of checking manually
  
- What is one thing you would do differently next time you work with AI on a coding task?

I would verify every AI suggestion before accepting it instead of trusting it automatically. The AI suggested adding a history display to the UI which I had to undo because it was unnecessary 

- In one or two sentences, describe how this project changed the way you think about AI generated code.

AI generated code looks correct at first glance but can have subtle logic bugs hiding in it
