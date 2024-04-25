# Assignment 1 - Individual
## Documentation (Tasks 5-7)
### Cherry Pick
* Cherry Picked the commit [eef4e08](https://github.com/annayPaul/git-assignment-1/commit/eef4e08d8f182e9ee2f0ec1c3baed1eb3ab94bb5) from branch [experimental-branch](https://github.com/annayPaul/git-assignment-1/compare/experimental-branch) into main
* For adding a programming problem: Added the fibonacci function that calucaltes the ith fibonacci number
### Revert Changes
* Added a .gitignore file in the commit [4b19a4b](https://github.com/annayPaul/git-assignment-1/commit/4b19a4bfd7d157b7838cefcd8560abc30d7210d4) and Reverted this commit in [e2309cac](https://github.com/annayPaul/git-assignment-1/commit/e2309cacab60ce846587065d77ef7a1fd7e11d2f)
* Modified the `fibonacci` function to cause errors
### Reset
* Used `git reset --hard HEAD~1` to Reset back to the working code
* Differences between
  - `--soft`: Restores the desired commit, does not change the staging area & working directory
  -   `--mixed`: (Default) Restores the desired commit and changes the staging area. Keeps the working directory unchanged
  -   `--hard`: Restores the desired commit in the modifies the staging area & working directory as well 
### Squash
![image](https://github.com/annayPaul/git-assignment-1/assets/168059220/6f3644be-35df-4954-b039-b7594eae1eb1)
Squashed 3 commits into 1. Stored those 3 commits the the "squash" branch

### Delete
![image](https://github.com/annayPaul/git-assignment-1/assets/168059220/085ad02b-6ff6-4767-9f00-0acebd890d8e)
Deleted a file
### Stash
![image](https://github.com/annayPaul/git-assignment-1/assets/168059220/5eb99880-b754-4369-bd1a-6758c96162bb)
