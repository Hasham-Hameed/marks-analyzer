# Marks Analyzer

A Python script that takes 5 subject marks (out of 100) as input and analyzes them: total, average, highest mark, and number of subjects passed.

## What it does

- Takes 5 numbers (marks out of 100) as input from the user
- Calculates the total of all marks
- Calculates the average (rounded to 2 decimal places)
- Finds the highest mark obtained
- Counts how many subjects were passed (marks >= 50)
- Prints all of the above

## How to run

```bash
python marks_analyzer.py
```

You'll be prompted to enter 5 marks one by one.

## Example

```
Enter your marks(out of 100): 80
Enter your marks(out of 100): 40
Enter your marks(out of 100): 55
Enter your marks(out of 100): 30
Enter your marks(out of 100): 90
The numbers you obtained are: [80, 40, 55, 30, 90]
The total obtained marks are: 295
The average of your marks is: 59.00
The maximum marks you have obtained in a subject are: 90
The number of subjects in which you have passed are: 3
```

## Status

This is a small, growing learning project. It started as a simple total/largest-mark script and has been upgraded step by step to add average and pass/fail counting.

Planned improvements:
- Input validation (handle non-numeric input)
- Support for any number of subjects, not just 5
- Show which subjects failed, not just the count
- Let the user set a custom pass mark instead of a hardcoded 50

## Author

Built while learning Python fundamentals: functions, loops, and conditionals.
