# Beads Task Management

This directory contains task management data for the confit project using Beads.

## Installation

Since Beads couldn't be installed automatically, you can install it manually:

### Option 1: NPM (Recommended)
```bash
npm install -g @beads/bd
```

### Option 2: Shell Script
```bash
curl -fsSL https://raw.githubusercontent.com/steveyegge/beads/main/scripts/install.sh | bash
```

### Option 3: Homebrew (macOS)
```bash
brew install steveyegge/beads/bd
```

### Option 4: Go
```bash
go install github.com/steveyegge/beads/cmd/bd@latest
```

## Initialize Beads

After installation, initialize Beads in the confit project:

```bash
bd init
```

## Quick Start

```bash
# View ready tasks
bd ready

# Create a new task
bd create "Fix store.get() bug" -p 0

# Show task details
bd show <task-id>

# Add dependencies
bd dep add <child-id> <parent-id>
```

## Resources

- GitHub: https://github.com/steveyegge/beads
- Documentation: See repository README
