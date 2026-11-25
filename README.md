# AI From Scratch: From Silicon to Intelligence

An educational reconstruction of a modern language-model pipeline, not a disclosure of proprietary model weights, private reasoning traces or exact deployment.

[Project website](https://krazad0.github.io/AI-FROM-SCRATCH/) · [Local website](index.html)

## Roadmap

1. [Silicon](chapters/01.md)
2. [Transistors](chapters/02.md)
3. [Digital logic](chapters/03.md)
4. [Computer architecture](chapters/04.md)
5. [GPUs](chapters/05.md)
6. [System software](chapters/06.md)
7. [Programming](chapters/07.md)
8. [Mathematics](chapters/08.md)
9. [Neural networks](chapters/09.md)
10. [Tokenization](chapters/10.md)
11. [Embeddings](chapters/11.md)
12. [Transformers](chapters/12.md)
13. [Training](chapters/13.md)
14. [Post-training](chapters/14.md)
15. [Reasoning](chapters/15.md)
16. [Context and cache](chapters/16.md)
17. [Tools and agents](chapters/17.md)
18. [Decoding](chapters/18.md)
19. [Infrastructure](chapters/19.md)
20. [Build a miniature model](chapters/20.md)

## Run the labs

Requires Python 3; no third-party packages.

```sh
python3 examples/logic.py
python3 examples/bigram.py
python3 examples/attention.py
```

The bigram is trained; attention uses fixed toy vectors. Neither is a full GPT. These chapters are introductory notes.

## References

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
- [Instruction tuning](https://arxiv.org/abs/2203.02155)
- [FlashAttention](https://arxiv.org/abs/2205.14135)
- [CUDA programming guide](https://docs.nvidia.com/cuda/cuda-c-programming-guide/)
- [Metal documentation](https://developer.apple.com/metal/)
