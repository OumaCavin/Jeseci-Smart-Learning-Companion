#!/usr/bin/env python3
"""
Create Admin User Script for Jeseci Smart Learning Companion
This script creates a default admin user for the platform
"""

import os
import sys
import hashlib
from datetime import datetime
from sqlalchemy.orm import Session
from config.database import SessionLocal
from database.models.sqlite_models import User

def create_admin_user():
    """Create a default admin user for the platform"""
    db = SessionLocal()
    
    try:
        print("🚀 Creating Admin User for Jeseci Smart Learning Companion...")
        
        # Default admin credentials
        admin_email = "admin@jeseci.com"
        admin_password = "admin123"
        admin_username = "admin"
        admin_first_name = "Admin"
        admin_last_name = "User"
        
        # Check if admin already exists
        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if existing_admin:
            print(f"⚠️  Admin user already exists: {admin_email}")
            print("📧 Email:", admin_email)
            print("🔑 Password:", admin_password)
            return existing_admin
        
        # Create admin user with profile information
        admin_user = User(
            email=admin_email,
            username=admin_username,
            password_hash=hashlib.sha256(admin_password.encode()).hexdigest(),
            first_name=admin_first_name,
            last_name=admin_last_name,
            bio="System Administrator",
            preferred_language="en",
            is_verified=True,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.add(admin_user)
        db.flush()  # Get the user ID
        db.commit()
        
        print("✅ Admin user created successfully!")
        print("📧 Email:", admin_email)
        print("🔑 Password:", admin_password)
        print("👤 Username:", admin_username)
        print("🆔 User ID:", admin_user.user_id)
        print("👤 Full Name:", f"{admin_first_name} {admin_last_name}")
        
        return admin_user
        
    except Exception as e:
        print(f"❌ Error creating admin user: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def create_additional_admin():
    """Create an additional admin user with custom credentials"""
    db = SessionLocal()
    
    try:
        print("\n🔧 Creating Additional Admin User...")
        
        # Custom admin credentials
        admin_email = input("Enter admin email (default: admin2@jeseci.com): ").strip() or "admin2@jeseci.com"
        admin_password = input("Enter admin password (default: AdminPass123!): ").strip() or "AdminPass123!"
        admin_username = input("Enter admin username (default: admin2): ").strip() or "admin2"
        admin_first_name = input("Enter first name (default: Admin): ").strip() or "Admin"
        admin_last_name = input("Enter last name (default: Two): ").strip() or "Two"
        
        # Check if user already exists
        existing_user = db.query(User).filter(
            (User.email == admin_email) | (User.username == admin_username)
        ).first()
        
        if existing_user:
            print(f"⚠️  User already exists: {admin_email} / {admin_username}")
            return existing_user
        
        # Create user with profile information
        user = User(
            email=admin_email,
            username=admin_username,
            password_hash=hashlib.sha256(admin_password.encode()).hexdigest(),
            first_name=admin_first_name,
            last_name=admin_last_name,
            bio="System Administrator",
            preferred_language="en",
            is_verified=True,
            is_active=True,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        
        db.add(user)
        db.flush()
        db.commit()
        
        print("✅ Additional admin user created successfully!")
        print("📧 Email:", admin_email)
        print("🔑 Password:", admin_password)
        print("👤 Username:", admin_username)
        print("🆔 User ID:", user.user_id)
        print("👤 Full Name:", f"{admin_first_name} {admin_last_name}")
        
        return user
        
    except Exception as e:
        print(f"❌ Error creating additional admin: {e}")
        db.rollback()
        raise
    finally:
        db.close()

def list_admin_users():
    """List all admin users in the system"""
    db = SessionLocal()
    
    try:
        print("\n👥 Current Admin Users:")
        print("=" * 50)
        
        # Query admin users by email or username pattern
        admin_users = db.query(User).filter(
            (User.email.like('%admin%')) | 
            (User.username.like('%admin%')) |
            (User.bio.like('%Administrator%'))
        ).all()
        
        if not admin_users:
            print("No admin users found.")
            return
        
        for user in admin_users:
            full_name = f"{user.first_name or ''} {user.last_name or ''}".strip() or "Unknown"
            
            print(f"🆔 ID: {user.user_id}")
            print(f"👤 Name: {full_name}")
            print(f"📧 Email: {user.email}")
            print(f"📱 Username: {user.username}")
            print(f"✅ Active: {'Yes' if user.is_active else 'No'}")
            print(f"🔐 Verified: {'Yes' if user.is_verified else 'No'}")
            print(f"📅 Created: {user.created_at}")
            if user.bio:
                print(f"📝 Bio: {user.bio}")
            print("-" * 30)
            
    except Exception as e:
        print(f"❌ Error listing admin users: {e}")
    finally:
        db.close()

def main():
    """Main function"""
    print("🎓 Jeseci Smart Learning Companion - Admin User Creation")
    print("=" * 55)
    
    while True:
        print("\nChoose an option:")
        print("1. Create default admin user")
        print("2. Create additional admin user")
        print("3. List all admin users")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            create_admin_user()
        elif choice == "2":
            create_additional_admin()
        elif choice == "3":
            list_admin_users()
        elif choice == "4":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()