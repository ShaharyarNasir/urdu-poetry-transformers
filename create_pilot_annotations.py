import csv
import os

poems = [
    {
        "poem_id": "ghalib_001",
        "poet": "Mirza Ghalib",
        "era": "19th century",
        "form": "ghazal",
        "couplets": [
            ("دل ہی تو ہے نہ سنگ و خشت", "درد سے بھر نہ آئے کیوں"),
            ("ہزاروں خواہشیں ایسی", "کہ ہر خواہش پہ دم نکلے"),
            ("ہستی کا اثبات کچھ اور بھی ہے",
             "دل کو بہلانے کے لیے کچھ خواب ہوں بھی ہیں"),
            ("دوا ہے غم کی دوا کہاں", "دوا کہ ہم کو تجھ سے وفا کہاں"),
        ]
    },
    {
        "poem_id": "iqbal_001",
        "poet": "Allama Iqbal",
        "era": "20th century",
        "form": "nazm",
        "couplets": [
            ("ستاروں سے آگے جہاں اور بھی ہیں", "ابھی عشق کے امتحاں اور بھی ہیں"),
            ("خودی کو کر بلند اتنا کہ ہر تقدیر سے پہلے",
             "خدا بندے سے خود پوچھے بتا تیری رضا کیا ہے"),
        ]
    },
    {
        "poem_id": "mir_001",
        "poet": "Mir Taqi Mir",
        "era": "18th century",
        "form": "ghazal",
        "couplets": [
            ("پاتا نہیں ہوں کہیں دل کو قرار کہیں",
             "دھوپ چھاؤں میں جیتا ہوں میں سارے دن"),
            ("میرے دل کے شہر میں اندھیری رات ہے",
             "نہ کوئی دوست ہے نہ کوئی رفیق ہے"),
        ]
    },
    {
        "poem_id": "bulleh_001",
        "poet": "Bulleh Shah",
        "era": "18th century",
        "form": "kafi",
        "couplets": [
            ("بول کہ لب آزاد ہیں تیرے", "بول زباں اب تک تیری ہے"),
            ("مٹی دی لو دا پہر آیا", "رات دی واری دا سہر آیا"),
        ]
    }
]

os.makedirs("data/annotated", exist_ok=True)

with open("data/annotated/pilot_annotations.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["poem_id", "couplet_id", "line1",
                    "line2", "couplet", "poet", "era", "meter"])
    for poem in poems:
        for i, (line1, line2) in enumerate(poem["couplets"], start=1):
            couplet_id = i
            couplet = f"{line1} {line2}"
            writer.writerow([poem["poem_id"], couplet_id, line1, line2,
                            couplet, poem["poet"], poem["era"], poem["form"]])


print("✅ data/annotated/pilot_annotations.csv created.")
