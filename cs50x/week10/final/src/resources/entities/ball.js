import * as PIXI from "pixi.js";
import Matter from "matter-js";
import Entity from "../../classes/Entity";
import game from "../game";

const x = 300;
const y = 900;
const r = 20;

const body = Matter.Bodies.circle(x, y, r, {
    label: "ball",
    angle: 0,
    density: 50,
    restitution: 0,
    friction: 0,
    frictionStatic: 0,
    frictionAir: 0,
});

const graphics = new PIXI.Graphics();
graphics.beginFill(0xff0000).drawCircle(0, 0, r).endFill();

const ball = new Entity(body, graphics);
ball.isFalling = () => {
    return (
        ball.body.position.y > game.app.view.height ||
        ball.body.position.x < 0 ||
        ball.body.position.x > game.app.view.width
    );
};
const onFallingCallback = [];
ball.onfalling = (callback) => {
    onFallingCallback.push(callback);
};
ball.isOnTop = () => {
    return ball.body.position.y < 0;
};
const onTopCallback = [];
ball.ontop = (callback) => {
    onTopCallback.push(callback);
};
ball.reset = () => {
    Matter.Body.setPosition(ball.body, { x: x, y: y });
    Matter.Body.setVelocity(ball.body, { x: 0, y: 0 });
    Matter.Body.setAngle(ball.body, 0);
};
ball.update = () => {
    ball.graphics.position.set(ball.body.position.x, ball.body.position.y);
    if (ball.isFalling()) {
        onFallingCallback.forEach((fn) => fn(ball));
    }
    if (ball.isOnTop()) {
        onTopCallback.forEach((fn) => fn(ball));
    }
};

export default ball;
