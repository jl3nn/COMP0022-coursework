# COMP0022 Coursework

## 1 - Quick Start Guide

To run the system, follow these steps:
1. Clone this GitHub repo
2. Create a `.env` file in the root directory, based off `.env.template`
3. Run `docker compose up --build`
4. Connect to `localhost`

## 2 - Dev practices

- When making changes, please add an issue to the project in GitHub.
- Allocate and progress that issue, creating a new branch with the same name.
- Make changes on the new branch.
- Push changes and create a Pull Request.
- Request review of the PR.
- If the review and GitHub Action checks pass, Squash changes into a single commit with a commit name equal to the branch name.

## 2 - Application Architecture

The application consists of a React frontend (`/client`), a Flask backend (`/server`), two database instances, for isolated data, (`/database` and `/personality-database`), further Reids is used before querying either database. Lastly, logging and alerting are set up (`\postgres` and `\grafana`).

The following ports are open:
- `80` - For hosting the frontend
- `5555` - For API server requests
- `3000` - For the Grafana Dashboard

All configuration is managed through Docker Compose. Any relevant passwords are defined in `.env.template`.

![System Arcitecture](./media/SystemDesign.drawio.png)

## 3 - Database Documentation

The main database has the following tables:

- movies
- users
- ratings
- tags
- genres
- actors
- directors
- movies_directors
- movies_actors
- movies_genres
- movies_users_tags

![ERD of main table](./media/mainERD.drawio.png)

The Personality database has the following tables:

- users
- movies
- ratings
- genres
- movie_genre

![ERD of personality table](./media/PersonalityERD.drawio.png)

## 4 - API Documentation

See [the docs](serverDocs.md), or, got to `http://localhost:5555/apidocs` if the application is running.
