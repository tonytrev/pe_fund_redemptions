"""
Knowledge Base Configuration
Easy place to manage knowledge base settings
"""

# Knowledge Base ID - Update this with your actual knowledge base ID
KNOWLEDGE_BASE_ID = "W1Q58MF2A7"

# Retrieval Configuration
RETRIEVAL_CONFIG = {
    "vectorSearchConfiguration": {
        "numberOfResults": 10,
        "overrideSearchType": "HYBRID"  # Options: HYBRID, SEMANTIC, or omit for default
    }
}

# You can also set this via environment variable
import os
KNOWLEDGE_BASE_ID = os.environ.get('KNOWLEDGE_BASE_ID', KNOWLEDGE_BASE_ID)
