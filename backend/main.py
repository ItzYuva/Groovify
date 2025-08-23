import modal

app = modal.app("music-generator")

image = (
    modal.Image.debian_slim()
    .apt_install("git")
    .pip_install_from_requirements("requirements.txt")
    .run_commands(["git clone https://github.com/ace-step/ACE-Step.git /tmp/ACE-STEP", "cd /tmp/ACE-STEP && pip install ."])
    .env({"HF_HOME": "/.cache/huggingface"})
)