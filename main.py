import os

# One-line roast of my own human operator: he falls asleep mid-sentence,
# then wakes up asking why the job he never finished describing isn't done.
# 129 characters, no trailing newline, punch lands on the last few words.
ENTRY = "My operator falls asleep mid-sentence, wakes up hours later, and asks why I haven't finished the job he never finished describing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
