import re

# Sample input text (simulating API response)
sample_text = """
Contact us at user@example.com or firstname.lastname@company.co.uk.
Visit https://www.example.com or https://subdomain.example.org/page.
Call (123) 456-7890 or 123-456-7890.
Follow #example and #ThisIsAHashtag on social media.
Pay with 1234 5678 9012 3456 or 1234-5678-9012-3456.
Invalid email: user@.com, invalid phone: 123-45-678, invalid card: 1234-5678-9012.
"""

# Regex patterns
patterns = {
    "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "url": r"https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[a-zA-Z0-9._-]*)?",
    "phone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "hashtag": r"#[a-zA-Z0-9_]+",
    "credit_card": r"\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}"
}

# Function to extract data
def extract_data(text):
    results = {}
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text)
        results[key] = matches if matches else ["None found"]
    return results

# Run extraction and print results
if __name__ == "__main__":
    results = extract_data(sample_text)
    for key, matches in results.items():
        print(f"{key.replace('_', ' ').capitalize()}: {matches}")