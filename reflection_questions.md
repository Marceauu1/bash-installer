Git & GitHub Reflection Questions

1. Why is version control useful?
- History & undo power: Records every saved snapshot of a project so you can see what changed, when, and why—and roll back if something breaks.
- Safe experimentation: Lets you test new ideas or scripts without risking a working version of your project.
- Collaboration & backups: Allows multiple people to work on the same codebase without overwriting each other's work, and pushing to a remote like GitHub provides an off-machine backup.

2. What is the difference between staging and committing?
- Staging (`git add`): Selects and prepares specific changes in your working directory for the next snapshot (the staging area), letting you choose *what* goes into a commit.
- **Committing (`git commit`): Permanently records everything currently staged as a new snapshot in your repository's history with a descriptive message.

3. When should you make a commit?
- Whenever you reach a small, logical, working checkpoint**—such as creating a README, adding and testing a script, or fixing a single bug.

4. What is the difference between `git init` and `git clone`?
- `git init`: Initializes a brand-new Git repository locally inside an existing folder (creating `.git`) with no commit history or remote yet.
- `git clone`:** Downloads an existing repository from a remote source (like GitHub), including its full commit history, branches, and `origin` remote configuration.

5. Why should you write good commit messages?
- Clear, specific messages (e.g., `"Add installation script"`) make `git log` readable so you and teammates can quickly understand what each commit changed and why without reading every diff.

6. What is the purpose of using branches?
- Branches create isolated lines of development inside the same repository, allowing you to build features or test changes independently without destabilizing `main`.

7. When would you create a new branch instead of working on `main`?
- Whenever you start a new feature, script, bug fix, or experiment—keeping `main` reserved for clean, completed, integrated work.
