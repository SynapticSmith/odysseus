import os
import re

def get_files_in_dir(directory, extension=None, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = ['.git', '__pycache__', 'node_modules', 'dist', 'build', 'venv', '.pytest_cache']

    files_list = []
    if not os.path.isdir(directory):
        return sorted(files_list)

    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if not any(os.path.join(root, d).endswith(ex) for ex in exclude_dirs)]
        for file in files:
            if extension is None or file.endswith(extension):
                filepath = os.path.join(root, file)
                files_list.append(filepath.replace('\\', '/'))
    return sorted(files_list)

def format_files_to_markdown(files, base_dir=""):
    items = []
    for f in files:
        if base_dir and f.startswith(base_dir):
            display_path = f[len(base_dir):].lstrip('/')
            items.append(f"[`{display_path}`](../{f})")
        else:
            items.append(f"[`{f}`](../{f})")

    lines = []
    for i in range(0, len(items), 5):
        lines.append("- " + ", ".join(items[i:i+5]))
    return "\n".join(lines)

def generate_full_repository_list():
    repo_root = '.'

    # 1. Frontend
    frontend_files = [f for f in get_files_in_dir('static') if f != 'static/js/MODULE_SUMMARY.md']
    frontend_md = format_files_to_markdown(frontend_files)

    # 2. Backend & Core
    app_files = ['app.py', 'setup.py', 'pyproject.toml', 'requirements.txt', 'requirements-optional.txt']
    core_files = get_files_in_dir('core')
    src_files = get_files_in_dir('src')
    routes_files = get_files_in_dir('routes')
    services_files = get_files_in_dir('services')
    docker_files = get_files_in_dir('docker')

    backend_core = app_files + core_files + src_files + routes_files + services_files + docker_files
    backend_md = format_files_to_markdown(sorted(backend_core))

    # 3. Ops, Scripts, Config
    config_files = get_files_in_dir('config')
    scripts_files = get_files_in_dir('scripts')
    ops_files = ['docker-compose.yml', 'docker-compose.gpu-nvidia.yml', 'docker-compose.gpu-amd.yml', 'Dockerfile', 'launch-windows.ps1', 'start-macos.sh', 'update_windows.bat', 'build-macos-app.sh', 'install-service.sh', 'odysseus-ui.service']

    ops_scripts_md = format_files_to_markdown(sorted(config_files + scripts_files + ops_files))

    # 4. Docs & Licenses
    docs_files = [f for f in get_files_in_dir('docs') if f != 'docs/ARCHITECTURE.md']
    licenses_files = get_files_in_dir('licenses')
    root_docs = ['README.md', 'CONTRIBUTING.md', 'ACKNOWLEDGMENTS.md', 'ROADMAP.md', 'SECURITY.md', 'THREAT_MODEL.md', 'LICENSE']

    docs_licenses_md = format_files_to_markdown(sorted(docs_files + licenses_files + root_docs))

    # 5. Tests
    unit_tests = [f for f in get_files_in_dir('tests') if f.startswith('tests/') and not f.startswith('tests/cli/')]
    cli_tests = get_files_in_dir('tests/cli')

    tests_md = f"#### Unit & Integration Tests\n{format_files_to_markdown(unit_tests)}\n\n#### CLI Tests\n{format_files_to_markdown(cli_tests)}"

    return f"""## Detailed File Repository
This section provides an exhaustive list of the files that make up the system architecture, organized by their domain.

### Frontend Files
{frontend_md}

### Backend & Core Logic
{backend_md}

### Infrastructure, Ops & Scripts
{ops_scripts_md}

### Documentation & Repository Guidelines
{docs_licenses_md}

### Testing & Validation
{tests_md}
"""

if __name__ == "__main__":
    doc_path = 'docs/ARCHITECTURE.md'
    with open(doc_path, 'r') as f:
        content = f.read()

    # 1. Regenerate entire Detailed File Repository section
    start_idx = content.find("## Detailed File Repository")
    if start_idx != -1:
        content = content[:start_idx] + generate_full_repository_list()

    # 2. Tighten Language across the document (remove speculative claims)
    replacements = {
        "empowering the student model to succeed on similar tasks in the future.": "empowering the student model to succeed on similar tasks.",
        "It is designed to be local-first and privacy-focused, treating the environment as a privileged admin console for private networks.": "It is a local-first, privacy-focused application, treating the environment as a privileged admin console.",
        "Odysseus features a registry of native automation actions that can be executed periodically by the task scheduler without needing to spin up an LLM.": "Odysseus contains a registry of native automation actions executed periodically by the task scheduler.",
        "An iterative `Think \u2192 Search \u2192 Extract \u2192 Synthesize` loop that generates sub-queries, executes searches, extracts content, and synthesizes findings into a final report.": "Implements an iterative loop for complex web searching, summarization, and extracting topic intent.",
        "The system coordinates between multiple LLM backends (local Ollama, OpenAI, Anthropic) while also maintaining a persistent RAG index.": "The system interfaces with multiple LLM backends while maintaining a persistent RAG index."
    }

    for old_text, new_text in replacements.items():
        content = content.replace(old_text, new_text)

    # 3. Fix EOF whitespace
    lines = content.splitlines()
    while lines and lines[-1].strip() == '':
        lines.pop()
    content = '\n'.join([line.rstrip() for line in lines]) + '\n'

    with open(doc_path, 'w') as f:
        f.write(content)
