## What is Tokenization
---

 LLMs break down their vocabulary into tokens. Tokens include words, but also sub-words (like the "un" in "unbelievable" and "unlikely"), punctuation, and other commonly used sequences of characters. The first step in training a large language model therefore is to break down the training text into its distinct tokens, and assign a unique integer identifier to each one.

---

## The 3-Part Interview Framework

### 1. The High-Level Definition (The "Hook")

> "At a fundamental level, Large Language Models cannot process raw text; they only understand mathematics. Tokenization is the preprocessing step that breaks down natural language into smaller units called **tokens**, and maps them to unique integer IDs from a predefined vocabulary dictionary. It bridges human language and neural network inputs."

### 2. The Core Mechanism (Demonstrating Technical Depth)

> "Modern production LLMs use **sub-word tokenization** algorithms, such as Byte-Pair Encoding (BPE) or WordPiece. Instead of splitting strictly by words or characters, it breaks text into frequent sub-words. Common words like `'computer'` become a single token, while unseen or complex words are split into roots and suffixes, like `'token'` and `'ization'`. This neatly solves the out-of-vocabulary problem and optimizes data compression."

### 3. Practical Engineering Impact (The "Senior Engineer" Edge)

> "As an engineer, tokenization dictates three critical operational constraints that I keep in mind when designing architectures:
> * **Context Windows:** Context limits are measured in tokens, not words. 100 English words generally translate to roughly 130 to 140 tokens.
> * **The Multilingual Cost:** Tokenizers are heavily optimized for English. Languages with non-Latin scripts, like Hindi or Arabic, get aggressively fractured into individual byte characters. This means non-English inputs consume context windows drastically faster and drive up API token billing costs.
> * **Model Blindspots:** Because the LLM only observes token IDs, it lacks intuitive character-level visibility. This explains why base LLMs inherently struggle with raw character tasks, like counting specific letters inside a word or resolving complex anagrams without explicit chain-of-thought prompt coaching."
> 
> 

---

## Pro-Tips for the Interview Room

* **Avoid the "Word-by-Word" Trap:** If you say "it splits sentences into words," an experienced interviewer will immediately flag it as inaccurate. Make sure to emphasize **sub-word** tokenization.
* **Keep it Conversational:** If they ask for a concrete example to verify your understanding, drop the **"Strawberry" anomaly**: *"It’s why an LLM fails if you ask it to count the 'r's in Strawberry—it doesn't see the letters 'S-t-r-a-w-b-e-r-r-y', it only sees the ID tokens for `[Straw]` and `[berry]`."* This proves you understand the edge cases of model limitations.


# Q) What is the difference between tokens and embeddings in LLMs?

**Tokens** are the fundamental units of language that a Large Language Model (LLM) processes, whereas **embeddings** are the complex mathematical representations that capture the deep meaning and context of those tokens. 

Here is a breakdown of how they differ and work together:

**Tokens: The Building Blocks**
Before an LLM can analyze text, it must break the language down into manageable pieces called **tokens**. 
*   **What they are:** Tokens can be whole words, sub-words (such as the "un" in "unbelievable"), punctuation marks, or other commonly used sequences of characters. 
*   **How they are represented:** During training, the model catalogs these distinct tokens and assigns a unique integer identifier to each one. For instance, the word "dog" might simply be assigned the ID "4". 

**Embeddings: The Semantic Meaning**
While a token ID acts as a label, it does not tell the model what the word actually means. That is where embeddings come in.
*   **What they are:** To understand relationships between tokens, the model assigns each token a vector—an array of multiple numeric values, such as. These initial vectors are then fed through a **transformer model** that uses a technique called *attention* to evaluate how each token is influenced by the surrounding tokens in the text. 
*   **How they capture context:** The transformer adjusts these vectors based on the contexts in which the tokens appear, producing new vectors that have semantic and linguistic characteristics embedded within them—hence the name **embeddings**. 
*   **Multi-dimensional relationships:** You can think of the elements inside an embedding as dimensions in a multi-dimensional vector-space. Because these values are calculated based on linguistic relationships, tokens used in similar contexts will result in vectors that point in similar directions. For example, the embeddings for "dog" and "puppy" will be closely aligned with each other, but very different from the embedding for a token like "skateboard".


# Q) How do transformers use attention to understand word relationships?

Transformers use **attention** as a mechanism to evaluate how individual tokens (words or sub-words) are influenced by the other tokens surrounding them within a given sequence. 

Here is how the attention process allows transformers to build a deep understanding of word relationships:

