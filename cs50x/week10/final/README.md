# BALANCING BALL GAME USING MATTERJS AND PIXIJS
### Video Demo: https://youtu.be/jx0XzURekqY
### Description:
For the development of this project, I'm using [vite](https://vitejs.dev/) with vanilla JavaScript. The command `yarn create vite final –template vanilla` generate final directory containing:
```
├── counter.js
├── index.html
├── javascript.svg
├── main.js
├── package.json
├── public
│   └── vite.svg
└── style.css
```
After cleaning unrelated files to the project, it left with:
```
├── index.html
├── main.js
├── package.json
├── public
└── style.css
```
Installing the matterjs and pixijs using `yarn add matter-js pixi.js`. Matterjs act as a physics `engine` and pixijs act as renderer. First, creating a class representing a game, all classes live under `src/classes/`. A `Game` has an `engine`, a matterjs object that responsible for calculating physical properties of an `entity`. An `app`, a part of pixijs that responsible for creating a UI and displaying entities to the screen. The `Game` class extends from `Page` class, the `Page` class represents a page in the game. It has a `composite`, a matterjs object that holds bodies. A `container`, a pixijs object that holds `graphics`.


The `Entity` class represents an object that can interact with other entities in the `world`. `Entity` has a `body`, matterjs object representing rigid body inside matterjs `world` that can interact with other `body` and the `world` physical properties such as gravity. A `graphics`, a pixijs object that responsible for displaying the `body` on the screen. The Button class only has a `graphics` because it doesn’t interact with any `entity` in the `world`. `Hole` class represents a hole that extends from `Entity` class, its `body` is a circle that is a sensor and static, its `graphics` is also a circle with alpha of 0.001 and line width of 3. Next, `Level` class represents a level that contains holes and `Levels` class represents all `Level`.


The `src/resources/` directory contains instances of classes and other resource. First, there is `game.js`, an instance of `Game`, `levels.json` contains all of the level name and holes position. `Levels.js` contains `Levels` instance. On the `src/resources/entities/` live all the instances of `Entity` class, they can interact with the `world` and each other. There are ball and plank. `src/resources/pages` contains all the game pages like `welcome.js`, the first thing you see when opening the game, `start.js` the page where you play the levels and `create.js` where you create a level


Finally, on the `main.js` where you assemble all resource by adding ball and plank to game and updating them, adding a collision rule for a ball and holes, adding welcome page to the game. The complete structure of the `final` directory is:
```
├── index.html
├── main.js
├── package.json
├── public
├── README.md
├── README.md.old
├── src
│   ├── classes
│   │   ├── Button.js
│   │   ├── Entity.js
│   │   ├── Game.js
│   │   ├── Hole.js
│   │   ├── Level.js
│   │   ├── Levels.js
│   │   └── Page.js
│   └── resources
│       ├── entities
│       │   ├── ball.js
│       │   └── plank.js
│       ├── game.js
│       ├── levels.js
│       ├── levels.json
│       └── pages
│           ├── create.js
│           ├── start.js
│           └── welcome.js
├── style.css
└── yarn.lock
```
