# create_raw_data.py
import csv
import os


def normalize_line(line):
    # Simple normalization: replace Arabic letter variations to a standard form
    # (you can improve this function as needed)
    replacements = {
        "ي": "ی",
        "ك": "ک",
        "ہي": "ہی",
        "سي": "سے",
        "کي": "کی",
        "کيوں": "کیوں",
        "ہون": "ہوں",
        "آيا": "آیا",
        "دے": "دے",
    }
    for old, new in replacements.items():
        line = line.replace(old, new)
    return line


poems = [
    {
        "poem_id": "mir_001",
        "poet": "Mir Taqi Mir",
        "era": "18th century",
        "form": "ghazal",
        "source": "public_domain",
        "couplets": [
            ("پاتا نہیں ہوں کہیں دل کو قرار کہیں",
             "دھوپ چھاؤں میں جیتا ہوں میں سارے دن"),
            ("میرے دل کے شہر میں اندھیری رات ہے",
             "نہ کوئی دوست ہے نہ کوئی رفیق ہے"),
        ]
    },
    {
        "poem_id": "ghalib_001",
        "poet": "Mirza Ghalib",
        "era": "19th century",
        "form": "ghazal",
        "source": "public_domain",
        "couplets": [
            ("ہزاروں خواہشیں ایسی کہ ہر خواہش پہ دم نکلے",
             "بہت نکلے میرے ارمان لیکن پھر بھی کم نکلے"),
            ("دل ہی تو ہے نہ سنگ و خشت درد سے بھر نہ آئے کیوں",
             "روئیں گے ہم ہزار بار کوئی ہمیں ستائے کیوں"),
            ("ہستی کا اثبات کچھ اور بھی ہے",
             "دل کو بہلانے کے لیے کچھ خواب ہوں بھی ہیں"),
            ("دوا ہے غم کی دوا کہاں", "دوا کہ ہم کو تجھ سے وفا کہاں"),
        ]
    },
    {
        "poem_id": "mir_002",
        "poet": "Mir Taqi Mir",
        "era": "18th century",
        "form": "ghazal",
        "source": "public_domain",
        "couplets": [
            ("پتا پتا، بوٹا بوٹا حال ہمارا جانے ہے",
             "جانے نہ جانے گل ہی نہ جانے باغ تو سارا جانے ہے"),
            ("عاشقی صبر طلب اور تمنا بے تاب ہے",
             "دل کا کیا رنگ کروں خون جگر ہونے تک"),
            ("چپ ہیں ذرہ ذرہ بکھرے ہوئے، ہوا کے گیت سن رہے",
             "دل کی صدا ہے کوئی، سن لے صدا کے قصے"),
            ("دل میں اک لہر سی سی رہی ہے", "اک موج سی بہہ رہی ہے"),
        ]
    },
    {
        "poem_id": "sauda_001",
        "poet": "Sauda",
        "era": "18th century",
        "form": "ghazal",
        "source": "public_domain",
        "couplets": [
            ("باز آئے نہ رہے مرتا ہوں کیوں", "موت سے بھی بڑھ کے ہے فنا کا ڈر"),
            ("بزم میں خالی ہیں نالہ و فغاں کے سوا",
             "آئے ہے زخم دل میں ایسے جہاں کے"),
        ]
    },
    {
        "poem_id": "iqbal_001",
        "poet": "Allama Iqbal",
        "era": "20th century",
        "form": "nazm",
        "source": "public_domain",
        "couplets": [
            ("ستاروں سے آگے جہاں اور بھی ہیں", "ابھی عشق کے امتحاں اور بھی ہیں"),
            ("خودی کو کر بلند اتنا کہ ہر تقدیر سے پہلے",
             "خدا بندے سے خود پوچھے بتا تیری رضا کیا ہے"),
        ]
    },
    {
        "poem_id": "bulleh_001",
        "poet": "Bulleh Shah",
        "era": "18th century",
        "form": "kafi",
        "source": "public_domain",
        "couplets": [
            ("بول کہ لب آزاد ہیں تیرے", "بول زباں اب تک تیری ہے"),
            ("مٹی دی لو دا پہر آیا", "رات دی واری دا سہر آیا"),
            ("ساون دیاں راتاں تے گونج دے بول", "گھر دیواں دیاں مٹیاں ہون والیاں"),
        ]
    }
]

os.makedirs("data", exist_ok=True)

with open("data/raw_corpus.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["poem_id", "couplet_id", "line_id", "poet",
                    "era", "form", "line_text", "source", "line_norm", "label"])
    for poem in poems:
        for i, (line_a, line_b) in enumerate(poem["couplets"], start=1):
            line_a_norm = normalize_line(line_a)
            line_b_norm = normalize_line(line_b)
            writer.writerow([poem["poem_id"], i, "a", poem["poet"],
                             poem["era"], poem["form"], line_a, poem["source"], line_a_norm, 1])
            writer.writerow([poem["poem_id"], i, "b", poem["poet"],
                             poem["era"], poem["form"], line_b, poem["source"], line_b_norm, 1])


print("✅ data/raw_corpus.csv created.")
