#!/bin/bash
# Jeseci Smart Learning Companion - Virtual Environment Setup
# Author: Cavin Otieno
# Date: December 13, 2025

echo "🚀 Setting up Jeseci Smart Learning Companion Virtual Environment..."

# Create virtual environment
echo "📦 Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "⚡ Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "⬆️  Upgrading pip to latest version..."
pip install --upgrade pip

# Install Python dependencies
echo "📚 Installing Python dependencies..."
pip install -r requirements.txt

# Install JAC language specifically
echo "🔧 Installing JAC language runtime..."
pip install "jaclang>=0.9.3"

# Verify installations
echo "✅ Verifying installations..."
python --version
pip list | grep -E "(jaclang|fastapi|sqlalchemy)"

echo "🎉 Virtual environment setup complete!"
echo "💡 To activate the environment, run: source venv/bin/activate"
echo "🚀 To run the application: jac serve app.jac"
echo "🌐 To run the API server: uvicorn main:app --reload"