#!/bin/bash
# Script to install Beads task management CLI

echo "🔧 Installing Beads (bd) for task management..."

# Check if bd is already installed
if command -v bd &> /dev/null; then
    echo "✅ Beads is already installed!"
    bd --version
    exit 0
fi

# Try npm first (most reliable cross-platform)
if command -v npm &> /dev/null; then
    echo "📦 Installing via npm..."
    npm install -g @beads/bd
    if [ $? -eq 0 ]; then
        echo "✅ Beads installed successfully via npm!"
        bd --version
        exit 0
    fi
fi

# Try brew on macOS
if [[ "$OSTYPE" == "darwin"* ]] && command -v brew &> /dev/null; then
    echo "🍺 Installing via Homebrew..."
    brew install steveyegge/beads/bd
    if [ $? -eq 0 ]; then
        echo "✅ Beads installed successfully via Homebrew!"
        bd --version
        exit 0
    fi
fi

# Try go install
if command -v go &> /dev/null; then
    echo "🔨 Installing via Go..."
    go install github.com/steveyegge/beads/cmd/bd@latest
    if [ $? -eq 0 ]; then
        echo "✅ Beads installed successfully via Go!"
        # Add GOPATH/bin to PATH hint
        echo "Note: Make sure \$GOPATH/bin is in your PATH"
        echo "Add this to your shell config: export PATH=\$PATH:\$(go env GOPATH)/bin"
        exit 0
    fi
fi

# Try shell script
echo "📥 Trying installation script..."
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash

if command -v bd &> /dev/null; then
    echo "✅ Beads installed successfully!"
    bd --version
else
    echo "❌ Automatic installation failed."
    echo ""
    echo "Please install manually:"
    echo "1. Visit: https://github.com/steveyegge/beads/releases/latest"
    echo "2. Download the appropriate binary for your platform"
    echo "3. Extract and move 'bd' to a directory in your PATH"
    exit 1
fi
