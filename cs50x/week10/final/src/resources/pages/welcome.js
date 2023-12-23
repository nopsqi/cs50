import Matter from "matter-js";
import * as PIXI from "pixi.js";
import game from "../game";
import Page from "../../classes/Page";
import Button from "../../classes/Button";
import start from "./start";
import create from "./create";

const buttons = [
    {
        text: "Start",
        position: {
            x: -75,
            y: 0,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.onstart();
            },
        },
    },
    {
        text: "Create",
        position: {
            x: 75,
            y: 0,
        },
        eventsHandler: {
            onpointerdown: (e) => {
                e.target.onpointerleave(e);
                e.target.page.oncreate();
            },
        },
    },
];

const welcome = new Page();
const buttonContainer = new PIXI.Container();
buttons.forEach((button) =>
    buttonContainer.addChild(
        new Button(button.text, button.position, button.eventsHandler)
    )
);
buttonContainer.position.set(300, 400);
welcome.addContainer(buttonContainer);

welcome.onstart = () => {
    game.switchPage(welcome, start);
};

welcome.oncreate = () => {
    game.switchPage(welcome, create);
};

export default welcome;
