
def book_word_count(content):
    wordcount = 0
    words = content.split()
    for word in words:
        wordcount += 1
    return wordcount


def character_count(content):
    character_counts = {}
    lowered_string = content.lower()
    for char in lowered_string:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    
    return character_counts


def char_report(character_counts):
    report = []
    for char, count in character_counts.items():
        if char.isalpha():
            new_entry = {"char": char, "count": count}
            report.append(new_entry)
    report.sort(key=lambda x: x["count"], reverse=True)
    return report

def main():
    with open("books/frankenstein.txt", "r") as file:
        content = file.read()
        wordcount = book_word_count(content)
        character_counts = character_count(content)
        report = char_report(character_counts)

        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{wordcount} words found in the document")
        for entry in report:
            char, count = entry['char'], entry['count']
            print(f"The '{char}' character was found {count} times")
        print(f"--- End report ---")
        

if __name__ == "__main__":
    main()
        


