import os
from model import rank_resumes
from file_reader import read_file

DATA_DIR = "data"


def load_job():
    with open(os.path.join(DATA_DIR, "job.txt"), "r", encoding="utf-8") as f:
        return f.read()


def load_resumes():
    resumes = []
    names = []

    for file in os.listdir(DATA_DIR):
        if file == "job.txt":
            continue

        path = os.path.join(DATA_DIR, file)

        with open(path, "rb") as f:
            text = read_file(f, file)

        resumes.append(text)
        names.append(file)

    return resumes, names


def main():
    job = load_job()
    resumes, names = load_resumes()

    ranked = rank_resumes(job, resumes)

    print("\nAI RESUME SHORTLISTING SYSTEM\n")
    print("Ranking Results:\n")

    for rank, (idx, score) in enumerate(ranked, 1):
        print(f"Rank {rank}: {names[idx]} | Score: {score:.2f}")

    print("\n✔ Done processing resumes.")


if __name__ == "__main__":
    main()
