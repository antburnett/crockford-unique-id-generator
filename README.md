# Crockford Unique ID Generator

A collection of Crockford Base32 ID generators for multiple platforms, providing short, human-readable unique identifiers.

## Overview

This repository contains implementations of Crockford Base32 ID generators for:

- **FME Desktop/Server** - Python Caller transformer for spatial data processing workflows
- **PostgreSQL** - Database function for server-side ID generation

Both implementations use the Crockford Base32 alphabet (`123456789ABCDEFGHJKMNPQRSTVWXYZ`) which excludes confusing characters (I, L, O, U, 0) for improved readability and reduced transcription errors.

## Features

- **Human-readable**: Excludes ambiguous characters to prevent confusion
- **Configurable length**: Default 12 characters (customizable)
- **Platform-specific**: Optimized for each environment's best practices
- **Performance-oriented**: FME version supports bulk processing mode

## Combination Examples

- **4 characters**: 32^4 = 1,048,576 combinations
- **12 characters**: 32^12 = 1.23 × 10^18 combinations
- **32 characters**: 32^32 = 1.46 × 10^48 combinations

## Usage

### FME Python Caller

1. Add `FME/PythonCaller.py` to your FME workspace as a Python Caller transformer
2. Connect your feature stream to the transformer input
3. Generated IDs will be added as `_cuid` attribute to each feature
4. Access processed features from the "PYOUTPUT" port

### PostgreSQL Function

```sql
-- Create the function
\i Postgres/Postgres.sql

-- Use as default value for new tables
CREATE TABLE your_table (
    id TEXT DEFAULT fn_generate_crockford_id() PRIMARY KEY,
    -- your other columns
);

-- Or add to existing tables
ALTER TABLE existing_table 
ADD COLUMN id TEXT DEFAULT fn_generate_crockford_id() UNIQUE;
```

## Examples

Generated IDs look like: `7N9WJ2K8PQR3`, `M4X6Y2H9BF7S`, `K3P8R5W9N2M7`

## Requirements

- **FME**: FME Desktop 2019.0+ or FME Server
- **PostgreSQL**: PostgreSQL 9.1+ (requires plpgsql)