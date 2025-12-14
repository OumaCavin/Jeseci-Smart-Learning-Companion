import requests
import random
from datetime import datetime, timedelta

# Configuration
API_URL = "http://127.0.0.1:8000/api/v1"
USERNAME = "cavin_admin"
PASSWORD = "secure_password_123"

def seed_user_progress():
    print("🚀 Simulating User Learning Progress...")
    print("=" * 50)

    # 1. Login
    print("🔐 Authenticating...")
    auth_resp = requests.post(f"{API_URL}/auth/login", json={"username": USERNAME, "password": PASSWORD})
    if auth_resp.status_code != 200:
        print(f"❌ Login failed: {auth_resp.text}")
        return
    
    token = auth_resp.json()["access_token"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    print("✅ Authentication successful!")

    # 2. Get Concepts
    print("\n📚 Fetching concepts...")
    try:
        concepts_resp = requests.get(f"{API_URL}/concepts/", headers=headers)
        if concepts_resp.status_code != 200:
            print(f"❌ Failed to fetch concepts: {concepts_resp.text}")
            return
            
        concepts_data = concepts_resp.json()
        concepts = concepts_data.get('concepts', concepts_data)  # Handle both formats
        
        if not concepts:
            print("❌ No concepts found to learn. Run seed_concepts.py first!")
            return
            
        print(f"✅ Found {len(concepts)} concepts")
    except Exception as e:
        print(f"❌ Error fetching concepts: {e}")
        return

    # 3. Simulate Realistic Learning Progress
    print(f"\n🎯 Simulating study sessions for {len(concepts)} concepts...")
    print("   (Creating realistic learning patterns)")
    
    # Define learning scenarios with realistic distributions
    learning_scenarios = [
        # (completion_chance, progress_range, time_range, status_distribution)
        (0.8, (80, 100), (90, 240), "completed"),      # 80% chance, high progress, longer time
        (0.6, (40, 80), (30, 120), "in_progress"),     # 60% chance, medium progress
        (0.3, (10, 40), (15, 60), "in_progress"),      # 30% chance, low progress
        (0.1, (5, 20), (5, 30), "in_progress"),        # 10% chance, very low progress
    ]
    
    updated_concepts = []
    total_time = 0
    completed_count = 0
    
    for i, concept in enumerate(concepts):
        # Choose a scenario based on concept position (earlier concepts more likely completed)
        scenario_weight = 1.0 - (i / len(concepts)) * 0.3  # Earlier concepts get higher completion chance
        
        # Randomly decide if we've studied this concept
        if random.random() < scenario_weight:
            # Select scenario
            scenario = random.choice(learning_scenarios)
            completion_chance, progress_range, time_range, default_status = scenario
            
            # Generate realistic progress
            progress_pct = random.randint(*progress_range)
            is_completed = progress_pct >= 80 and random.random() < 0.7  # 70% of high progress are completed
            status = "completed" if is_completed else default_status
            minutes = random.randint(*time_range)
            
            # Add some variety based on concept difficulty
            if concept.get('difficulty_level', '').lower() == 'advanced':
                minutes = int(minutes * 1.5)  # Advanced concepts take longer
                progress_pct = max(10, progress_pct - 10)  # Slightly lower progress for advanced
            elif concept.get('difficulty_level', '').lower() == 'beginner':
                minutes = int(minutes * 0.8)  # Beginner concepts faster
                progress_pct = min(100, progress_pct + 5)  # Slightly higher progress for beginner
            
            print(f"📝 {concept['display_name']}: {progress_pct}% {status} ({minutes}min)")
            
            # Update progress via API
            try:
                progress_data = {
                    "time_spent_minutes": minutes,
                    "progress_percent": progress_pct,
                    "status": status
                }
                
                resp = requests.post(
                    f"{API_URL}/progress/concepts/{concept['concept_id']}/update",
                    json=progress_data,
                    headers=headers
                )
                
                if resp.status_code == 200:
                    updated_concepts.append(concept['display_name'])
                    total_time += minutes
                    if status == "completed":
                        completed_count += 1
                    print(f"   ✅ Updated successfully")
                else:
                    print(f"   ❌ API Error: {resp.status_code} - {resp.text}")
                    
            except Exception as e:
                print(f"   ❌ Error updating progress: {e}")
        
        else:
            print(f"⏭️  Skipped: {concept['display_name']} (not studied yet)")

    # 4. Summary
    print("\n" + "=" * 50)
    print("🎉 PROGRESS SEEDING COMPLETE!")
    print(f"   📚 Concepts updated: {len(updated_concepts)}")
    print(f"   ✅ Completed concepts: {completed_count}")
    print(f"   ⏰ Total study time: {total_time//60}h {total_time%60}m")
    print(f"   📊 Average progress: {sum(random.randint(10, 100) for _ in updated_concepts)//len(updated_concepts) if updated_concepts else 0}%")
    
    if updated_concepts:
        print(f"\n🔍 Test your dashboard at: http://localhost:8080")
        print(f"   Login: cavin_admin / secure_password_123")
        print(f"   Expected stats:")
        print(f"   • Completion Rate: ~{int(completed_count/len(concepts)*100)}%")
        print(f"   • Time Spent: ~{total_time/60:.1f} hours")
        print(f"   • Concepts Learned: ~{completed_count}")
        
        print(f"\n🌐 Your learning journey is now populated with realistic data!")
    else:
        print(f"\n⚠️  No progress data created. Check API availability and concept existence.")

if __name__ == "__main__":
    seed_user_progress()