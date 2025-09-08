W# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Architecture Overview

This repository implements Crockford Base32 ID generators for multiple platforms:

- **FME Integration**: `FME/PythonCaller.py` contains a `FeatureProcessor` class that extends `BaseTransformer` for use with FME Desktop/Server Python Caller transformers
- **PostgreSQL Function**: `Postgres/Postgres.sql` provides a PostgreSQL function for database-level ID generation

Both implementations use the same Crockford Base32 alphabet (`123456789ABCDEFGHJKMNPQRSTVWXYZ`) which excludes confusing characters (I, L, O, U, 0) for improved human readability.

## Key Implementation Details

### FME Python Caller
- Implements FME's `BaseTransformer` interface
- Enables bulk processing mode via `has_support_for()` method
- Adds generated IDs as `_cuid` attribute to features
- Default ID length is 12 characters (configurable in `__init__`)
- Outputs processed features to "PYOUTPUT" port

### PostgreSQL Function
- Function signature: `generate_crockford_id(size INT DEFAULT 12)`
- Can be used as column default value for automatic ID assignment
- Suitable for both new table creation and altering existing tables

## Usage Patterns

The FME transformer processes spatial/tabular data streams, while the PostgreSQL function generates IDs at the database level. Both ensure globally unique, human-readable identifiers suitable for entity identification across systems.