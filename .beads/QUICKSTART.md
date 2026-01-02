# Beads Quick Start for Confit Project

## Installation

Run the installation script:
```bash
.beads/INSTALL_BEADS.sh
```

Or see `.beads/README.md` for manual installation options.

## Initialize Beads

```bash
# Initialize in the project root
bd init
```

## Import Tasks from TASKS.md

All tasks identified in the project review are documented in `TASKS.md`. You can create them in Beads:

```bash
# Example: Create the critical store.get() bug fix
bd create "Fix store.get() bug" -p 0
bd desc <task-id> "resolve_module_and_params() returns placeholder.full_key (string) instead of actual object at line 40 in src/confit/store.py"

# Create package exports fix
bd create "Fix package exports" -p 0

# Create README syntax fix
bd create "Fix README syntax errors" -p 0

# And so on for other tasks...
```

## Essential Commands

### View Tasks
```bash
bd ready          # Show tasks ready to work on
bd list           # List all tasks
bd show <id>      # Show task details
```

### Create Tasks
```bash
bd create "Task title" -p <priority>    # Create with priority (0=highest)
bd desc <id> "Description text"         # Add description
```

### Manage Dependencies
```bash
bd dep add <child> <parent>    # child depends on parent
bd dep rm <child> <parent>     # Remove dependency
bd deps <id>                   # Show task dependencies
```

### Update Tasks
```bash
bd start <id>      # Mark task as in progress
bd done <id>       # Mark task as complete
bd block <id>      # Mark task as blocked
```

## Workflow Example

1. **View ready tasks:**
   ```bash
   bd ready
   ```

2. **Start working on a task:**
   ```bash
   bd start bd-a1b2
   ```

3. **Complete the task:**
   ```bash
   bd done bd-a1b2
   ```

4. **See what's ready next:**
   ```bash
   bd ready
   ```

## Task Priority Guidelines

- **P0 (Priority 0):** Critical bugs that break functionality
- **P1 (Priority 1):** Important improvements, tests, documentation
- **P2 (Priority 2):** Nice-to-have fixes, minor improvements
- **P3 (Priority 3):** Future enhancements, low priority features

## Using with Git

Beads integrates with Git:
- Tasks are stored in `.beads/` directory as JSONL files
- Version controlled with your code
- Branches, merges, and commits work seamlessly
- Task state travels with your branches

## Stealth Mode

If working on a shared project and want private tasks:
```bash
bd init --stealth
```

This keeps task data local and prevents commits to the repository.

## Resources

- **GitHub:** https://github.com/steveyegge/beads
- **Project Tasks:** See `TASKS.md` for detailed task breakdown
- **Issues Found:** See the project review in git history
