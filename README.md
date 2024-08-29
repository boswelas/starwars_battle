<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT LOGO -->
<div align="center">
<h2 align="center">Star Wars Character Battle</h2>
  <p align="center">
    Star Wars Character Battle allows users to simulate battle between their favorite Star Wars characters and receive a personalized story about the battle. 
    <br />
    <a href="https://github.com/boswelas/starwars_battle"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <span>Check it out live at </span><a href="https://starwars-battle.vercel.app/">starwars-battle.vercel.app</a>
      <br />
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#problems-and-solutions">Problems and Solutions</a></li>
    <li><a href="#future-goals">Future Goals</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
Characters are selected on the main page, and users can read details about them that are scraped from https://starwars.fandom.com/ . Character stats used in battle are based on the Star Wars card game stats available on the fandom site, with some liberties taken to fill in missing pieces. The battle result is determined with an algorithm developed for the project. From there, the results are fed to the ChatGPT API, which creates a narrative specific to the battle.

Admittedly, this project was really an excuse just to make something goofy and learn about web-scraping (I succeeded at both!).

<p align="right">(<a href="#readme-top">back to top</a>)</p>




## Built With
* Python
* Playwright
* BeautifulSoup4
* TypeScript
* Next.js
<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/github_username/repo_name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```
5. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin github_username/repo_name
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

![til](./frontend/public/images/star_wars_demo.gif)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- PROBLEMS AND SOLUTIONS -->
## Problems and Solutions
### The Problem
<p>After deploying the project backend on Railway.app, I encountered a pretty common CORS no “Access-control-allow-origin” error. Initially, I assumed the error had to do with how my frontend was hosted on Vercel, so to begin trouble-shooting, I updated the CORS policy to allow all origins. When that and several other CORS-related changes didn’t work, I took to combing through the server logs.
  
After spending quite a bit of time deep in the logs, I found this line:
/opt/venv/lib/python3.11/site-packages/playwright/driver/node: /lib/x86_64-linux-gnu/libc.so.6: version `GLIBC_2.38' not found (required by /nix/store/p3ffjixpnfgkqh20nsrc13vrj3yfi0nj-gcc-13.2.0-lib/lib/libstdc++.so.6)
</p>

### The Solution
<p>The issue turned out to be a problem specific to using Playwright on Railway. Per existing threads, Railway support recommended using Browserless, which appeared to be a paid service. Other solutions I considered were switching to another web scraping tool or hosting the project backend elsewhere.

However, the solution found <a href="https://www.answeroverflow.com/m/1161366860705566924" target=”blank” >here</a> was simpler.

I created a railway.json file to build and deploy, and changed the Nixpacks version to an older version (1.14.0). 
</p>

### What I Learned
<p>CORS errors are most often caused by server misconfigurations, network issues, and incorrect URL or endpoints. However, there are also times when server or environment issues can manifest as CORS errors, even though the root cause is unrelated to CORS itself. 

In this case, the CORS error occurred because the server couldn't start properly due to a missing GLIBC_2.38 dependency, causing it to fail in responding to requests. When the server can't process requests correctly, it often doesn't send the expected CORS headers, leading the browser to mistakenly interpret the issue as a CORS error. By downgrading Nixpacks, I resolved the server's underlying issue, allowing it to respond correctly and eliminating the CORS error.
</p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE GOALS -->
## Future Goals

<p>There are still a couple features I plan to implement in the future.

* Improve performance by storing character data in a database table so that only never-before-scraped characters need to be scraped in real time.
* Craft a more engaging loading screen by displaying battle calculations in real time while loading the results page.
</p>
<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
