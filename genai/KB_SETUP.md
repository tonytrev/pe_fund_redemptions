# Knowledge Base Setup Guide

## Quick Setup

1. **Get your Knowledge Base ID** from the AWS Bedrock console
2. **Update the configuration** in `kb_config.py`:
   ```python
   KNOWLEDGE_BASE_ID = "YOUR_ACTUAL_KB_ID_HERE"
   ```
3. **Or set environment variable**:
   ```bash
   export KNOWLEDGE_BASE_ID="your-kb-id-here"
   ```

## Knowledge Base Tool Features

### Tool: `knowledge_base___retrieve_documents`

**Purpose**: Search across all fund documents using semantic/hybrid search

**Parameters**:
- `query` (required): Search query (e.g., "redemption fees for ClassA investors")
- `max_results` (optional): Number of results (default: 10, max: 20)

**Example Usage**:
```python
knowledge_base___retrieve_documents(
    query="What are the holding period requirements for different investor classes?",
    max_results=5
)
```

### Response Format

The tool returns formatted results with:
- **Relevance Score**: How well the content matches your query (0.0 to 1.0)
- **Source**: S3 location of the document
- **Content**: The relevant text excerpt

### Configuration Options

In `kb_config.py` you can adjust:

```python
RETRIEVAL_CONFIG = {
    "vectorSearchConfiguration": {
        "numberOfResults": 10,
        "overrideSearchType": "HYBRID"  # HYBRID, SEMANTIC, or omit
    }
}
```

**Search Types**:
- `HYBRID`: Combines semantic and keyword search (recommended)
- `SEMANTIC`: Pure vector/semantic search
- Omit for default behavior

## Required AWS Permissions

Your execution role needs:
```json
{
    "Effect": "Allow",
    "Action": [
        "bedrock-agent-runtime:Retrieve"
    ],
    "Resource": [
        "arn:aws:bedrock:us-east-1:*:knowledge-base/YOUR_KB_ID"
    ]
}
```

## Usage Tips

1. **Use for cross-document searches**: When you need to find information that might be in multiple fund documents
2. **Combine with specific tools**: Use knowledge base for discovery, then specific S3 tools for structured data
3. **Refine queries**: More specific queries generally return better results
4. **Check relevance scores**: Scores above 0.7 are typically very relevant

## Troubleshooting

- **"Knowledge Base ID not configured"**: Update `KNOWLEDGE_BASE_ID` in `kb_config.py`
- **"Knowledge Base not found"**: Check the KB ID is correct and exists in us-east-1
- **"Access denied"**: Ensure your AWS role has `bedrock-agent-runtime:Retrieve` permissions
