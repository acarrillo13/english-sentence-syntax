English Sentence Syntax Parser
Overview

This project implements a Pushdown Automaton (PDA) that parses English sentences based on formal grammar rules. The system breaks down sentences into syntactic components (noun phrases, verb phrases, etc.) and validates whether they conform to the defined grammar structure.
Key Components

    Grammar Rules: Defines how different parts of speech can be combined to form valid sentences

    PDA Implementation: Python class that processes input strings according to the grammar

    Visualization: LaTeX/TikZ diagram showing the PDA state machine

How It Works

The system uses context-free grammar rules to analyze sentence structure:

    Sentences are built from Noun Phrases (NP) and Verb Phrases (VP)

    Supports modifiers (adjectives, adverbs), conjunctions, and prepositional phrases

    Validates input against production rules using a stack-based approach

Files

    510 language-2.pdf: Project documentation explaining the grammar and approach

    languagesyntax.py: Python implementation of the PDA

    main.tex: LaTeX source for the PDA state diagram

Usage

    Run the Python script:
    bash

    python languagesyntax.py

    Enter a space-separated string of parts of speech (e.g., "det adj noun verb")

    The system will output whether the string is accepted and show the processing trace

Example valid input:

det adj noun verb

(Equivalent to sentences like "The big dog runs")
Grammar Highlights

Key production rules include:

    S → NP VP | S conj S | adv S

    NP → noun | det noun | det AdjP noun

    VP → verb | verb NP | VP conj VP

    AdjP → adj | adj AdjP

    PP → prep NP

Visualization

The main.tex file generates a diagram of the two-state PDA showing all transitions and production rules.
Limitations

    Works with parts of speech tags rather than actual words

    Some complex English sentence structures may not be covered

    No semantic analysis (only checks syntactic validity)

Potential Extensions

    Add lexicon mapping to actual words

    Implement more complex grammar rules

    Add error detection with suggestions

    Develop a sentence generator using the grammar

