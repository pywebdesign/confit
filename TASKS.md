# Confit Project Tasks

This file tracks all tasks needed to improve the confit project.
Once Beads is installed, these can be imported into the task management system.

## Critical Priority (P0) - Must Fix Immediately

### 1. Fix store.get() Bug
**ID:** critical-store-get
**Status:** 🔴 Blocked
**File:** `src/confit/store.py:82-83`
**Issue:** `resolve_module_and_params()` returns `placeholder.full_key` (string) instead of the actual object, overwriting the resolved object in the store.
**Impact:** Library is completely broken - users cannot retrieve created objects.
**Fix:** Change line 40 to return the object instead of the key, or don't overwrite at line 82.

### 2. Fix Package Exports
**ID:** critical-init-exports
**Status:** 🔴 Blocked
**Dependencies:** None
**Files:**
- `src/confit/__init__.py` - Currently empty
- `src/confit/utils/__init__.py` - Missing

**Issue:** Users can't do `import confit` or `from confit import store` as shown in README.
**Fix:** Add proper exports to `__init__.py` files.

### 3. Fix README Syntax Errors
**ID:** critical-readme-syntax
**Status:** 🟡 Ready
**File:** `README.md`
**Issues:**
- Line 19: `type: MySimpleObject:` has extra colon
- Line 39: `config.store.get()` should be `confit.store.get()`
- Missing YAML code fence syntax (```yaml)
- Grammar and incomplete sentences

### 4. Add Example YAML Files
**ID:** critical-example-yaml
**Status:** 🟡 Ready
**Dependencies:** None
**Issue:** README shows YAML examples but no actual files exist for users to reference.
**Fix:** Create `examples/` directory with working YAML configuration files.

## High Priority (P1) - Should Fix Soon

### 5. Fix Duplicate Test
**ID:** test-duplicate
**Status:** 🟡 Ready
**File:** `tests/object_creation_test.py:70-94`
**Issue:** `test_deep_with_interface` defined twice.

### 6. Add Comprehensive Test Coverage
**ID:** test-coverage
**Status:** 🟡 Ready
**Dependencies:** [critical-store-get]
**Missing Tests:**
- File not found errors (invalid YAML path)
- Malformed YAML syntax
- Cyclic dependencies
- Missing class/module imports
- Invalid configuration keys
- Empty configurations
- Type mismatches
- `_id` references to non-existent objects

### 7. Add Integration Tests
**ID:** test-integration
**Status:** 🟡 Ready
**Dependencies:** [critical-example-yaml]
**Issue:** Tests only use programmatic dicts, never actual YAML files.
**Fix:** Add tests that load real YAML files like users would.

### 8. Improve Error Handling
**ID:** error-handling
**Status:** 🟡 Ready
**Files:** `src/confit/store.py`, `src/confit/dependencies.py`
**Issues:**
- Line 77: KeyError just prints, doesn't raise
- No validation that `_id` references exist
- Circular dependency errors lack detail
- No helpful messages for common mistakes

### 9. Add Configuration Validation
**ID:** config-validation
**Status:** 🟡 Ready
**Dependencies:** [error-handling]
**Need:**
- Schema validation for config structure
- Type checking before instantiation
- Helpful error messages for common mistakes

### 10. Add LICENSE File
**ID:** add-license
**Status:** 🟡 Ready
**Issue:** No LICENSE file - unclear legal status.
**Fix:** Add appropriate open source license (MIT, Apache 2.0, etc.).

### 11. Add Type Hints
**ID:** type-hints
**Status:** 🟡 Ready
**Files:** `src/confit/store.py`, `src/confit/dependencies.py`, `src/config_reader.py`
**Issue:** Only `import_utils.py` has comprehensive type hints.
**Fix:** Add type hints to all functions and classes.

### 12. Add Docstrings
**ID:** docstrings
**Status:** 🟡 Ready
**Issue:** Only one function has docstrings - all others undocumented.
**Fix:** Add comprehensive docstrings following Google or NumPy style.

## Medium Priority (P2) - Nice to Have

### 13. Fix Package Name in setup.py
**ID:** setup-package-name
**Status:** 🟡 Ready
**File:** `setup.py:4`
**Issue:** Has placeholder `your_project_name` instead of `confit`.

### 14. Remove Duplicate src/confit.py
**ID:** cleanup-duplicate-file
**Status:** 🟡 Ready
**File:** `src/confit.py`
**Issue:** Empty file at src root alongside src/confit/ package - confusing.

### 15. Add CONTRIBUTING.md
**ID:** add-contributing
**Status:** 🟡 Ready
**Dependencies:** [add-license]

### 16. Add CHANGELOG.md
**ID:** add-changelog
**Status:** 🟡 Ready

### 17. Setup Development Tools
**ID:** dev-tools
**Status:** 🟡 Ready
**Need:**
- mypy configuration
- Linter config (black, ruff, or pylint)
- pre-commit hooks
- .editorconfig

### 18. Add CI/CD
**ID:** ci-cd
**Status:** 🟡 Ready
**Dependencies:** [test-coverage, dev-tools]
**Need:** GitHub Actions workflow for:
- Running tests
- Linting
- Type checking
- Coverage reporting

### 19. Create Examples Directory
**ID:** examples-dir
**Status:** 🟡 Ready
**Dependencies:** [critical-store-get, critical-example-yaml]
**Examples needed:**
- Trading system (mentioned in README)
- Microservices configuration
- Database connection pooling
- Multi-environment setup

### 20. Pin Dependencies
**ID:** pin-dependencies
**Status:** 🟡 Ready
**File:** `pyproject.toml`
**Issue:** Uses `pyyaml>=6.0.2` without upper bound.
**Fix:** Consider version ranges for stability.

## Low Priority (P3) - Future Enhancements

### 21. CLI Tool
**ID:** feature-cli
**Status:** 💡 Future
**Purpose:** Command-line tool to:
- Validate configs
- Inspect object graph
- Debug dependency issues

### 22. Advanced Features
**ID:** feature-advanced
**Status:** 💡 Future
**Features:**
- Environment variable substitution
- Config file merging (dev.yaml + prod.yaml)
- Factory function support (not just constructors)
- Lazy loading/initialization
- Lifecycle management (cleanup, context managers)

### 23. Documentation Website
**ID:** docs-website
**Status:** 💡 Future
**Dependencies:** [docstrings, examples-dir]
**Tools:** Sphinx, MkDocs, or similar

### 24. PyPI Publication
**ID:** pypi-publish
**Status:** 💡 Future
**Dependencies:** [add-license, add-changelog, test-coverage]
**Need:**
- Wheel building config
- Versioning strategy
- Release workflow

### 25. Dependency Graph Visualization
**ID:** feature-viz
**Status:** 💡 Future
**Purpose:** Tool to visualize dependency graph for debugging.

## Task Legend

- 🔴 Blocked - Cannot proceed until dependencies resolved
- 🟡 Ready - Can be worked on now
- 🔵 In Progress - Currently being worked on
- ✅ Completed - Done
- 💡 Future - Lower priority enhancement
