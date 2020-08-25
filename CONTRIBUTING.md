# Contributing

First off, thank you for considering contributing to Z-polls. It's people
like you that make Z-polls such a great tool.

<hr>

### Where do I go from here?

If you've noticed a bug or have a feature request, [make one][new issue]! It's
generally best if you get confirmation of your bug or approval for your feature
request this way before starting to code.

### Fork & create a branch

If this is something you think you can fix, then fork Z-polls and create
a branch with a descriptive name.

### Getting Started

Make sure you're using python3 (preferably 3.8, 3.7, 3.6) and have pip installed.

Now install the development dependencies(Django, Bulma):

```
cd Z-polls
python3 -m venv {your-venv-name}
source {your-venv-name}/bin/activate
pip install -r requirements.txt
```

To start Development server:

```
python3 manage.py migrate
python3 manage.py runserver
```

Then enter the link provided by your terminal in your browser.

To Create Super User (for exploring purposes):-

```
python3 manage.py createsuperuser
```
Then fill in your detail.

### Implement your fix or feature

At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first 😸

### Merging a PR (maintainers only)

* A PR can only be merged into master by a maintainer if:
* It has been approved by at least two maintainers. If it was a maintainer who opened the PR, only one extra approval is needed.
* It has no requested changes.
* It is up to date with current master.
* Any maintainer is allowed to merge a PR if all of these conditions are met.

### Shipping Release(maintainers only):

* The website is completely functional
* There are no bugs remaining in the particular issue
* The changes are Documented

### Issue and Pull Request Labels
This section lists the labels we use to help us track and manage issues and pull requests. Most labels are used across all Atom repositories, but some are specific to cdh77/Z-polls.

GitHub search makes it easy to use labels for finding groups of issues or pull requests you're interested in. For example, you might be interested in open issues across cdh77/Z-polls and packages which are labeled as bugs, but still need to be reliably reproduced or perhaps open pull requests in cdh77/Z-polls which haven't been reviewed yet. To help you find issues and pull requests, each label is listed with search links for finding open items with that label in cdh77/Z-polls only.

The labels are loosely grouped by their purpose, but it's not required that every issue have a label from every group or that an issue can't have more than one label from the same group.

Please open an issue on cdh77/Z-polls if you have suggestions for new labels, and if you notice some labels are missing on some repositories, then please open an issue on that repository.

<hr>

References:-
* [Python Docs](https://docs.python.org/)
* [Django docs](https://docs.djangoproject.com/en/)
* [Bulma Docs](https://bulma.io/documentation/)
* [Github Docs](https://docs.github.com/en)
* [Github Guides](https://guides.github.com/en)

<hr>

