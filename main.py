def generate_contextcraft_content(seed_idea):
    """
    Simulates ContextCraft multi-engine content generation pipeline.
    Transforms a single seed idea into X, LinkedIn, and Shorts formats.
    """
    outputs = {
        "x_thread": f"🧵 1/3 Here is a core insight on: {seed_idea}\n2/3 Breakdown of the idea...\n3/3 Wrap up and call to action.",
        "linkedin_post": f"💡 Transforming how we think about: {seed_idea}\n\nKey takeaways:\n• Point 1\n• Point 2\n\nWhat are your thoughts on this?",
        "youtube_shorts": f"[00:00-00:15] Hook: Did you know this about {seed_idea}?\n[00:15-00:45] Main Explanation\n[00:45-00:60] Call to action / Outro"
    }
    return outputs

if __name__ == "__main__":
    test_idea = "AI Driven Content Compilation"
    result = generate_contextcraft_content(test_idea)
    print("--- ContextCraft Pipeline Output ---")
    for platform, content in result.items():
        print(f"\n[{platform.upper()}]\n{content}")
