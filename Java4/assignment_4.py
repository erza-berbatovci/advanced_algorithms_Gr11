import re

def moderate_posts(blacklist, posts):
    # Convert blacklist to lowercase and store in a set for fast lookup
    blacklist_set = set(phrase.lower() for phrase in blacklist)
    
    results = []
    
    for i, post in enumerate(posts, start=1):
        # Convert to lowercase
        lower_post = post.lower()
        
        # Replace underscores and punctuation with spaces
        normalized_post = re.sub(r'[^a-z0-9\s]', ' ', lower_post)
        normalized_post = re.sub(r'\s+', ' ', normalized_post).strip()
        
        found_phrases = []
        for phrase in blacklist_set:
            # Normalize phrase too
            normalized_phrase = re.sub(r'[^a-z0-9\s]', ' ', phrase)
            normalized_phrase = re.sub(r'\s+', ' ', normalized_phrase).strip()
            
            if normalized_phrase in normalized_post:
                found_phrases.append(phrase)
        
        # Format output
        if found_phrases:
            formatted_phrases = "[" + ", ".join(f'"{p}"' for p in found_phrases) + "]"
            results.append(f"Post {i}: FLAGGED - Contains: {formatted_phrases}")
        else:
            results.append(f"Post {i}: CLEAN")
    
    return results



blacklisted_phrases = [
    "hate speech", "buy followers", "click here now", "banned content", "illegal drugs"
]

posts_to_check = [
    "Check out my new recipe for chocolate cake!",
    "CLICK HERE NOW for amazing deals!!!",
    "I don't agree with that hate speech in the comments",
    "Buy_Followers cheap and fast delivery",
    "This is a normal post about my day"
]

results = moderate_posts(blacklisted_phrases, posts_to_check)

# Display results
for res in results:
    print(res)
