# 📄 PDF Merger using `pypdf`

A simple Python script to **merge multiple PDF files** into one using the `pypdf` library. Perfect for small tasks like combining reports, notes, or documents. ⚡

---

## 📁 Project Structure

```
📦 PDF-Merger/
├── main.py            # 🧠 Main script to merge PDFs
├── pdf1.pdf           # 📄 Sample PDF 1
├── pdf2.pdf           # 📄 Sample PDF 2
├── pdf3.pdf           # 📄 Sample PDF 3
├── merged-pdf.pdf     # ✅ Output: Merged PDF file
```

---

## 🚀 How It Works

🔹 Prompts you to enter how many PDFs to merge  
🔹 Takes file names (like `pdf1.pdf`, `pdf2.pdf`, etc.)  
🔹 Merges them in the order entered  
🔹 Saves the result as `merged-pdf.pdf`

---

## 🛠️ Requirements

- Python 3.x  
- Install `pypdf`:

```bash
pip install pypdf
```

---

## ▶️ How to Run

Run the script from your terminal:

```bash
python main.py
```

Follow the prompts:

```
How many PDFs you want to merge? 3
Enter the name of PDF 1 : pdf1.pdf
Enter the name of PDF 2 : pdf2.pdf
Enter the name of PDF 3 : pdf3.pdf
```

You’ll get a new file named `merged-pdf.pdf` in the same folder. ✅

---

## 💡 Notes

- Make sure all PDFs you want to merge are in the **same folder** as `main.py`.
- Output will always overwrite `merged-pdf.pdf` if it already exists.
