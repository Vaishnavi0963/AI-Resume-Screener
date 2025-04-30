from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read the job description and resume text
with open('job_description.txt', 'r') as f:
    job_description = f.read()

with open('sample_resume.txt', 'r') as f:
    resume = f.read()

# Combine texts for vectorization
texts = [job_description, resume]

# Convert text to vectors using TF-IDF
vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(texts)

# Calculate cosine similarity
similarity_score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0] * 100

# Print the match percentage
print(f"Resume Match Score: {similarity_score:.2f}%")

# Basic result interpretation
if similarity_score > 60:
    print("Result: Strong Match – Resume is suitable for this job.")
elif similarity_score > 40:
    print("Result: Moderate Match – Resume might be improved.")
else:
    print("Result: Low Match – Resume does not fit the job description well.")