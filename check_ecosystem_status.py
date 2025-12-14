#!/usr/bin/env python3
"""
Database Status Verification Script
Quick check to see if your Jeseci ecosystem is properly seeded
"""

import requests
import sys
from datetime import datetime

def check_status():
    """Check the status of all ecosystem components"""
    print("🔍 JESECI ECOSYSTEM STATUS CHECK")
    print("=" * 50)
    print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test backend connectivity
    print("\n1️⃣  Backend Health Check")
    try:
        response = requests.get("http://127.0.0.1:8000/health", timeout=5)
        if response.status_code == 200:
            print("   ✅ Backend is running and healthy")
        else:
            print(f"   ⚠️  Backend returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException:
        print("   ❌ Backend is not accessible")
        print("   💡 Start with: uvicorn main:app --reload --host 0.0.0.0 --port 8000")
        return False
    
    # Test authentication
    print("\n2️⃣  Authentication Test")
    try:
        auth_resp = requests.post("http://127.0.0.1:8000/api/v1/auth/login", 
                                 json={"username": "cavin_admin", "password": "secure_password_123"})
        if auth_resp.status_code == 200:
            token = auth_resp.json()["access_token"]
            print("   ✅ Authentication working")
            headers = {"Authorization": f"Bearer {token}"}
        else:
            print(f"   ❌ Authentication failed: {auth_resp.status_code}")
            return False
    except Exception as e:
        print(f"   ❌ Authentication error: {e}")
        return False
    
    # Check concepts
    print("\n3️⃣  Knowledge Base Status")
    try:
        concepts_resp = requests.get("http://127.0.0.1:8000/api/v1/concepts/", headers=headers)
        if concepts_resp.status_code == 200:
            concepts_data = concepts_resp.json()
            concepts = concepts_data.get('concepts', concepts_data)
            print(f"   ✅ {len(concepts)} concepts available")
            
            if concepts:
                print("   📚 Sample concepts:")
                for concept in concepts[:3]:
                    print(f"      • {concept['display_name']} ({concept['difficulty_level']})")
                if len(concepts) > 3:
                    print(f"      ... and {len(concepts) - 3} more")
            else:
                print("   ⚠️  No concepts found - run seed_concepts.py")
        else:
            print(f"   ❌ Cannot fetch concepts: {concepts_resp.status_code}")
    except Exception as e:
        print(f"   ❌ Concepts check failed: {e}")
    
    # Check progress tracking
    print("\n4️⃣  Progress Tracking Status")
    try:
        progress_resp = requests.get("http://127.0.0.1:8000/api/v1/progress/", headers=headers)
        if progress_resp.status_code == 200:
            progress_data = progress_resp.json()
            stats = progress_data.get('overall_stats', {})
            
            concepts_learned = stats.get('total_concepts_learned', 0)
            time_spent = stats.get('total_time_spent', 0)
            completion_rate = stats.get('completion_rate', 0)
            
            print(f"   ✅ Progress tracking active")
            print(f"   📊 Statistics:")
            print(f"      • Concepts learned: {concepts_learned}")
            print(f"      • Time spent: {time_spent} hours")
            print(f"      • Completion rate: {completion_rate}%")
            print(f"      • Learning streak: {stats.get('learning_streak', 0)} days")
            
            if concepts_learned == 0:
                print("   💡 No progress data - run seed_progress.py for demo data")
        else:
            print(f"   ❌ Progress endpoint error: {progress_resp.status_code}")
    except Exception as e:
        print(f"   ❌ Progress check failed: {e}")
    
    # Check learning paths
    print("\n5️⃣  Learning Paths Status")
    try:
        paths_resp = requests.get("http://127.0.0.1:8000/api/v1/learning-paths/", headers=headers)
        if paths_resp.status_code == 200:
            paths = paths_resp.json()
            print(f"   ✅ {len(paths)} learning paths generated")
            
            if paths:
                print("   🛤️  Sample paths:")
                for path in paths[:2]:
                    progress = path.get('progress', 0)
                    print(f"      • {path['title']} ({path['difficulty']}) - {progress}% complete")
                if len(paths) > 2:
                    print(f"      ... and {len(paths) - 2} more")
        else:
            print(f"   ❌ Learning paths error: {paths_resp.status_code}")
    except Exception as e:
        print(f"   ❌ Learning paths check failed: {e}")
    
    # Overall status
    print("\n6️⃣  Overall Ecosystem Status")
    try:
        # Quick API health check
        root_resp = requests.get("http://127.0.0.1:8000/")
        if root_resp.status_code == 200:
            print("   ✅ API root endpoint working")
        
        # Check if we have data
        has_concepts = len(concepts) > 0 if 'concepts' in locals() else False
        has_progress = stats.get('total_concepts_learned', 0) > 0 if 'stats' in locals() else False
        
        if has_concepts and has_progress:
            print("   🎉 Ecosystem is fully operational!")
            print("   🌐 Frontend: http://localhost:8080")
            print("   👤 Login: cavin_admin / secure_password_123")
        elif has_concepts:
            print("   ⚠️  Concepts available but no progress data")
            print("   💡 Run seed_progress.py to populate dashboard")
        else:
            print("   ❌ Knowledge base is empty")
            print("   💡 Run seed_complete_ecosystem.py to populate everything")
            
    except Exception as e:
        print(f"   ❌ Status check failed: {e}")
    
    print("\n" + "=" * 50)
    print("📋 Quick Commands:")
    print("   • Populate everything: python seed_complete_ecosystem.py")
    print("   • Just concepts: python seed_concepts.py")
    print("   • Just relationships: python seed_relationships.py") 
    print("   • Just progress: python seed_progress.py")
    print("   • Test API: curl http://127.0.0.1:8000/health")

if __name__ == "__main__":
    check_status()