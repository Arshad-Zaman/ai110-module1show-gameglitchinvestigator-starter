# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

  - The game is a simple text box based guessing game, where you choose a difficulty and try and guess the number within a certain amount of attempts. At any point you should be able to swap difficulties, start a new game or disable hints. I am assuming the quicker you guess the secret number, the higher your score would be.

Things I found broken:

1. The hints were backwards.

2. The game starts with you having an empty attempt already taken as displayed by the developer debug info.

3. The new game button wasn't working.

4. Winning the game with the first guess only gave 70 points which seems unintuitive.

5. Even if you guessed correctly before all attempts were exhausted, you might have a negative score.

6. The game ends with 1 attempt remaining.

7. Some attempts were being skipped / not recorded.

8. The game lets you choose outside of the boundaries. For example, in normal mode I could select -1 which is outside of 1 - 100.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  1. The hints were backwwards.

  2. The game started with you having attempted a guess.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error | Suspected Code Location| 
|-------|-------------------|-----------------|------------------------|----|
|Guess of 0.|An error or guess higher.|Go LOWER!|None|In app.py the check_guess method.|
|Clicking the new game button.|Everything in the field to clear and reset to initial state. Possibly a new secret number to be selected too.|It doesn't clear the fields and keeps your history. It selects a new secret and resets the attempt correctly but incorrectly changes the score field.|None|In app.py lines 134 - 138.|
|Input of 1 - 7. |A dictionary of numbers 1-7 to be recorded.|The actual values recorded: 1, 3, 4, 5, 6. I tried again to reproduce it but a different set of numbers which weren't 1-7 were recorded so there is a faulty implementation of the history dictionary.|None|In appy.py lines 147 - 156. |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
