import Matter from "matter-js";
import * as PIXI from "pixi.js";
import Entity from "./Entity";

export default class Hole extends Entity {
    constructor(x, y, r = 40) {
        const body = Matter.Bodies.circle(x, y, r, {
            label: "hole",
            isSensor: true,
            isStatic: true,
        });
        const graphics = new PIXI.Graphics();
        graphics
            .beginFill(0xffffff, 0.001)
            .lineStyle({ width: 3, color: 0xffffff })
            .drawCircle(0, 0, r)
            .endFill();
        graphics.position.set(x, y);
        super(body, graphics);
    }
}