*   **Assigning Contextual Weights:** When evaluating a specific token, the attention layer looks at the surrounding tokens and assigns them "weights" to reflect their level of influence. For example, in the sentence "I heard a dog bark," when the model evaluates the token "bark," it will assign higher weights to the words "heard" and "dog" than it will to "I" or "a." This is because "heard" and "dog" are much stronger contextual indicators for "bark".
*   **Calculating Embeddings:** The transformer uses these calculated weights to adjust the numerical values within the token's embedding vector. This ensures the resulting vector accurately captures the word's semantic meaning based on the specific context in which it is being used.
*   **Learning Patterns Over Time:** Initially, an untrained model does not know which tokens influence each other. However, as it processes massive volumes of training text, it iteratively learns which words frequently appear close together. By analyzing the proximity and frequency of token pairings, it uncovers patterns that allow it to assign vector values that truly reflect human linguistic structures.
*   **Parallel Processing via Multi-head Attention:** To make this massive number of calculations highly efficient, transformers use a technique called **multi-head attention**. This allows the model to evaluate multiple elements or dimensions of a token's vector simultaneously in parallel.

It is also important to note that attention operates slightly differently depending on what part of the transformer is running. While an **encoder** block uses attention to look at all surrounding tokens to build rich embeddings, a **decoder** block uses **masked attention** to predict the next word in a sequence. Masked attention restricts the model so it can only consider the tokens that *precede* the current token, ignoring any future tokens since they would be unknown during live text generation.



# Q) How does a model predict the next word in a sequence?

To predict the next word in a sequence, a large language model relies on the **decoder block** of its transformer architecture to iteratively calculate the most probable continuation of the text.

Here is a breakdown of how this predictive process works:

*   **Evaluating the Context:** The model analyzes the sequence of tokens provided so far (the prompt) to understand the relationships and semantic context. Strong indicator words in the sequence help the model narrow down the probabilities for what might come next. 
*   **Applying Masked Attention:** The decoder uses a technique called **masked attention** to consider each token in context. This mechanism ensures the model only looks at the tokens that *precede* the one it is trying to predict, assigning weights to those prior tokens based on their contextual influence.
*   **Determining the Most Probable Token:** The attention layers calculate possible vector representations for the next token, and a feed-forward neural network evaluates these options to identify the single most probable candidate. For example, if the sequence is *"When my dog was a..."*, the model uses the assigned attention weights to predict *"puppy"* rather than unrelated words like *"cat"* or *"skateboard"*.
*   **Iterative Generation:** Once the next token is predicted, it is appended to the current sequence. The model then repeats the entire process—evaluating the newly updated sequence to predict the *next* token—and continues this loop until it predicts that the sequence has ended.

This predictive ability is honed during the model's training phase, where it is fed vast amounts of text data for which the full sequence is already known. By predicting the next word and comparing it to the actual word in the training data, the model continuously adjusts its learned weights to reduce errors and improve its accuracy for future predictions.


# Q) What is the purpose of positional encoding for tokens?

The purpose of positional encoding is to **indicate exactly where a token appears within a sequence of text**. 

When initial token vectors are fed into a transformer model, they are accompanied by this positional information because **the specific order of the tokens is highly relevant to understanding how they relate to one another**. Without knowing the position of each word, the model would lose the structural and grammatical context of the sentence, making it unable to accurately evaluate the semantic meaning and relationships between the tokens.

# Q) What is the difference between an encoder and a decoder?

In a transformer model, the **encoder** and **decoder** are two distinct blocks that perform different but complementary roles in processing and generating language:

**The Encoder (Understanding Context)**
*   **Purpose:** The encoder's primary job is to **create embeddings** that capture the deep linguistic and semantic characteristics of each token. 
*   **How it works:** It uses an attention mechanism to examine each token in turn and determine how it is influenced by the other tokens around it. Crucially, the encoder evaluates the surrounding tokens in the sequence simultaneously to build rich, contextual vector representations. 
*   **Output:** It feeds the results of its attention layer through a fully connected neural network to produce the final, optimized embeddings that the system uses to understand the text's meaning.

**The Decoder (Generating Text)**
*   **Purpose:** The decoder's job is to use the embeddings calculated by the encoder to **iteratively predict the next most probable token** in a sequence, such as when generating a completion from a user's prompt.
*   **How it works:** While the decoder also uses attention, it relies on a restricted technique called **masked attention**. This means that when predicting a token, the decoder can only consider the context of the tokens that *precede* it. It intentionally ignores or "masks" any subsequent tokens because those words are meant to be unknown during live text generation. 
*   **Output:** By evaluating only the preceding tokens in the sequence, the decoder calculates possible vectors for the next token and uses a feed-forward neural network to identify the single most likely word to continue the sequence.



