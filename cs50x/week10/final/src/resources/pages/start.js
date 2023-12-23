import Matter from "matter-js";
import * as PIXI from "pixi.js";
import Page from "../../classes/Page";
import Button from "../../classes/Button";
import game from "../game";
import welcome from "./welcome";
import ball from "../entities/ball";
import levels from "../levels";
import plank from "../entities/plank";

const style = {
    fill: 0xffffff,
    fontSize: 35,
};
const start = new Page();
const interfaceContainer = new PIXI.Container();
interfaceContainer.addChild(
    new Button(
        "Back",
        { x: 530, y: 50 },
        {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.onback();
            },
        }
    )
);
const life = new PIXI.Text("life:", style);
life.anchor.set(0, 0.5);
life.position.set(20, 50);
const lifeNumber = new PIXI.Text(game.life, style);
lifeNumber.anchor.set(0, 0.5);
lifeNumber.position.set(60, 0);
life.addChild(lifeNumber);

const level = new PIXI.Text("lv:", style);
level.anchor.set(0, 0.5);
level.position.set(150, 50);
const levelNumber = new PIXI.Text(levels.current.name, style);
levelNumber.anchor.set(0, 0.5);
levelNumber.position.set(40, 0);
level.addChild(levelNumber);

start.addLevel = (level) => {
    start.addComposite(level.composite);
    start.addContainer(level.container);
    levelNumber.text = levels.current.name;
};
start.removeLevel = (level) => {
    start.removeComposite(level.composite);
    start.removeContainer(level.container);
};
start.addLevel(levels.current);
const nextPopUp = new Button(
    "Next",
    { x: 300, y: 500 },
    {
        onpointerdown: (e) => {
            e.target.onpointerleave(e);
            start.onnext();
        },
    }
);
nextPopUp.visible = false;
interfaceContainer.addChild(nextPopUp);
ball.onfalling(() => {
    try {
        if (start.displayed) {
            game.life -= 1;
        }
    } catch (error) {
        start.removeLevel(levels.current);
        levels.reset();
        start.addLevel(levels.current);
        game.life = 3;
    }
    lifeNumber.text = game.life;
});
ball.ontop(() => {
    start.removeLevel(levels.current);
    ball.reset();
    plank.reset();
    start.displayed = false;
    nextPopUp.visible = true;
});
interfaceContainer.addChild(life, level);
start.addContainer(interfaceContainer);

start.container.on("added", () => {
    start.displayed = true;
});
start.container.on("removed", () => {
    start.displayed = false;
});

start.onback = (e) => {
    game.switchPage(start, welcome);
};

start.onnext = () => {
    try {
        levels.next();
    } catch (error) {
        console.log(error);
    }
    ball.reset();
    plank.reset();
    nextPopUp.visible = false;
    levelNumber.text = levels.current.name;
    start.displayed = true;
    start.addLevel(levels.current);
};

export default start;
