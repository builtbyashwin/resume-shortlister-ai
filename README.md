# 🧠 AI Resume Shortlisting System (ATS Simulator)

An intelligent resume ranking system that simulates how Applicant Tracking Systems (ATS) work in real companies. It uses Natural Language Processing (NLP) techniques to analyze resumes and rank them based on relevance to a job description.

---

## 🚀 Features

- 📄 Supports multiple resume formats (`.txt`, `.pdf`, `.docx`, `.odt`)
- 🧠 NLP-based ranking using TF-IDF + Cosine Similarity
- 🏆 Automatic candidate ranking based on job fit
- ⚙️ Fully offline and lightweight (CPU-friendly)
- 📂 Batch processing from local dataset folder
- 💡 Real-world ATS-style simulation

---

## 🏗️ Tech Stack

- Python
- scikit-learn
- NumPy
- PyPDF2
- python-docx
- odfpy

---

## 📁 Project Structure

resume-shortlister-ai/
│
├── app.py              # Main execution script
├── model.py            # ML ranking logic (TF-IDF + similarity)
├── file_reader.py     # Multi-format resume parser
│
└── data/
    ├── job.txt        # Job description
    ├── resume1.txt
    ├── resume2.docx
    ├── resume3.pdf
    ├── resume4.odt

---

## ⚙️ How It Works

1. Load job description from `data/job.txt`
2. Read all resumes from the `data/` folder
3. Extract text from different file formats
4. Convert text into TF-IDF vectors
5. Compute cosine similarity
6. Rank candidates based on relevance score

---

## ▶️ How to Run

Clone the repository:
git clone https://github.com/buildwithashwin/resume-shortlister-ai.git
cd resume-shortlister-ai

Install dependencies:
pip install scikit-learn numpy PyPDF2 python-docx odfpy

Run the project:
python3 app.py

---

## 💡 Sample Output

AI RESUME SHORTLISTING SYSTEM

Ranking Results:

Rank 1: resume1.txt | Score: 0.52  
Rank 2: resume4.odt | Score: 0.20  
Rank 3: resume2.docx | Score: 0.20  
Rank 4: resume3.pdf | Score: 0.02  

✔ Done processing resumes.

---

## 🔮 Future Improvements

- Skill extraction using NLP
- Explainable AI (why a resume ranked higher)
- Streamlit web interface
- PDF report generation
- Deployment as SaaS tool

---

## 👨‍💻 Author

Built by Ashwin  
