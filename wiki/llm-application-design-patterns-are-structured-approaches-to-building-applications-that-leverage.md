# LLM application design patterns are structured approaches to building applications that leverage large language models (LLMs). These patterns provide a framework for developers to efficiently integrate LLMs into their systems and products. Here are some of the key design patterns:

LLM application design patterns are structured approaches to building applications that leverage large language models (LLMs). These patterns provide a framework for developers to efficiently integrate LLMs into their systems and products. Here are some of the key design patterns:

**In-context Learning**

*   **Description**: Utilizes LLMs off the shelf, controlling behavior through prompting and contextual data.
*   **Components**: LLMs, prompt templates, few-shot examples, external APIs, vector databases.
*   **Benefits**: Reduces AI problems to data engineering problems, real-time data incorporation.
*   **Real-world Examples**: Chatbots, legal document analysis.
*   **Significance**: Simplifies AI development, outperforms fine-tuning for small datasets.

```
graph TD
    A[User Query] -->|Input| B[Prompt Construction/Retrieval]
    B -->|Determines relevance| D[Vector Database]
    E[External APIs] -->|Provides data| B
    F[Embedding Model] -->|Processes data| D
    G[Data Preprocessing/Embedding] -->|Stores data| D
    B -->|Compiled Prompt| H[Prompt Execution/Inference]
    H -->|Submits to LLM| I[Pre-trained LLM]
    I -->|Inference| J[Operational Systems]
    J -->|Logging, Caching, Validation| K[User Response]
```

**Data Preprocessing/Embedding**

*   **Description**: Involves storing private data to be retrieved later, breaking documents into chunks, and storing them in a vector database.
*   **Components**: Embedding models, vector databases.
*   **Benefits**: Efficient data retrieval for LLM processing.
*   **Real-world Examples**: Data-sensitive applications requiring privacy.
*   **Significance**: Enables efficient handling of large datasets.

```
graph TD
    A[Raw Data] -->|Input| B[Data Preprocessing]
    B -->|Chunks| C[Embedding Model]
    C -->|Embeddings| D[Vector Database]
    D -->|Stored for Retrieval| E[LLM Application]
    E -->|Retrieves relevant data| F[Prompt Construction]
```

Did you enjoy reading this on SMRY?

Tell us what would make the reader better

Did you enjoy reading this on SMRY?

Tell us what would make the reader better

## Related
[Add wiki-links manually or run update_wikilinks.py]