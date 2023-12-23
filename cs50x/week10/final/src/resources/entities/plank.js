import Matter from "matter-js";
import * as PIXI from "pixi.js";
import Entity from "../../classes/Entity";
import game from "../game";

const body = Matter.Bodies.rectangle(300, 1000, 500, 100, {
    label: "plank",
    angle: 0,
    density: 50,
    restitution: 0,
    friction: 0,
    frictionStatic: 0,
    frictionAir: 0,
    isStatic: true,
});
const graphics = new PIXI.Graphics();
graphics.beginFill(0x00ff00).drawRect(-250, 0, 500, 10).endFill();
graphics.position.set(body.position.x, 950);

const plank = new Entity(body, graphics);
const handleLeft = (value) => {
    plank.graphics.pivot.set(250, 0);
    Matter.Body.rotate(
        plank.body,
        value,
        { x: plank.body.vertices[1].x, y: plank.body.vertices[1].y },
        false
    );
    plank.graphics.position.set(
        plank.body.vertices[1].x,
        plank.body.vertices[1].y
    );
    plank.graphics.rotation = plank.body.angle;
};

const handleRight = (value) => {
    plank.graphics.pivot.set(-250, 0);
    Matter.Body.rotate(
        plank.body,
        value,
        { x: plank.body.vertices[0].x, y: plank.body.vertices[0].y },
        false
    );
    plank.graphics.position.set(
        plank.body.vertices[0].x,
        plank.body.vertices[0].y
    );
    plank.graphics.rotation = plank.body.angle;
};
const rotation = Math.PI * 0.005;
const keyHandler = {
    KeyQ: () => handleLeft(rotation),
    KeyA: () => handleLeft(-rotation),
    KeyE: () => handleRight(-rotation),
    KeyD: () => handleRight(rotation),
};
const key = new Set();
document.addEventListener("keydown", (e) => {
    key.add(e.code);
});
document.addEventListener("keyup", (e) => {
    key.delete(e.code);
});

Matter.Events.on(game.engine, "beforeUpdate", () => {
    [...key].forEach((k) => keyHandler[k]?.());
});

plank.reset = () => {
    Matter.Body.setPosition(plank.body, {x: 300, y: 1000});
    Matter.Body.setAngle(plank.body, 0, false);
    plank.graphics.pivot.set(0);
    plank.graphics.position.set(
        plank.body.position.x,
        950
    );
    plank.graphics.rotation = plank.body.angle;
};

export default plank;
