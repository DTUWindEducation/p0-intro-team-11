Questions Week 1

1. What is the difference between git and GitLab?

Git is a software program, whereas GitLab is an online hosting service.

2. What is the difference between GitLab, GitHub, and BitBucket?

GitHub, GitLab, and Bitbucket are all Git repository hosting services

3. Why would I ever want to use git, but not GitLab?

If I want a local version of a file (only me working on it).

4. What are the steps to update the GitLab server with some changes I made on my computer?

- Navigate to the repo
- git add
- git commit (add text)
- git pull

5. What is a branch and why would I use one?

It allows me to work on different features, fixes, or experiments without affecting the main codebase.

6. How could you visualize a branch with 3 commits, and then another branch that breaks off after the second commit and has a single commit?

A---B---C  (main branch)
      \
       D  (feature branch)


7. Give an example of a set of git commands that would result in a merge conflict.

- Me and teammate make an edit to the same line of code
- They push to the server
- I try to push to the server - it gets rejected


8. Is Git suitable for latex documents?

Yes, as it can track changes line by line.

9. Should I from now on version my word and powerpoint slides using git? Why/why not?

No, as they are completely different file types.

10. What could happen when I push my latest commit to the remote repository without pulling first?

If someone has made edits, it could create a merge conflict.

11. What happens when I pull without commiting my local changes first?

If someone has made edits, it could create a merge conflict.

12. What is the difference between branching and forking?

Branching is a way of diverging from the main line of development within the same repository. Forking involves creating a copy of an entire repository under your own GitHub account. This copy is completely separate from the original repository, and you can make changes without affecting the original project.