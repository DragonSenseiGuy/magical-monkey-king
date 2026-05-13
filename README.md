# The Legend of the Monkey King

A short Ren'Py visual novel retelling the legend of Sun Wukong, the Monkey King,
followed by an analysis of his behavior from three classical Chinese viewpoints:
**Confucianism**, **Daoism**, and **Buddhism**.

Built as a school project.

## Play it in your browser

Once GitHub Pages is enabled on this repo, the latest build is automatically
deployed at:

`https://<github-user>.github.io/<repo-name>/`

## What's in the game

The story plays through nine numbered scenes (the scene number is shown in the
top-right corner during play, so it can be cited like a page number):

1. Born from Stone
2. The Hidden Cave
3. Fear of Death
4. At the Master's Temple
5. The Dragon King's Palace
6. Heaven's Stables
7. The Peach Garden
8. The Heavenly Army
9. The Buddha's Bet

After the story ends, the player can consult **Confucius**, **Laozi**, and
**the Buddha** in any order. Each teacher introduces their core ideas, then
walks through specific scenes from the story, labeling Wukong's behavior as
either `[RIGHT, by this teaching]` or `[WRONG, by this teaching]`, and closes
with practical advice on how a person should live.

## Project layout

```
game/
  script.rpy        Main story
  analysis.rpy      Three Views of the Monkey King (philosophy section)
  options.rpy       Project metadata
  images/           All backgrounds and character portraits
.github/
  workflows/
    deploy.yml      Builds the web distribution and deploys to GitHub Pages
```

## Running locally

1. Install the [Ren'Py SDK](https://www.renpy.org/latest.html) (8.3 or newer).
2. Open the SDK launcher and choose **Add Existing Project**, pointing it at
   the root of this repo.
3. Click **Launch Project**.

## How the deploy works

The workflow in `.github/workflows/deploy.yml` runs on every push to `main`. It:

1. Downloads the Ren'Py SDK and the web-support package.
2. Builds the project as a web (HTML5) distribution.
3. Uploads the resulting folder as a GitHub Pages artifact.
4. Deploys it to GitHub Pages.

After the first successful run, the game will be playable in any modern
browser at the Pages URL above.
