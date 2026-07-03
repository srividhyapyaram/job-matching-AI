import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load job dataset
jobs = pd.read_csv("jobs.csv")

# Take user input
user_skills = input("Enter your skills (space separated): ").lower()

# Convert user skills to set
user_skill_set = set(user_skills.split())

# Prepare data for similarity
all_text = list(jobs["skills"]) + [user_skills]

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(all_text)

similarity = cosine_similarity(vectors[-1], vectors[:-1])
best_match_index = similarity.argmax()

# Get matched job
matched_job = jobs.iloc[best_match_index]
job_title = matched_job["job_title"]
job_skills = set(matched_job["skills"].split())

# Skill gap analysis
missing_skills = job_skills - user_skill_set

print("\n✅ Best Matched Job:", job_title)
print("📌 Required Skills:", ", ".join(job_skills))
print("👤 Your Skills:", ", ".join(user_skill_set))

if missing_skills:
    print("🚀 Recommended Skills to Learn:", ", ".join(missing_skills))
else:
    print("🎉 You have all required skills for this job!")
