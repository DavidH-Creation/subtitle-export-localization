# Graph Report - C:\Users\david\dev\subtitle-export-localization  (2026-04-08)

## Corpus Check
- Corpus is ~10,519 words - fits in a single context window. You may not need a graph.

## Summary
- 30 nodes · 36 edges · 5 communities detected
- Extraction: 69% EXTRACTED · 31% INFERRED · 0% AMBIGUOUS · INFERRED: 11 edges (avg confidence: 0.5)
- Token cost: 0 input · 0 output

## God Nodes (most connected - your core abstractions)
1. `process_file()` - 6 edges
2. `extract()` - 5 edges
3. `build_document()` - 4 edges
4. `extract_with_python_docx()` - 3 edges
5. `extract_with_zipfile()` - 3 edges
6. `_episode_from_id()` - 3 edges
7. `_parse_episode_num()` - 3 edges
8. `classify_line()` - 3 edges
9. `_merge_split_lines()` - 3 edges
10. `_extract_ep_num()` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "C: Users"
Cohesion: 0.29
Nodes (9): classify_line(), main(), _merge_split_lines(), _parse_episode_num(), process_file(), Merge split-dialogue lines where speaker and text are on separate lines., Process an entire script file. Returns (jsonl_records, stats)., Try to extract episode number from a title line. (+1 more)

### Community 1 - "C: Users"
Cohesion: 0.36
Nodes (7): extract(), extract_with_python_docx(), extract_with_zipfile(), main(), Extract paragraphs using python-docx (preferred)., Fallback extract paragraphs via zipfile + xml.etree., Extract paragraphs from a .docx file. Tries python-docx first, then zipfile.

### Community 2 - "C: Users"
Cohesion: 0.47
Nodes (5): build_document(), _episode_from_id(), main(), Extract episode label from record ID like EP01_001., Build a Word document from translated JSONL records.

### Community 3 - "C: Users"
Cohesion: 1.0
Nodes (2): _extract_ep_num(), main()

### Community 4 - "C: Users"
Cohesion: 1.0
Nodes (2): _extract_ep_num(), main()

## Knowledge Gaps
- **9 isolated node(s):** `Extract paragraphs using python-docx (preferred).`, `Fallback extract paragraphs via zipfile + xml.etree.`, `Extract paragraphs from a .docx file. Tries python-docx first, then zipfile.`, `Extract episode label from record ID like EP01_001.`, `Build a Word document from translated JSONL records.` (+4 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Are the 4 inferred relationships involving `process_file()` (e.g. with `_merge_split_lines()` and `_parse_episode_num()`) actually correct?**
  _`process_file()` has 4 INFERRED edges - model-reasoned connections that need verification._
- **Are the 3 inferred relationships involving `extract()` (e.g. with `extract_with_python_docx()` and `extract_with_zipfile()`) actually correct?**
  _`extract()` has 3 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `build_document()` (e.g. with `_episode_from_id()` and `main()`) actually correct?**
  _`build_document()` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Extract paragraphs using python-docx (preferred).`, `Fallback extract paragraphs via zipfile + xml.etree.`, `Extract paragraphs from a .docx file. Tries python-docx first, then zipfile.` to the rest of the system?**
  _9 weakly-connected nodes found - possible documentation gaps or missing edges._